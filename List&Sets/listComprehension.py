name = 'michael'
upperName = [char.upper() for char in name]
print('list: ', upperName ,'||| string: ', "".join(upperName))

print('list: ', [bool(val) for val in[0,[],'', 1]])

# IF:
numbers = list(range(1,7)) # [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if(num%2==0)]
odd= [num for num in numbers if(num%2!=0)]
print(evens)# [2, 4, 6]
print(odd)# [1, 3, 5]

with_vowels = 'This is so much fun!'
noVowelsList = [char for char in with_vowels if(char not in 'aeiou')]# ['T', 'h', 's', ' ', 's', ' ', 's', ' ', 'm', 'c', 'h', ' ', 'f', 'n', '!']
noVowelsListOrSpace = [char for char in with_vowels if(char not in 'aeiou ')]# ['T', 'h', 's', 's', 's', 'm', 'c', 'h', 'f', 'n', '!']
print(''.join(noVowelsList))# Ths s s mch fn!
print(''.join(noVowelsListOrSpace))# Thsssmchfn!

# IF/ELSE:

multiplyOddDivideEven = [num * 2 if(num%2!=0) else int(num/2) for num in numbers]
print(multiplyOddDivideEven) # [2, 1, 6, 2, 10, 3]

#  NESTED LIST COMPREHENSION
print("NESTED LIST COMPREHENSION"+"=" * 40)

nested_list = [list(range(1,4)), list(range(4,7)), list(range(7,10))]# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  loop through all elements
[[print(inner) for inner in outer] for outer in nested_list]
print("=" * 40)

xenraya = [["X" if(num % 2 ==0) else "O" for num in range(1,4)] for valNotUsed in range(1,4)]
print(xenraya)  # [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]
