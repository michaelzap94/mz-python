import time
from threading import Thread

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


print("=======================================================================")

# Multi Threads: Create 2 Threads, each responsible of running a "target" function
thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)
# Now we have 3 Threads: MAIN Thread + 2 Threads we just created above

start = time.time()

# .start() -> run the target function
thread1.start()
thread2.start()

# Now both Threads will run at the same time as the Main Thread,
# Therefore, we need to tell our Main Thread to wait for the new Threads to finish

# .join() -> make the Main thread wait for these Threads to finish
thread1.join()
thread2.join()

end = time.time()

print('TOTAL: Two thread time: ', end - start)

# Run this and see what happens!
