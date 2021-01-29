from multiprocessing import Process
import time

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


####### SINGLE PROCESS
# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('TOTAL Single process time: ', time.time() - start, '\n\n')

print("============================================")
####### TWO PROCESSES
# EACH will execute the WHOLE file from the beginning
# Create a new Process that will execute a "target" function

#process1 = Process(target=ask_user) - It won't work, because both will access console simultaneously BUT they are different entities
process1 = Process(target=complex_calculation) 
process2 = Process(target=complex_calculation)

# NOW we have 3 processes -> the MAIN process + 2 processes created above

if __name__ == '__main__':
        
    # start process
    process1.start()
    process2.start()

    start = time.time()

    # Wait for the process to finish running
    process1.join()
    process2.join()

    print('TOTAL Two process time: ', time.time() - start)

    # Use Multi Processing when you need to run multiple things at the same time in the CPU but you are not waiting for something else
    # If you are waiting for something else, USE Multi Threading
