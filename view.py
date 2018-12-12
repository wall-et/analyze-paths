import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class View:
    def __init__(self):
        pass

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
