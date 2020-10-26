# IF you want to execute operations sequentially -> don't use Threads, specially if modifying a Shared State
# IF you want to execute operations sequentially and use Threads -> Queuing system

import time, random, queue
from threading import Thread

counter = 0
# 2 Queues
job_queue = queue.Queue() # Things to be printed out
counter_queue = queue.Queue() # amounts by which to increase the counter

def increment_manager():
	global counter
	while True:
        # Wait till item available and don't allow other Threads to run this
		increment = counter_queue.get()  # this waits until an item is available and locks the queue

		time.sleep(random.random())
		old_counter = counter
		time.sleep(random.random())
		counter = old_counter + increment # Increased counter
		time.sleep(random.random())
        # Add something to print to the job_queue
		job_queue.put((f'New counter value {counter}', '------------'))
		time.sleep(random.random())

		counter_queue.task_done()  # this unlocks the queue

def printer_manager():
	while True:
        # Wait till item available and don't allow other Threads to run this
		for line in job_queue.get(): # this waits until an item is available and locks the queue
			time.sleep(random.random())
			print(line)

        # this unlocks the queue
		job_queue.task_done()

# printer_manager and increment_manager run continuously because of the `daemon` flag.
# daemon=True -> RUN forever along with Main Thread till some error
Thread(target=increment_manager, daemon=True).start()
Thread(target=printer_manager, daemon=True).start()

def increment_counter():
	counter_queue.put(1) 
	time.sleep(random.random())

# Create 10 Threads-------------------------------------------------------
worker_threads = [Thread(target=increment_counter) for thread in range(10)]
# Start 10 Threads
for thread in worker_threads:
	time.sleep(random.random())
	thread.start()

# Now all Threads will run at the same time as the Main Thread,
# Therefore, we need to tell our Main Thread to wait for the new Threads to finish
# .join() -> make the Main thread wait for these Threads to finish
for thread in worker_threads:
	thread.join()
# -------------------------------------------------------------------------
counter_queue.join()  # wait for counter_queue to be empty to finish
job_queue.join()  # wait for job_queue to be empty to finish