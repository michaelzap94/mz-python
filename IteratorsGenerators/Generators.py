# INFINITE GENERATOR
# Lame function that returns a list of beats.
# Only runs 100 times
def current_beat():
    max = 100
    nums = (1,2,3,4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

# Infinite Generator - returns one beat a time, no list used!
def current_beat_using_Generator():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1


print(current_beat()) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

gen = current_beat_using_Generator()
print(gen) # <generator object current_beat_using_Generator at 0x037AEE30>
print(next(gen))# 1
print(next(gen))# 2

# for x in current_beat_using_Generator():
#     print(x) # will loop for ever

# ANOTHER EXAMPLE FIB

# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(10):
    print(n, end='')
#============================================================================================
# Generator expressions - like list comprehension
print('='*40)
#LONG ============
def nums():
    for num in range(1, 10):
        yield num
long = nums()
print(long) # <generator object nums at 0x0105EEF0>
print(next(long)) #1
# SHORT Generator expressions ============
short = (num for num in range(1,10))
print(short) # <generator object <genexpr> at 0x0105EEB0>
print(next(short)) #1

# vs list comprehension

short_list = [num for num in range(1,10)]
print(short_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#SPEED TEST ===============================================================================
import time
# SUMMING 10,000,000 Digits With Generator Expression  --->>>>>> TAKES LESS TIME because it executes the operation directly one element at a time
gen_start_time = time.time() # save start time
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time # end time - start time


# SUMMING 10,000,000 Digits With List Comprehension --->>>>>> TAKES MORE TIME because it first MAKES the list then executes the operation one element at a time
list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")


