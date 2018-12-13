import pickle



from settings import logger, FIXED_FILE_NAME, ERROR_FILE_NAME, FIXED_FILE_NAME_PICKLE
# from IPython.core.display import HTML
# css = open('style-table.css').read() + open('style-notebook.css').read()
# HTML('<style>{}</style>'.format(css))

import matplotlib.pyplot as plt
import pandas as pd
import os.path


class Model:
    SLICE_X = 10
    SLICE_Y = 10

    def __init__(self):
        # self.df = self.load_data()
        self.pickle = None
        self.fixed_file = None
        self.data = None

        # self.im_x = None
        # self.im_y = None

        self.prev_data = None

    def fix_corrupted_file(self, file_name, fixed_path, corrupted_path):
        logger.debug(
            f"entering fix_corrupted_file,file_name={file_name},fixed_path={fixed_path},corrupted_path={corrupted_path}")
        logger.error(file_name)

        valid_counter = 0
        invalid_counter = 0

        # for line in fileinput.input(file_name):
        with open(file_name, 'r') as datar, open(fixed_path, "w") as fixedw, open(
                corrupted_path,
                "w",
                encoding="utf-8") as errorw:

            for line in datar.readlines():
                if (len(line.split(', ')) == 14):
                    fixedw.write(line.strip(" "))
                    valid_counter += 1
                else:
                    errorw.write(line.strip(" "))
                    invalid_counter += 1

        logger.error(f"{valid_counter} valid lines.")
        print(f"{valid_counter} valid lines.")
        logger.error(f"{invalid_counter} corrupted lines. See {corrupted_path}")

    def optimize_csv_file(self, file_name):
        logger.debug(f"entering optimize_csv_file,file_name={file_name}")

        cols_types = dict({
            'delta_time': 'object',
            'filename': 'category',
            'frame': 'uint16',
            'obj': 'uint16',
            'path_time': 'object',
            'seq': 'uint16',
            'size': 'uint32',
            'x': 'uint16',
            'y': 'uint16'})
        cols = ["frame", "x", "y", "obj", "size", "seq", "tbd1", "tbd2", "tbd3", "filename", "start", "path_time",
                "delta_time", "tbd4"]
        useful_cols = ["frame", "x", "y", "obj", "size", "seq", "filename", "start", "path_time", "delta_time"]

        df = pd.read_csv(file_name, names=cols, usecols=useful_cols, dtype=cols_types, parse_dates=['start'],
                         infer_datetime_format=True)

        logger.debug(f"optimize_csv_file: finished reading csv file")

        df = self.set_time_row(df)
        df = self.set_index(df)
        # df = self.remove_duplicates()

        return df

    def load_data(self, file_name):
        print("Loading Data...\nThis may take a while.")
        logger.debug(f"entering load_data,file_name={file_name}")

        file_name_only = os.path.splitext(os.path.basename(file_name))[0]
        logger.debug(f"file name only - {file_name_only}")
        self.fixed_file = f"data/fixed_{file_name_only}.csv"

        if not os.path.exists(self.fixed_file):
            curr_f = f"data/corrupted_{file_name_only}.csv"
            self.fix_corrupted_file(file_name, self.fixed_file, curr_f)

        if not os.path.exists(f"pickles_can/{file_name_only}.pkz"):
            df = self.optimize_csv_file(self.fixed_file)
            self.dump_to_pickle(df, file_name_only)

        self.data = pd.read_pickle(f"pickles_can/{file_name_only}.pkz")
        self.set_indexes()

    def set_indexes(self):
        self.data_by_objs = self.data.groupby(["filename", "obj"]).size().sort_values(ascending=False)
        self.data_by_time = self.data.groupby(["filename", "obj"]).agg({'sample_time': ['min', 'max']})
        # df = self.data
        # df['x_index'] = df['x'] // (self.im_x // 10)
        # df['y_index'] = df['y'] // (self.im_y // 10)
        # self.data_by_blocks = df

    def set_general_index(self, df):
        logger.debug(f"entering set_index")

        df_by_obj = df.set_index(['filename', 'obj']).sort_index()

        return df_by_obj

    def dump_to_pickle(self, df, pickle_name):
        logger.debug(f"entering dump_to_pickle")

        self.data = f"pickles_can/{pickle_name}.pkz"
        df.to_pickle(f"pickles_can/{pickle_name}.pkz")

    def set_time_row(self, df):
        logger.debug(f"entering set_time_row")
        df['sample_time'] = df.start
        df['sample_time'] += pd.to_timedelta(df['delta_time'])
        df.drop('start', 1)
        df.drop('delta_time', 1)
        df.drop('path_time', 1)
        return df

    def get_routes_by_area(self, x1, y1, x2, y2):
        logger.debug(f"entering get_routes_by_area x1={x1},y1={y1},x2={x2},y2={y2}")
        df1 = self.data[(self.data.x.between(x1, x2)) & (self.data.y.between(y1, y2))]

        self.prev_data = df1
        return df1.groupby(["filename", "obj"]).size()

    def get_all_routes(self):
        logger.debug(f"entering get_routes_by_obj")

        return self.data_by_objs

    def get_square_routes(self, list_square,img_size):
        x_size = img_size[1] // self.SLICE_X
        y_size = img_size[0] // self.SLICE_Y
        multiple = True if len(list_square) > 2 else False
        df_copy1 = pd.DataFrame().reindex_like(self.data)
        res = pd.DataFrame().reindex_like(self.data)
        for index in range(len(list_square) // 2):
            top_left = (list_square[index] * x_size, (list_square[index+1]) * y_size)
            bottom_right = ((list_square[index ] + 1) * x_size, list_square[index+1] * y_size)
            df_copy1 = self.get_routes_by_area(top_left[0], bottom_right[1], bottom_right[0], top_left[1])
            if index > 2:
                res = res.append(df_copy1, ignore_index=True)
        if len(list_square) > 2:
            return res
        return df_copy1

    def get_routes_be_hour(self, hour_one, hour_two):
        logger.debug(f"entering get_routes_be_hour hour_one={hour_one},hour_two={hour_two}")

        start_time = pd.to_datetime(hour_one).time()
        end_time = pd.to_datetime(hour_two).time()

        min = self.data_by_time.sample_time['min'].dt.time  # objs[('sample_time','min')]
        max = self.data_by_time.sample_time['max'].dt.time  # objs[('sample_time','max')]

        items = self.data_by_time[(min.between(start_time, end_time)) | ((min < start_time) & (max > start_time))]
        self.prev_data = items
        return items

    def get_routes_be_date(self, date, hour_one, hour_two):
        logger.debug(f"entering get_routes_be_date date={date} hour_one={hour_one},hour_two={hour_two}")

        date = pd.to_datetime(date)  # "2017-08-17"

        start_time = date + pd.to_timedelta(hour_one)  # "07:01:09"
        end_time = date + pd.to_timedelta(hour_two)  # "08:11:09"

        min = self.data_by_time[('sample_time', 'min')]
        max = self.data_by_time[('sample_time', 'max')]

        items = self.data_by_time[
            (min.between(start_time, end_time)) | ((min.where(min < start_time) & (max.where(max > start_time))))]
        return items

    # def get_route_by_block(self,x_inds,y_inds):
    #     logger.debug(f"entering get_route_by_block x_indexes={x_inds} y_indexes={y_inds}")
    #
    #     return self.data_by_blocks[(self.data_by_blocks['x_index'].isin(x_inds)) & (self.data_by_blocks['y_index'].isin(y_inds))]
