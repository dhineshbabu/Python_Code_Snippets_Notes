#  Thread Locking
#  Avoiding the dreaded race conditions and deadlocks
#  Race condition:  same resource modified by multiple threads
#  Deadlock: multiple threads waiting on the same resource
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0


def test1(count):
    global counter
    thread_name = threading.currentThread().name
    logging.info(f'Starting: {thread_name}')

    for x in range(count):
        logging.info(f'Count: {thread_name}+ = {count}')
        #  The GIL (Global Interpreter Lock is in action
        #  counter += 1
        #  Locking
        """
        lock = threading.Lock()
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()
        """
        #  Locking Simplified
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {thread_name}')
            counter += 1
            time.sleep(2)
    logging.info(f'Completed: {thread_name}')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1, 5)
            ex.submit(test1, v)

    logging.info('App Finished')


if __name__ == '__main__':
    main()
