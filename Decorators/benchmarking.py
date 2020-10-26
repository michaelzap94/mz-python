# Let's define a speed_test decorator
from functools import wraps # import this so fn.__name__ is the name of the function we are executing, instead of wrapper
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs) # run the function
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(9000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(9000000)])


print(sum_nums_gen())
print(sum_nums_list())

