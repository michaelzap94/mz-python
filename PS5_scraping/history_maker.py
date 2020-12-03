import os
from csv import DictWriter

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'history.csv')

def make_history(result):
    print(result)
    pass