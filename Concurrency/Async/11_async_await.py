# THEY ARE USED TO AVOID WAITING TIMES
# SAME AS using 'yield' but EASIER to understand

# 'yield from' -> became 'await' 
# ->both will WAIT for WHOLE function TO FINISH, BUT, You can suspend it(make it wait for something) in the middle. eg: input

from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine # we have to say this is no longer a Generator but a Coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(friend_upper_coroutine):
    print('Starting...')
    await friend_upper_coroutine # WAIT for ENTIRE friend_upper_coroutine TO FINISH
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)