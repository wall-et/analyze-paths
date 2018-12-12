from view import View
from model import Model
import re
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
        self.v.plot_image_and_routes(self.m.data, self.m.get_all_routes().head(90))

    def run(self):
        self.initial_run()
        self.v.output("Displaying the first 100 rounds.\nFeel free to filter.(or call for help)")
        cmd = "init"
        while cmd != 'exit':
            cmd = self.v.get_input()
            if self.string_found("area", cmd) or self.string_found("f1", cmd):
                x1, y1, x2, y2 = cmd.split("|")[1].split(",")
                self.v.plot_image_and_routes(self.m.data, self.m.get_routes_by_area(int(x1), int(y1), int(x2), int(y2)))
            if self.string_found("hour", cmd) or self.string_found("f2", cmd):
                t1, t2 = cmd.split("|")[1].split(",")
                self.v.plot_image_and_routes(self.m.data, self.m.get_routes_be_hour(t1, t2))

    def string_found(self, string1, string2):
        if re.search(r"\b" + re.escape(string1) + r"\b", string2):
            return True
        return False
