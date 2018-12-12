import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class View:
    def __init__(image_name,self):
        image = mpimg.imread(image_name)
        plt.axis("off")
        plt.imshow(image)
        plt.show()