from random import random
import sys # to use command line arguments: sys.argv is a list. # python FunctionsColt.py 4 5 4 ----> ['FunctionsColt.py', '4', '5', '4']

def flip_coin():
    randomInt = int(random() * 10)
    if(randomInt > 5):
        return "heads"
    else:
        return "tails"

def iterate(num = 5): # default in case no argument is passed.
    for w in range(num):
        print(flip_coin())

#iterate(int(sys.argv[1]))

#function as parameters=============================================
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def math(a,b,fn=add):
    return fn(a,b)
print(math(2,2)) #4
print(math(4,2,subtract)) #2

#LOCAL SCOPE=================================================================
name = 'outside'
def func():
    name = 'now inside'
    print(name)

func()#inside
print(name)#outside,  THEREFORE: 'name' was not changed inside func() as it is a Local Variable. like: ''' var name = 'something' inside a function in JS. '''

#GLOBAL SCOPE==============
name2 = 'outside'
"""my comment, will NOT work"""
def func2():
    """my comment that WILL WORK"""

    global name2 # DECLARING THIS VARIABLE 'GLOBAL': is like refering to just ''' name inside a function in JS, WITHOUT let/var, therefore, referring to the global variable '''
    name2 = 'now inside'
    print(name2)

func2()
print(name2)

print(func2.__doc__)# my comment that WILL WORK

# nonlocal --> used ONLY in nested functions

realName = 'Michael'
def parentFunc():
    realName = 'parentFunc'
    def childFunc():
        nonlocal realName
        realName = 'childFunc'
        return realName
    return childFunc()

print(parentFunc()) # childFunc

# *ARGS -- THIS EXPECTS DIFFERENT ARGUMENTS, NOT A TUPLE OR A LIST. but args will become a tuple.
def sumTuples(first, *args):
    # first will be 4 AND args will be (5,6,7)
    sum = first
    for x in args:
        sum += x
    return sum
print(sumTuples(4,5,6,7)) # 22
print('trying tuples')
#print(sumTuples(4,(1,2))) # WILL NOT WORK AS IT HAS TO BE UNPACKED.
print(sumTuples(4,*(1,2))) # 7 # WILL WORK AS the tuple IS UNPACKED USING '*'
print(sumTuples(4,*[1,2])) # 7 # WILL WORK AS the LIST IS UNPACKED USING '*'

# **kwargs ----> THIS EXPECTS DIFFERENT ARGUMENTS with values. not a dictionary. but kwargs will become a dictionary.

def favColors(name, **kwargs):
    #print(name) # Michael
    #print(kwargs) # {'jacket': 'black', 'trousers': 'blue', 't_shirt': 'white'}
    print(f"{name}'s favourite color for jacket is: {kwargs['jacket']}")

favColors('Michael', jacket = 'black', trousers = 'blue', t_shirt = 'white') # Michael's favourite color for jacket is: black

###############WILL NOT WORK###########################
#favColors('Patty', {'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'}) # ERROR

#YOU WILL HAVE TO UNPACK IT USING '**'
favColors('Patty', **{'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'})#
#######################################################

# IF you want to pass a dict,
# you need to assign it to an argument so it works with kwargs
favColors('Patty', jacket = {'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'}) # Patty's favourite color for jacket is: {'jacket': 'orange', 'trousers': 'white', 't_shirt': 'black'}
# CALLING .items() on the dict WILL NOT WORK EITHER
a = {'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'}
#favColors('Patty', a.items()) # ERROR
# WE NEED DICT UNPACKING "**mdict" to pass dicts as an argument
favColors('Patty', **a) #Patty's favourite color for jacket is: orange

# THE FOLLOWING WILL NOT WORK AS 'colorJacket' is not a property of the object 'a'.

# a = {'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'}
# def favColors2(name, colorJacket, **kwargs):
# #     print(f"{name}'s favourite color for jacket is: {colorJacket}")
# #     print('REST:',kwargs)
# # favColors2('Patty', **a) # ERROR

# CHANGE IN FUNCTION favColors
a = {'jacket' : 'orange', 'trousers' : 'white', 't_shirt' : 'black'}
def favColors2(name, jacket, **kwargs):
    print(f"{name}'s favourite color for jacket is: {jacket}")
    print('REST:',kwargs) # REST: {'trousers': 'white', 't_shirt': 'black'}
favColors2('Patty', **a) # Patty's favourite color for jacket is: orange # REST: {'trousers': 'white', 't_shirt': 'black'}

# **a will become """" jacket='orange', trousers = 'white', t_shirt = black """ THEREFORE: jacket is orange in the parameters of the function.





#TUPLE UNPACKING "*mtuple" =================================================
def sumAllValues(*args): # THIS EXPECTS DIFFERENT ARGUMENTS, NOT A TUPLE OR A LIST
    total = 0
    for num in args:
        total += num
    print(total)

nums = list(range(1,7)) # can't be an argument of *args
nums_tuple = tuple(nums) # can't be an argument of *args
# USE * TO UNPACK LISTS OR TUPLES.
# unpacked_tuple = *nums_tuple # CAN'T ASSIGN IT TO A VARIABLE.
sumAllValues(*nums) # 21
sumAllValues(*nums_tuple) # 21