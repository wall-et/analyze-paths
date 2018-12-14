import sys
import matplotlib.pyplot as plt
from matplotlib import cm as CM
import matplotlib.image as mpimg
from settings import logger
import matplotlib.ticker as plticker
import numpy as np
from PIL import Image
import pandas as pd



class View:
    def __init__(self,conf):
        self.img = None
        self.image_name = None
        self.config = conf
        self.NUM_SLICE = int(self.config['num_of_blocks_in_image'])
        self.len_param = {'area': 4, 'hour': 2, 'date': 3 }
    def get_file(self):
        if sys.argv and len(sys.argv) > 1:
            return sys.argv[1]
        else:
            self.output("Insert File Name To Parse")
            inp = self.get_input()
        return inp
        # if inp else None
        # return (sys.argv[1] if sys.argv and len(sys.argv) > 1 else None)

    def get_image(self):
        if sys.argv and len(sys.argv) > 2:
            return sys.argv[2]
        else:
            self.output("Insert Image Name To Display")
            inp = self.get_input()
        return inp

    def set_image(self, image_name):
        self.image_name = image_name
        self.img = mpimg.imread(image_name)

    def display_image(self):
        # image = mpimg.imread(self.img)
        plt.axis("off")
        plt.imshow(self.img)
        plt.show()

    def plot_image_and_routes(self, data_obj):
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry("600x600+500+10")

        dataframe, df_obj = data_obj
        # df_obj = df_obj.head(35)
        # im = mpimg.imread(self.image_name)
        # plt.axis("off")

        l = len(df_obj)
        logger.debug(f"plotting {l} routes")
        # self.plot_one_by_one(dataframe, df_obj)
        lim = int(self.config['path_by_path_limit'])
        max_lim = int(self.config['start_draw_heatmap_limit'])
        if l < max_lim and l > lim:
            self.plot_all_routes(dataframe, df_obj)
        elif l <= lim:
            self.plot_one_by_one(dataframe, df_obj)
        else:
            self.plot_heatmap(dataframe, df_obj)
        # plt.pause(0.1)


    def draw_grid(self):
        logger.debug(f"enter draw grid ")
        img_d = mpimg.imread(self.image_name)
        fig = plt.figure(figsize=(7.5, 5))
        ax = fig.add_subplot(111)

        im_size = img_d.shape[:2]
        width = im_size[1]
        height = im_size[0]

        myInterval_w = width // int(self.config['num_of_blocks_in_image'])
        myInterval_h = height // int(self.config['num_of_blocks_in_image'])

        loc_w = plticker.MultipleLocator(base=myInterval_w)
        loc_h = plticker.MultipleLocator(base=myInterval_h)

        ax.xaxis.set_major_locator(loc_w)
        ax.yaxis.set_major_locator(loc_h)

        # Add the grid
        ax.grid(which='major', axis='both', linestyle='-', color="k")

        # Add the image
        ax.imshow(img_d)

        # Find number of gridsquares in x and y direction
        nx = abs(int(float(ax.get_xlim()[1] - ax.get_xlim()[0]) / float(myInterval_w)))
        ny = abs(int(float(ax.get_ylim()[1] - ax.get_ylim()[0]) / float(myInterval_h)))

        # Add some labels to the gridsquares
        for j in range(ny):
            y = myInterval_h / 2 + j * myInterval_h
            for i in range(nx):
                x = myInterval_w / 2. + float(i) * myInterval_w
                ax.text(x, y, '{:d}'.format(i + j * nx), color='k', ha='center', va='center')

        plt.pause(0.1)
        plt.gcf().clear()


    def plot_all_routes(self, dataframe, df_obj):
        im = mpimg.imread(self.image_name)

        plt.imshow(im)
        # self.draw_grid()
        for t in df_obj.index:
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y)
        plt.pause(0.1)
        plt.gcf().clear()

    def plot_one_by_one(self, dataframe, df_obj):
        im = mpimg.imread(self.image_name)
        if not self.config['auto_load_path_by_path']:
            self.output("Enter to next route")
        for t in df_obj.head(15).index:
            plt.imshow(im)
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y, c='r')
            # plt.plot(oo.x, oo.y,c=np.random.rand(3,1))
            plt.pause(0.5)
            plt.gcf().clear()
            if not self.config['auto_load_path_by_path']:
                self.get_input()
        self.plot_all_routes(dataframe, df_obj)


    def plot_heatmap(self, dataframe, df_obj):
        im = mpimg.imread(self.image_name)
        plt.imshow(im)
        count = pd.DataFrame({'count': dataframe.loc[df_obj.index].groupby(["x", "y"]).size()}).reset_index()
        mat_count = count.pivot('y', 'x', 'count').values
        plt.imshow(mat_count, cmap=plt.get_cmap("hsv"), interpolation='nearest')
        plt.colorbar()
        plt.pause(0.5)
        plt.gcf().clear()

    def output(self, msg):
        print(msg)

    def get_input(self):
        return input(">>")

    def get_filters(self, olf_f):
        self.output(f"Enter to keep filter. d to delete. insert new to edit")
        f = dict()
        self.output(f"FIlter By Area :x1,y1,x2,y2: current ({olf_f['area']})")
        area = self.get_input()
        if not area:
            f['area'] = olf_f['area']
        else:
            if area == "d":
                f['area'] = None
            else:
                try:
                    split_input = area.split(',')
                    if len(split_input) != self.len_param['area']:
                        raise ValueError("You give one or more bigger /smaller requires values")

                    x1, y1, x2, y2 = split_input
                    area = [int(x1), int(y1), int(x2), int(y2)]
                    f['area'] = area
                except ValueError as err:
                    print('error params:', err)
        self.output(f"FIlter By Hour :00:00:00,00:00:00: current ({olf_f['hour']})")
        hour = self.get_input()
        if not hour:
            f['hour'] = olf_f['hour']
        else:
            if hour == "d":
                f['hour'] = None
            else:
                try:
                    split_input = hour.split(',')
                    if len(split_input) != self.len_param['hour']:
                        raise ValueError("You give one or more bigger /smaller requires values")
                    t1, t2 = split_input
                    hour = [t1, t2]
                    f['hour'] = hour
                except ValueError as err:
                    print('error params:', err)
        self.output(f"FIlter By Date and Time :2017-08-17,00:00:00,00:00:00: current ({olf_f['date']})")
        date = self.get_input()
        if not date:
            f['date'] = olf_f['date']
        else:
            if date == "d":
                f['date'] = None
            else:
                try:
                    split_input = date.split(',')
                    if len(split_input) != self.len_param['date']:
                        raise ValueError("You give one or more bigger /smaller requires values")
                    d, t1, t2 = date.split(",")
                    date = [d, t1, t2]
                    f['date'] = date
                except ValueError as err:
                    print('error params:', err)
        self.output(f"FIlter By block X,Y :1,2,50: current ({olf_f['block']})")
        block_list = []
        block = self.get_input()
        if not block:
            f['block'] = olf_f['block']
        else:
            if block == "d":
                f['block'] = None
            else:
                block_list = block.split(",")
                block = []
                for obj in block_list:
                    block.append(int(obj.strip()))
                f['block'] = block_list
        return f

    def set_config(self,conf):
        for key,value in conf.items():
            new_set = None
            self.output(f"setting of {key}: {value}")
            new_set = self.get_input()
            if new_set:
                conf[key]=new_set
        return conf