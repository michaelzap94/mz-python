def countdown(n):
    while n > 0:
        yield n
        n = n - 1

g1 = countdown(3)
g2 = countdown(6)
print(next(g1)) # 3
print(next(g2)) # 6
print(next(g1)) # 2
print(next(g2)) # 5
print(next(g1)) # 1
print(next(g2)) # 4

# Python can only execute 1 task or thread at a time per process
# HERE: You are executing 2 different tasks, if you execute them fast enough it looks as if they were Async
# IN FACT -> Python Async is built around this concept of Generators
# Generators are faster than Threads
#============================================================================================================
# example of using MULTITASKING without using more than one Thread
tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    # pop first generator
    task = tasks[0]
    tasks.remove(task)
    try:
        # task will be a generator so run next() on it
        x = next(task)
        print(x)

        # append same generator to the back of the list
        tasks.append(task)
    except StopIteration:
        print('Task finished')

# If a task does not YIELD or takes too LONG between one yield and another 
# -> you could offload the work to a separate Thread or Process using ThreadPool or ProcessPool
