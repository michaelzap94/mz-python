import re

# ?P<ANY_LABEL> -> GIVE names to groups

def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group()) # Mrs. Tilda Swinton
	print(matches.group('first')) # Tilda
	print(matches.group('last')) # Swinton

parse_name("Mrs. Tilda Swinton")
