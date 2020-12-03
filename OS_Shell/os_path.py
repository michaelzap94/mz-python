import os
# __file__ is the absolute path to the current file
print(__file__) # /Users/michael/Personal/mz-python/OS_Shell/os_path.py

# The basename function will return just the filename of a path
print(os.path.basename("this/is/some/path/filename_is_result.txt")) # filename_is_result.txt
print(os.path.basename(__file__)) # os_path.py

# The dirname will just return the path part
print(os.path.dirname("this/is/some/path/filename_is_result.txt")) # this/is/some/path
print(os.path.dirname(__file__)) # /Users/michael/Personal/mz-python/OS_Shell

# tell you if a path(Dir and/or File) exists or not
print(os.path.exists("this/is/some/path/filename_is_result.txt")) # False
# only checks if the path is a directory
print(os.path.isdir("this/is/some/path/filename_is_result.txt")) # False
# only checks if the path is a file
print(os.path.isfile("this/is/some/path/filename_is_result.txt")) # False

# Join one or more path(Dir or/and file) components together using the appropriate separator
print(os.path.join("this/is/some", "path/filename_is_result.txt")) # this/is/some/path/filename_is_result.txt
# Split a path into a tuple that contains the directory and the file
print(os.path.split("this/is/some/path/filename_is_result.txt")) # ("this/is/some/path", "filename_is_result.txt")