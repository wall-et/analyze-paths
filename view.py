
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from settings import logger

class View:
    def __init__(self):
        self.img = None
        self.image_name = None

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

    def plot_image_and_routes(self, data_obj, image_name=None):
        dataframe, df_obj = data_obj
        if image_name:
            self.image_name = mpimg.imread(image_name)
        # im = mpimg.imread(self.image_name)
        # plt.axis("off")

        l = len(df_obj)
        logger.debug(f"plotting {l} routes")
        # self.plot_one_by_one(dataframe, df_obj)
        if l < 5000 and l > 20:
            self.plot_all_routes(dataframe, df_obj)
        elif l <= 20:
            self.plot_one_by_one(dataframe, df_obj)
        else:
            self.plot_heatmap( dataframe, df_obj)
        # plt.pause(0.1)

    def plot_all_routes(self, dataframe, df_obj):
        im = mpimg.imread(self.image_name)
        plt.imshow(im)
        for t in df_obj.index:
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y)
        plt.show()
        plt.gcf().clear()

    def plot_one_by_one(self, dataframe, df_obj):
        im = mpimg.imread(self.image_name)
        for t in df_obj.head(15).index:
            plt.imshow(im)
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y,c='r')
            # plt.plot(oo.x, oo.y,c=np.random.rand(3,1))
            plt.pause(0.5)
            plt.gcf().clear()
        self.plot_all_routes(dataframe, df_obj)

    def plot_heatmap(self, dataframe, df_obj):
        self.plot_all_routes(dataframe, df_obj)
        pass

    def output(self, msg):
        print(msg)

    def get_input(self):
        return input(">>")
