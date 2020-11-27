import logging

#will not log this to the file
logger = logging.getLogger(__name__)

def add(x, y):
    """"""
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y