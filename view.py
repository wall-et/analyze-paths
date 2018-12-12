import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


class View:
    def __init__(self):
        self.img = None

    def get_file(self):
        if sys.argv and len(sys.argv) > 1:
            return sys.argv[1]
        else:
            inp = input("Insert File Name To Parse")
        return inp
        # if inp else None
        # return (sys.argv[1] if sys.argv and len(sys.argv) > 1 else None)

    def get_image(self):
        if sys.argv and len(sys.argv) > 2:
            return sys.argv[2]
        else:
            inp = input("Insert Image Name To Display")
        return inp

    def set_image(self,image_name):
        self.img = mpimg.imread(image_name)

    def display_image(self):
        # image = mpimg.imread(self.img)
        plt.axis("off")
        plt.imshow(self.img)
        plt.show()

    def plot_image_and_routes(self,dataframe, df_obj, image_name = None):
        if image_name:
            self.img = mpimg.imread(image_name)
        im = self.img
        # plt.axis("off")
        plt.imshow(im)
        for t in df_obj.index:
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y)
        plt.show()