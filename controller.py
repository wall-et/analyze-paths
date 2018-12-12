import sys
import model as m
from view import View
from model import Model
from settings import DEFUALT_IMAGE_FILE, DEFUALT_DATA_FILE


class Controller:
    def __init__(self):
        self.m = Model()
        self.v = View(DEFUALT_IMAGE_FILE)
        self.file = self.get_file()
        self.fix_data()


    def get_file(self):
        return (sys.argv[1] if sys.argv and len(sys.argv) > 1 else DEFUALT_DATA_FILE)

    def fix_data(self):
        self.m.fix_corrupted_file(self.file)


c = Controller()
