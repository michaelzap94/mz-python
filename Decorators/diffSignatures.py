# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "lol"

print(greet("todd"))
print(order(side="burger", main="fries"))
print(lol())

#USING wraps TO PRESERVE METADATA=================================================

from functools import wraps
#preserves a function#s metadata when it is decorated --> """Adds two numbers together."""
# therefore the function being passed's metadata will not be lost,
# otherwise we will be logging the inner function 'wrapper' metadata. --> """I AM WRAPPER FUNCTION"""

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add(4,1))
print(add.__doc__)
print(add.__name__)
help(add)

# More examples of Args with a decorator =================================

from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")

greet('Tony') #hi there Tony
#greet(name="Tony") #ValueError("No kwargs allowed! sorry :(")
