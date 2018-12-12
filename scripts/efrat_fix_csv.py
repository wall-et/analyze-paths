import time
import logging
import fileinput
import sys
import pandas as pd
import pickle

logger = logging.getLogger(__name__)
FIXED_FILE_NAME = "data/fixed.csv"
FIXED_FILE_NAME_PICKLE = "data/paths.pkl.xz"

ERROR_FILE_NAME = "data/corrupt_data.csv"
DEFUALT_DATA_FILE = "data/oddetect.csv"
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
#     filename='mylog.log')

before_time = time.time()


def fix_corrupted_file(file_name):
    logger.debug(f"entering fix_corrupted_file,file_name={file_name}")
    logger.error(file_name)
    valid_counter = 0
    invalid_counter = 0

    # for line in fileinput.input(file_name):
    with open(file_name, 'r') as datar, open(FIXED_FILE_NAME_PICKLE, "wb") as fixedw, open(
            ERROR_FILE_NAME,
            "w",
            encoding="utf-8") as errorw:
        for line in datar.readlines():
            if (len(line.split(", ")) == 14):
                pickle.dump(line.strip(" "),fixedw)
                # fixedw.write(line.strip(" "))
                valid_counter += 1
            else:
                errorw.write(line.strip(" "))
                invalid_counter += 1

    logger.error(f"{valid_counter} valid lines.")
    logger.error(f"{invalid_counter} corrupted lines.")
    logger.error("See corrupt_data.csv")


file =  sys.argv[1] if sys.argv and len(sys.argv) > 1 else DEFUALT_DATA_FILE
fix_corrupted_file(file)

print(time.time() - before_time)
