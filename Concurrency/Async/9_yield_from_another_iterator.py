from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def get_friend():
    # yield from -> getting next value of something you can get a value from
    yield from friends 
    # SAME AS:
    # for x in friends: 
    #     yield x

def greet(friends_generator):
    while True:
        try:
            friend = next(friends_generator)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))