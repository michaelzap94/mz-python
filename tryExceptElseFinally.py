def first():
    raise NameError('A custom message')
# first()
#=========================
# THE BASIC SYNTAX:
try:
    foobar
except:
    print("PROBLEM!")
else:
    print('if no errors')
finally:
    print('Always, regardless of errors')
print("after the try, will execute if we are handling all/specific excepts. OR no errors")

#THIS IS HOW get() IS IMPLEMENTED
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name": "Ricky"}
print(get(d, "city")) # None, instead of crashing.

#======================================
# as E: where E is the message of the error. e.__class__ will give you the class name of the error

while True:
    try:
        num = int(input("please enter a number: "))
    except Exception as e:
        print(f'message of error is: {e} and type of error is {e.__class__}')
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print('='*40, "REST OF GAME LOGIC RUNS!", '='*40)

#======================================

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err) # MESSAGE OF THE ERROR
# 	else:
# 		print(f"{a} divided by {b} is {result}")

#combine errors in a single line, but we'll have to be more generic.

def divide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong when dividing!", end='')
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")



# print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))


#======================================
class customError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

def firstCustomError():
    raise customError('my message')

#firstCustomError()

#Debugging with PDB, python debugger====================================
# ===================
# NOTES  NOTES  NOTES
# ===================
import pdb
# pdb.set_trace()

# Also commonly on one line:
#import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)import pdb, CONTINUE IWHT THE REST OF THE CODE.
# q (quit)

#First Example:
first = "First"
second = "Second"
#pdb.set_trace()# it WILL PAUSE execution., SHOW YOU THE NEXT LINE OF CODE, AND YOU CAN EXPLORE THE VALUES.
result = first + second
third = "Third"
result += third
print(result)


# Be careful with variable names! --> c or l are commands in the pdb, so if you want to print a parameter c or l, use p c OR p l
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d
add_numbers(1,2,3,4)


