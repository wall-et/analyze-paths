
from view import View
from model import Model
from settings import DEFUALT_IMAGE_FILE, DEFUALT_DATA_FILE


class Controller:
    def __init__(self):
        self.m = Model()
        self.v = View()
        self.file = self.v.get_file()
        self.file = self.file if self.file else DEFUALT_DATA_FILE
        self.image = self.v.get_image()
        self.image = self.image if self.image else DEFUALT_IMAGE_FILE
        # self.fix_data()
        # self.initial_run()


    def fix_data(self):
        self.m.fix_corrupted_file(self.file)
        self.m.load_data(self.file)

    def initial_run(self):
        self.v.set_image(self.image)
        self.m.load_data(self.file)
        self.v.plot_image_and_routes(self.m.data,self.m.get_all_routes().head(100))

    def run(self):
        self.initial_run()
        self.v.output("Displaying the first 100 rounds.\nFeel free to filter.(or call for help)")
        cmd = "init"
        while cmd != 'exit':
            cmd = self.v.get_input()


        # self.v.display_image(self.image)

