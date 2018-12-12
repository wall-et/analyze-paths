import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from controller import Controller as cont


class View:
    def __init__(self):
        pass

    def get_file(self):
        return (sys.argv[1] if sys.argv and len(sys.argv) > 1 else None)

    def get_image(self):
        return (sys.argv[2] if sys.argv and len(sys.argv) > 1 else None)

    def display_image(self,image_name):
        image = mpimg.imread(image_name)
        plt.axis("off")
        plt.imshow(image)
        plt.show()
