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
        # df_obj = df_obj.head(15)
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
            self.plot_heatmap(dataframe, df_obj)
        # plt.pause(0.1)


    def draw_grid(self):
        image = mpimg.imread(self.image_name)
        plt.imshow(image)
        # self.draw_grid()
        # image = mpimg.imread(self.image_name)
        for i in range(50, 1000, 50):
            image[i:i + 2, :] = 0
            image[:, i:i + 2] = 0
        plt.imshow(image, alpha=0.5)
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
        self.output("Enter to next route")
        for t in df_obj.head(15).index:
            plt.imshow(im)
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y, c='r')
            # plt.plot(oo.x, oo.y,c=np.random.rand(3,1))
            plt.pause(0.5)
            plt.gcf().clear()
            self.get_input()
        self.plot_all_routes(dataframe, df_obj)

    def plot_heatmap(self, dataframe, df_obj):
        self.plot_all_routes(dataframe, df_obj.head(100))
        pass

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
                x1, y1, x2, y2 = area.split(',')
                area = [int(x1), int(y1), int(x2), int(y2)]
                f['area'] = area
        self.output(f"FIlter By Hour :00:00:00,00:00:00: current ({olf_f['hour']})")
        hour = self.get_input()
        if not hour:
            f['hour'] = olf_f['hour']
        else:
            if hour == "d":
                f['hour'] = None
            else:
                t1, t2 = hour.split(",")
                hour = [t1, t2]
                f['hour'] = hour
        self.output(f"FIlter By Date and Time :2017-08-17,00:00:00,00:00:00: current ({olf_f['date']})")
        date = self.get_input()
        if not date:
            f['date'] = olf_f['date']
        else:
            if date == "d":
                f['date'] = None
            else:
                d, t1, t2 = date.split(",")
                date = [d, t1, t2]
                f['date'] = date
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
