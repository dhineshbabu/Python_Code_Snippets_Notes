#  Multiprocess starting and stopping
#  The full lifecycle

import logging
import multiprocessing
from multiprocessing.context import Process
import time


# worker process
def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'{name} finished')


#  main process
def main():
    logging.info('Started')
    max = 2
    worker = Process(target=work, args=['Working', max], daemon=True, name='Worker')
    worker.start()
    time.sleep(5)
    #  if the process is running, stop it
    if worker.is_alive:
        worker.terminate()
    worker.join()
    #  exitcode==0 good
    #  anything else for exit code is an error
    logging.info(f'Finished: {worker.exitcode}')


#  main process
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == '__main__':
    main()