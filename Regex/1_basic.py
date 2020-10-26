import re

# create regex
pattern = re.compile(r'(cat)')

res = re.search(pattern, "A cat is white cat")
print(res) # <re.Match object; span=(2, 5), match='cat'>
print(res.group(0)) # cat ->res.group(0) === res.group() it will return the matching object of the general match
print(res.group(1)) # cat ->res.group(0) === res.group() it will return the matching object of the general match
