import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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

    def set_image(self,image_name):
        self.image_name = image_name
        self.img = mpimg.imread(image_name)

    def display_image(self):
        # image = mpimg.imread(self.img)
        plt.axis("off")
        plt.imshow(self.img)
        plt.show()

    def plot_image_and_routes(self,dataframe, df_obj, image_name = None):
        if image_name:
            self.image_name = mpimg.imread(image_name)
        im = mpimg.imread(self.image_name)
        # plt.axis("off")
        plt.imshow(im)
        for t in df_obj.index:
            oo = dataframe.loc[t]
            plt.plot(oo.x, oo.y)
        plt.show()
        # plt.pause(0.1)

    def output(self,msg):
        print(msg)

    def get_input(self):
        return input(">>")