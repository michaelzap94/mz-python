import logging

logger = logging.getLogger("main.second")

def add(x, y):
    """"""
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y