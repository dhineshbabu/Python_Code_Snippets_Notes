#  Queues and Futures

#  Getting values from a thread
#  This is a problem for future me

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import time
import random
from queue import Queue


def test_queue(name: str, que: Queue):
    thread_name = threading.current_thread().name
    logging.info(f'Starting: {thread_name}')
    time.sleep(random.randrange(1, 5))
    logging.info(f'Finished: {thread_name}')
    ret = 'Hello ' + name + ' your random number is: '+ str(random.randrange(1, 100))
    que.put(ret)


#  Queues
def queued():
    que = Queue()
    t = Thread(target=test_queue, args=['Bryan', que])
    t.start()
    logging.info('Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')


#  Futures
#  Use futures, easier and cleaner
def test_future(name: str):
    thread_name = threading.current_thread().name
    logging.info(f'Starting: {thread_name}')
    time.sleep(random.randrange(1, 5))
    logging.info(f'Finished: {thread_name}')
    ret = 'Hello ' + name + ' your random number is: '+ str(random.randrange(1, 100))
    return ret


def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future, 'Bryan' + str(x))
            ret.append(future)
    logging.info('Do something on the main thread')
    for r in ret:
        logging.info(f'Returned : {r.result()}')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')
    #  queued()
    pooled()


if __name__ == '__main__':
    main()
