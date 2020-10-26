# NO INDEXING, UNORDERED, IMMUTABLE
list_set = set([1,2,3,4])
print(list_set) # {1, 2, 3, 4}

even = set(range(0,40,2))
print('even',even) # even {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38}

squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print('squares',squares) # squares {4, 6, 9, 16, 25}
print('#'*44)
mset = {1,2,3,4,4}
print(mset)
# following 4 opperations will not modify sets.

#ORDER DOESN'T MATTER

#UNION -> gets unique items only. ALL ITEMS BUT ONLY INCLUDE UNIQUE ITEMS OR ----> even | sqares
print(even.union(squares))
#INTERSACTION -> RETURNS common elements OR ----> even & sqares
print(even.intersection(squares))

#ORDER MATTERS
print('#'*24)

#set1.DIFFERENCE(set2) !== set2.DIFFERENCE(set1) REMOVES THE COMMON ELEMENTS IN THE LEFT-HAND SIDE SET
print(even.difference(squares))
print('even', even)
print('squares', squares)
print(squares.difference(even))
print('even', even)
print('squares', squares)
#set1.SYMMETRIC_DIFFERENCE(set2) !== set2.SYMMETRIC_DIFFERENCE(set1) WILL ADD ALL ELEMENTS AND REMOVE THE INTERSECTION
print('#'*24)
print(even.symmetric_difference(squares))
print('even', even)
print('squares', squares)
print(squares.symmetric_difference(even))
print('even', even)
print('squares', squares)

# difference_update will UPDATE the left-hand side set.
print(even.difference_update(squares))#-> None
print('even', even)# WILL BE MODIFIED
print('squares', squares)

############## ADD/REMOVE/DISCARD ############
new_set = set()
new_set.add(4)
new_set.add(16)
new_set.discard(4)
new_set.discard(4)# will not throw any error.
new_set.remove(16)
try:
    new_set.remove(16) # will throw an error.
except Exception as error:
    print(error)


###SUBSET, SUPERSET
large = set(range(1,10))
small = set(range(1,5))
print(large.issuperset(small)) # True
print(small.issubset(large)) # True

##FROZENSET=> CANNOT CHANGE
even_const = frozenset(range(0,100,2))


######CHALLENGE#####
input = input("Enter some text: ")
vowels = frozenset('aeiou')
print(vowels)
output = set(input).difference(vowels) # remove vowels in the input
# for letter in input:
#     if(letter not in vowels):
#         output.add(letter)
print(sorted(output))

#SET COMPREHENSION
first = {'a','e','i','o','u'}
str = 'michael'

#find all vowels in your name
vowelsInName = {char for char in str if(char in first)}
print(type(vowelsInName), vowelsInName) # <class 'set'> {'e', 'i', 'a'}
