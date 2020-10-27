from csv import writer, DictWriter, QUOTE_MINIMAL 
import os

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'write_data.csv')
FILENAME_DICT = os.path.join(current_dir, 'write_data_DICT.csv')

#NORMAL using writer and lists-------------------------------------------------
# newline='' -> Always add a new line when append
with open(FILENAME, "w", newline='') as csv_file:
    # QUOTE_MINIMAL -> constant: don't wrap data in quoute unless we need it
    # quotechar -> A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. It defaults to '"'.
    # delimiter -> A one-character string used to separate fields. It defaults to ','
    csv_writer = writer(csv_file, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL) # gives the csv_writer with this file
    csv_writer.writerow(["name","age"]) # row header
    for data in [{'name': "mike", 'age': 23}, {'name': "henry", 'age':31}]:
        csv_writer.writerow([data['name'], data['age']])

#ADVANCED using DictWriter and Dicts----------------------------------------------
with open(FILENAME_DICT, 'w', newline='') as csv_file:
    field_names_headers = ['name', 'age']
    csv_dict_writer = DictWriter(csv_file, fieldnames=field_names_headers)
    csv_dict_writer.writeheader() # First create the headers
    for dataInDict in [{'name': "mike", 'age': 23}, {'name': "henry", 'age':31}]:
        csv_dict_writer.writerow(dataInDict)
