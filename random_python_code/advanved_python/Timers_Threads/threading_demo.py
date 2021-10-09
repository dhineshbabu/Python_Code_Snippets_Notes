# Thread basics
# Move a function to multiple threads
# Wait for all threads to complete

# Imports
import logging
from threading import Thread
import time
import random


def long_task(name):
    # Function to perform work
    max = random.randrange(1, 10)
    logging.info(f'Task: {name} performing {str(max)} times')
    for x in range(max):
        logging.info(f'Task {name}: {x}')
        time.sleep((random.randrange(1, 3)))
    logging.info(f'Task: {name}: complete')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    #  Do something here with single thread: Main
    # long_task('main')

    #  Now running it on a multiple threads
    threads = []
    for x in range(10):
        t = Thread(target=long_task, args=['thread '+ str(x)])
        threads.append(t)
        t.start()

    #  Wait for all the threads to finish
    for t in threads:
        t.join()
    logging.info('Finished all threads')


if __name__ == "__main__":
    main()


