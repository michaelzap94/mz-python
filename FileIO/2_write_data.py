import os
current_dir = os.path.dirname(__file__)
FILEPATH = os.path.join(current_dir, "story_write.txt")

#with will execute ASYNC so be careful

# Write will always overwrite the existing file
with open(FILEPATH, "w") as file:
    file.write("first line\n")
    file.write("second line\n")

with open(FILEPATH, "a") as file:
    file.write("can only append to END\n")
    file.write("can only append to END\n")
    file.write("can only append to END\n")

with open(FILEPATH, "r+") as file:
    file.write("At the beginning but will OVERWRITE original")
