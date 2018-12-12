
from view import View
from model import Model
from settings import DEFUALT_IMAGE_FILE, DEFUALT_DATA_FILE


class Controller:
    def __init__(self):
        self.m = Model()
        self.v = View()
        self.file = self.v.get_file() if self.v.get_file() else DEFUALT_DATA_FILE
        self.image = self.v.get_image() if self.v.get_image() else DEFUALT_IMAGE_FILE
        self.fix_data()
        self.v.display_image(self.image)


    def fix_data(self):
        self.m.fix_corrupted_file(self.file)


c = Controller()
