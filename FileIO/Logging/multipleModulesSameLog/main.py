import logging
import os
import first
import second

current_dir = os.path.dirname(__file__)
FILEPATH = os.path.join(current_dir, "sample.log")

filename = os.path.basename("main")
logger = logging.getLogger(filename)

def main():
    """
    The main entry point of the application
    """
    #get logger
    logger.setLevel(logging.INFO)
    # create the logging file handler and formatter
    fh = logging.FileHandler(FILEPATH)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    first.add(7, 8)
    second.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()