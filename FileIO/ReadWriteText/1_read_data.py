import os
current_dir = os.path.dirname(__file__)
FILEPATH = os.path.join(current_dir, "story.txt")

# open a connection to file -> this will have to be closed
file = open(FILEPATH) # it will be read by default, 
print(file.read())
file.seek(0) # resets the cursor to point to the first character
print(file.read())
file.seek(0)
print(file.readlines()) # -> ['first line\n', 'second line\n', 'third line']
file.close()
file.closed # -> True

#------------------------------------------------------------------------

with open(FILEPATH) as file:
    data = file.readlines()

print(data) # -> ['first line\n', 'second line\n', 'third line']