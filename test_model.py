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

    def test_load_data(self):
         # df = self.m.optimize_csv_file(DEFUALT_DATA_FILE)
         # print(df)
         self.m.load_data(DEFUALT_DATA_FILE)
         self.m.set_indexes()
         r = self.m.get_routes_by_area(100, 150, 200, 250)
         self.assertEqual(len(r),278477)



    #     img = self.c.image
    #     self.assertEqual(img, DEFUALT_IMAGE_FILE)
    #

if __name__ == '__main__':
    unittest.main()

