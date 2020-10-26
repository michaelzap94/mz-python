# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
    iterator = iter(iterable) # convert iterable into an iterator
    while True: # execute till False OR break
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)

print('='*67)
# ==============================================================================

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    #return Counter object
    def __iter__(self):
        return self

    #we have to add this so it BECOMES an Iterator. Otherwise, it will not be an iterator.
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

# for will call iter(Counter(50, 70)) and then next on it. Next will use self.current set to 50 in the __init__ and self.high set to 70 in the __init__
for x in Counter(50,70):
    print(x)
