from view import View
from settings import DEFUALT_IMAGE_FILE, DEFUALT_DATA_FILE
import unittest
from model import Model

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        config = dict({'hard_reload_data_files': False,
                            'auto_load_path_by_path': False,
                            'num_of_blocks_in_image': 10,
                            'path_by_path_limit': 20,
                            'start_draw_heatmap_limit': 3000})
        self.m = Model(config)

    def test_filters(self):
         self.m.load_data(DEFUALT_DATA_FILE)
         self.m.set_indexes()

         r = self.m.get_routes_by_area(100, 150, 200, 250)
         self.assertEqual(len(r), 278477)

         self.m.set_indexes()
         h = self.m.get_routes_by_hour("07:01:09", "08:11:09")
         self.assertEqual(len(h), 772)

         d = self.m.get_routes_be_date("2017-08-17", "07:01:09", "08:01:09")
         self.assertEqual(len(d), 33)

         d1 = self.m.get_routes_be_date("2017-08-17", "01:01:09", "04:07:45")
         self.assertEqual(len(d1), 1107)
         

if __name__ == '__main__':
    unittest.main()

