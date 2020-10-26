
jabber = open("sample.txt",'r')
for line in jabber: #||for line in jabber.readlines():
    if "jabberwock" in line.lower():
        print(line, end='')
jabber.close()

print('======================================================')

# LIKE TRY WITH resources in java, it will automatically close the open method.
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print('======================================================')

with open("sample.txt", 'r') as jabber:
    line = jabber.readline() # reads a single line
    while line: # while there's a line to read
        print(line, end='')
        line = jabber.readline() # next line to read, last line will be empty

print('======================================================')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines() # return a list of all lines. // not efficient for large files though.
print(lines)
# lines has been defined in the previous with open. Remember: Python can define global variables on the go
for line in lines:
    print(line, end='')

print('======================================================')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
# lines[::-1] reverses the array 'lines'
for line in lines[::-1]:
    print(line, end='')

print('======================================================')

with open("sample.txt", 'r') as jabber:
    singleString = jabber.read() # reads the whole document, till end. OUTPUTS one string.
    print(singleString)

for line in singleString[::-1]: # reverses the singleString
    print(line, end='')
