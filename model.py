import sys
from settings import logger, FIXED_FILE_NAME, ERROR_FILE_NAME,DEFUALT_DATA_FILE


def fix_corrupted_file(file_name):
    logger.debug(f"entering fix_corrupted_file,file_name={file_name}")
    logger.error(file_name)
    valid_counter = 0
    invalid_counter = 0

    # for line in fileinput.input(file_name):
    with open(file_name, 'r') as datar, open(FIXED_FILE_NAME, "w", encoding="utf-8") as fixedw, open(
            ERROR_FILE_NAME,
            "w",
            encoding="utf-8") as errorw:
        for line in datar.readlines():
            if (len(line.split(', ')) == 14):
                fixedw.write(line.strip(" "))
                valid_counter += 1
            else:
                errorw.write(line.strip(" "))
                invalid_counter += 1

    logger.error(f"{valid_counter} valid lines.")
    logger.error(f"{invalid_counter} corrupted lines.")
    logger.error("See corrupt_data.csv")
