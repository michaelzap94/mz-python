from threading import Thread
import time
import random

counter = 0

def increment_counter():
	global counter
	time.sleep(random.randint(0, 2))
	counter += 1
	time.sleep(random.randint(0, 2))
	print(f'New counter value: {counter}')
	time.sleep(random.randint(0, 2))
	print('-----------')

for x in range(10):
	t = Thread(target=increment_counter)
	time.sleep(random.randint(0, 2))
	t.start()

# FUSSING-> RANDOM SLEEPS will MESS UP the code
# New counter value: 1
# New counter value: 2
# -----------
# New counter value: 4
# -----------
# New counter value: 6
# New counter value: 6
# New counter value: 6
# New counter value: 7
# New counter value: 8
# -----------
# -----------
# -----------
# -----------
# -----------
# -----------
# New counter value: 9
# -----------
# New counter value: 10
# -----------

# Therefore: BE VERY CAREFUL when Threads modify a shared STATE(counter)