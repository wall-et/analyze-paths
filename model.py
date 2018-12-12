
import pickle
from settings import logger, FIXED_FILE_NAME, ERROR_FILE_NAME, FIXED_FILE_NAME_PICKLE
# from IPython.core.display import HTML
# css = open('style-table.css').read() + open('style-notebook.css').read()
# HTML('<style>{}</style>'.format(css))

import matplotlib.pyplot as plt
import pandas as pd
import os.path

class Model:
    def __init__(self):
        # self.df = self.load_data()
        self.pickle=None
        pass

    def fix_corrupted_file(self, file_name):
        logger.debug(f"entering fix_corrupted_file,file_name={file_name}")
        logger.error(file_name)
        valid_counter = 0
        invalid_counter = 0

        # for line in fileinput.input(file_name):
        with open(file_name, 'r') as datar, open(FIXED_FILE_NAME, "w") as fixedw, open(
                ERROR_FILE_NAME,
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
        logger.error(f"{invalid_counter} corrupted lines.")
        logger.error("See corrupt_data.csv")

    def optimize_csv_file(self):

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
        df = pd.read_csv(FIXED_FILE_NAME, names=cols, usecols=useful_cols, dtype=cols_types, parse_dates=['start'],
                          infer_datetime_format=True)

        remove duplica
        groupby x,y,obj,file,seq
        set index
        dump to pickle
        return df

    def load_data(self,file):
        if not os.path.exists(file):
            self.optimize_csv_file()
        self.pickle = pd.read_pickle(FIXED_FILE_NAME_PICKLE)



    def set_index(self,df):
        df_by_obj = df.set_index(['filename', 'obj']).sort_index()
        df_by_obj.head()
