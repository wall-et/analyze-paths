
import sys

import model as m

DEFUALT_IMAGE_FILE = "data/fixed.csv"

file =  sys.argv[1] if sys.argv and len(sys.argv) > 1 else DEFUALT_IMAGE_FILE
m.fix_corrupted_file(file)

