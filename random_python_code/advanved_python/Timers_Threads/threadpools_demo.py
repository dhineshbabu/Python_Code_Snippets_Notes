#  Thread pools
#  Reusing existing threads, because creating threads are expensive

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random


def test1(item):
    s = random.randrange(1, 10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.currentThread().name}')
    logging.info(f'Thread {item}: sleeping for = {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')


#  Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')
    workers = 5
    items = 15

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test1, range(items))
    logging.info('App Finished')


if __name__ == "__main__":
    main()


