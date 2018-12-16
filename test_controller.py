from settings import DEFUALT_IMAGE_FILE
import unittest
from controller import Controller

class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.c = Controller()

    def test_initial_run(self):
        self.c.initial_run()

        img = self.c.image
        self.assertEqual(img, DEFUALT_IMAGE_FILE)


if __name__ == '__main__':
    unittest.main()
