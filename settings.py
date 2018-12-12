import logging

logging.basicConfig(
    # filename='log.log',
    # filemode='a',
    level=logging.DEBUG,
    # format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
)
logger = logging.getLogger(__name__)


DATA_PATH = "data/"
FIXED_FILE_NAME = f"{DATA_PATH}fixed.csv"
ERROR_FILE_NAME = f"{DATA_PATH}corrupt_data.csv"
DEFUALT_DATA_FILE = f"{DATA_PATH}oddetect.csv"
DEFUALT_IMAGE_FILE = f"{DATA_PATH}paths0.png"
FIXED_FILE_NAME_PICKLE = f"{DATA_PATH}paths.pkl.xz"