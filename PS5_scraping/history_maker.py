import os
from csv import writer, QUOTE_MINIMAL
from constants import RETAILERS

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'history.csv')

def make_history(results):
    headers = RETAILERS.keys()
    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, "a", newline='') as csv_file:
    # QUOTE_MINIMAL -> constant: don't wrap data in quoute unless we need it
    # quotechar -> A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. It defaults to '"'.
    # delimiter -> A one-character string used to separate fields. It defaults to ','
        csv_writer = writer(csv_file, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL) # gives the csv_writer with this file
        if not file_exists:
            csv_writer.writerow(headers) # row header
        csv_writer.writerow(results)