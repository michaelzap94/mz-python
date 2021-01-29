import random
import time

from threading import Thread

class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Initialize the thread"""
        Thread.__init__(self)
        self.name = name
    # python will call this method, when you call .start() on a thread
    def run(self):
        """Run the thread"""
        amount = random.randint(1, 3)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)

def create_threads():
    """
    Create a group of threads
    """
    for i in range(5):
        name = "Thread #%s" % (i+1)
        my_thread = MyThread(name)
        my_thread.start()

if __name__ == "__main__":
    create_threads()