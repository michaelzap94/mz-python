import logging
import os

current_dir = os.path.dirname(__file__)
FILEPATH = os.path.join(current_dir, "sample.log")

# add filemode="w" to overwrite
logging.basicConfig(filename=FILEPATH, level=logging.INFO)

# get logger to log exceptions
# logger = logging.getLogger(__name__)
logger = logging.getLogger("ex")

# since the min level is INFO, this will not show in the text file
logging.debug("This is a debug message")

# logs that will show in the file:
logging.info("Informational message")
logging.warning("Warning message")
logging.error("An error has happened!")
try:
    raise RuntimeError
except RuntimeError:
    logger.exception("Error!")

# read file
with open(FILEPATH) as file_handler:
    for line in file_handler:
        print(line)