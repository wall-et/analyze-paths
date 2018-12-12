
import sys
import model as m
import view as v
from settings import DEFUALT_IMAGE_FILE,DEFUALT_DATA_FILE

class Controller:
    def __init__(self):
        self.file = get_file()
    file =  sys.argv[1] if sys.argv and len(sys.argv) > 1 else DEFUALT_IMAGE_FILE
    m.fix_corrupted_file(file)


<<<<<<< HEAD
def get_file():
    pass
=======
>>>>>>> 0f8f31b2f9671f5246b1976c4080413b908ee7fd
