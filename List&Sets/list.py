list1 = [1, 2, 3]
list2 = list([1, 2, 3])

print(list1 == list2)
# ITERATOR==========================

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
iterator = iter(items)

for e in range(len(items) + 1):
    try:
        print(next(iterator))
    except:
        print('Stopped iteration')
# RANGES===========================
decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

print(my_range == range(3, 40, 3))  # True

print(range(0, 5, 2) == range(0, 6, 2))  # True, not identical but output/have the same values
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

# sevens = range(7, 1000000,7)
# x = int(input("Pleae enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
# else:
#     print("{} is not divisible by seven".format(x))

# Ranges Challenge
o = range(0, 100, 4)
print(o)  # -> range(0,100,4) or multiples of 4
print(list(o))  # -> [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]

p = o[::5]
print(p)  # -> range(0,100,20) something like saying range(0,100,5*4) or multiples of both 5 and 4
print(list(p))  # ->[0, 20, 40, 60, 80]
# Tuples
x = [2, 4]
print(x)
f, z = x
print(f)
print(z)
# COLT==================================================================================
print(list(range(1, 10)[::-1]))  # REARRANGE, SAME AS REVERSE.
# append, extend ======================
first = [1, 2, 3]
second = [4, 5, 6]
first.append(second)  # --> None
print(first)  # ADDED TO THE FIRST LIST #--> [1,2,3,[4,5,6]]
first = [1, 2, 3]
second = [4, 5, 6, 7, 8, 9]
first.extend(second)  # --> None
print(first)  # ADDED TO THE FIRST LIST #--> [1,2,3,4,5,6,7,8,9]
# insert==============
first.insert(2, 'hello')
print(first)  # ADDED as the 2nd index position: [1, 2, 'hello', 3, 4, 5, 6]
print(first[-1])  # -> last value 6
first.insert(-1, 'loca')
print(first)  # ADDED BEFORE the last index position. PENULTIMO: [1, 2, 'hello', 3, 4, 5, 'loca', 6]
first.insert(len(first), 'last')
print(first)  # ADDED AS THE LAST ITEM: [1, 2, 'hello', 3, 4, 5, 'loca', 6, 'last']
# clear========
first.clear()
print(first)  # emptied the list
# pop======== //PROVIDE AN INDEX -> RETURN REMOVED VALUE
returnedPop = second.pop(1)  # if no index, remove the last item
print(returnedPop)  # --> 5
print(second)  # [4, 6, 7, 8, 9]
# remove======= //PROVIDE A VALUE -> DOES NOT RETURN ANYTHING
second.remove(4)
print(second)  # [6, 7, 8, 9]
# index(value, index at which start searching,
# index up to which end searching)====== // find position of a given item in the list
print(second.index(6))  # 0 index
# print(second.index(10))#error
print(second.index(8, 1, 3))  # 2 index
# count - counts number of occurrences
print(second.count(8))  # 1 occurrence
# reverse - reverses the order of the list. UPDATES the existing list. Nothing is returned.
second.reverse()
print(second)
# sort - sorts things in ASC order. IN PLACE - Nothing is returned.
second.sort()  # [9, 8, 7, 6]
print(second)  # [6, 7, 8, 9]
# join - turns a list in a String
# joinedStr = '||'.join(second) # ERROR AS the list contains INTEGERS.
joinedStr = '||'.join(["my", "name", "is", 'Homit'])
print(joinedStr)  # -> 'my||name||is||Homit'
# SLICING - Creates a new copy of the list.
print("SLICING" + "=" * 40)

NewListDiffObj = second[::-1]  # Reverses the list - does not affect original list
print(NewListDiffObj)  # -> [9, 8, 7, 6]
print(second[-2:])  # slice [6, 7, 8, 9] FROM 8(-2) to the END. --> [8,9]
print(second[:-1])  # slice [6, 7, 8, 9] FROM the Beginning to the END 9(-1), not including it --> [6,7,8]
print(second[1:-1])  # slice [6, 7, 8, 9] FROM index 1 to the END 9(-1), not including it -->  [7,8]
print(second[-2:1])  # slice [6, 7, 8, 9] not possible so []

# slice [6, 7, 8, 9] FROM index -2(which is 8) upto(but not including) index 1 (which is 7),
# in reverse order because of -1 step --> [8]
print(second[-2:1:-1])


# slicing negative STEPS-> if Negative. reverse the order. GO BACKWARDS
# If we don't pass a START or and END --> [START would be at the end point:END would be at the beginning:-STEP]
slicinglist = [1, 2, 3, 4, 5, 6]
print("slicing negative step" + "=" * 40)
print(slicinglist[1::-1])  # 6,5,4,3,2
print(slicinglist[2::-1])
print(slicinglist[:1:-1])
print(slicinglist[4:1:-1])
print("=" * 40)

# Modify Portions, SLICE/REMOVE numbers[x:y] AND INSERT new list starting at the same index.
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers)  # [1,'a','b','c',4,5] REMOVED 2 and 3 & INSERTED a,b, c
# =====================
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = ['a', 'b', 'c']
print(numbers)  # [1, 'a', 'b', 'c', 5] REMOVED 2, 3, 4 & INSERTED a,b, c

# SWAP VALUES - IF YOU NEED TO DO SOMETHING IN PLACE(No new list)
names = ['Michael', 'Zapata']
names[0], names[1] = names[1], names[0]
print(names)  # ['Zapata', 'Michael']
