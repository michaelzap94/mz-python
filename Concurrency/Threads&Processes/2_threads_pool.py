import time
from concurrent.futures import ThreadPoolExecutor

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
    print('Started calculating...')
    cc_start = time.time()
    [x**2 for x in range(20000000)]
    cc_end = time.time()
    print('complex_calculation: ', cc_end - cc_start)

# SINGLE THREAD - With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
end = time.time()
print('TOTAL: Single thread time: ', end - start, '\n\n')

# TWO THREADS "max_workers = 2" - With two threads, we can do them both at once...
start = time.time()

# ThreadPoolExecutor allows you to create a bunch of Threads with NO target (Pool) so we can use the Pool to execute jobs(Functions)

# IOW-> have a bunch of Threads(max_workers) waiting AND ask them to do something ^ get result back multiple times
# without having to be always creating new Threads. 
# This way you don't have to create Threads for every single function all the time.

# USE "with" so we don't have to call pool.shutdown()
with ThreadPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(ask_user)
    #pool.submit(FUNCTION_3)
    #pool.submit(FUNCTION_4)

print('Two thread total time: ', time.time() - start)

# Run this and see what happens!