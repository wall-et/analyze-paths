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

    def display_image(self,image_name):
        image = mpimg.imread(image_name)
        plt.axis("off")
        plt.imshow(image)
        plt.show()

    def plotfilter(dataframe, df_obj, img_name):
        im = Image.open(img_name)
        plt.imshow(im)
        for t in dataframe.index:
            oo = df_obj.loc[t]
            plt.plot(oo.x, oo.y, alpha=0.7)
        plt.show()