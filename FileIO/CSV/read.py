"""
3 ways to read: basic file open || reader || DictReader
"""
from csv import reader, DictReader
import os

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'read_data.csv')

# BASIC using normal file read==================
with open(FILENAME, 'r') as f:
    lines = f.readlines()
#skip headers
lines = [line.strip() for line in lines[1:]]
for line in lines:
    person_data = line.split(',')
    print(person_data)

print("=======================================")
# Using reader==================================
with open(FILENAME) as file:
    csv_reader = reader(file) # <class '_csv.reader'> -> Generator ['','']
    print(next(csv_reader)) #print headers ->  ['name', 'age', 'university']
    for row in csv_reader:
        print(row) #print remainder rows

# Using DictReader==================================
with open(FILENAME) as file:
    csv_dict_reader = DictReader(file) # <csv.DictReader object at 0x013032B0> -> Generator [{},{}]
    # NO HEADERS, since the fieldNames/Headers will be the keys in each object of the LIST of Dicts
    for row in csv_dict_reader:
        print(row) 
        #print rows : each row is an -> OrderedDict([('name', 'mike'),('age', 23)])
        # {'name': 'mike', 'age': '23', 'university': 'kings'}, 
        # {'name': 'henry', 'age': '32', 'university': 'warwick'}
