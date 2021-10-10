#  Multiprocessing
#  Multiple processes running in the same script
#  This is very different from threading
#  Each process has its own memory space and its own threads

import logging
import multiprocessing
from multiprocessing import  process
import time

# Process starting function
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num * 2)
    logging.info(f'Finished {name} as {__name__}')


# Basic Process Usage

def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=(x,), daemon=True)
        processes.append(p)
        p.start()

    #  Wait for the processes
    for p in processes:
        p.join()  #  joining MainProcess to wait for other Processes to complete
    logging.info(f'Finished {name} as {__name__}')


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == '__main__':
    main()
