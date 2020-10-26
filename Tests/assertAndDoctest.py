# Example 1
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1)) # 2
try:
    add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!
except AssertionError as e:
    print(e.__repr__())
# Example 2
def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
try:
    print(eat_junk(food)) # AssertionError: food must be a junk food!
except AssertionError as e:
    print(repr(e))

# Doctests ================================================================
# COMMANDS --> python -m doctest -v filename.py
def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100,200)
    300
    """
    return a + b

def double(values):
    """ double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]

# Doctests can only compare to single quoted strings
def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    return "hi"

# Watch out for whitespace!
# (There's a trailing space on line 42)
def true_that():
    """
    >>> true_that()
    True
    """
    return True

# Order of keys in dicts matters in doctests
def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key: True for key in keys}


