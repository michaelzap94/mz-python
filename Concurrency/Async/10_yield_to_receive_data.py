# SIMPLE
def greet():
    # SUSPEND THE FUNCTION, BUT assign the value we receive to a variable ('friend')
    friend = yield
    print(f'Hello, {friend}')

try:
    g = greet()
    g.send(None) # Priming the generator:  runs up to yield and then do:
    g.send('Adam') # This is what goes into the 'yield' of the generator
except StopIteration:
    pass

# ADVANCED
from collections import deque
friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper() # get a friend from deque
        # SUSPEND THE FUNCTION, BUT assign the value we receive to a variable ('greeting')
        greeting = yield
        print(f'{greeting} {friend}')

def greet(friend_upper_generator):
    yield from friend_upper_generator
    # SAME AS:

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')