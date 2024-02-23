#  Daemon Threads - Quitting when we quit the app
import logging
import threading
from threading import Timer, Thread
import time


def test1():
    thread_name =  threading.currentThread().name
    logging.info(f'Starting: {thread_name}')
    for x in range(60):
        logging.info(f'Working: {thread_name}')
        time.sleep(1)
    logging.info(f'Finished: {thread_name}')


def stop():
    logging.info('Exiting the application')
    exit(0)


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Started')
    #  Stop in 3 seconds
    timer = Timer(3, stop)
    timer.start()

    #  Run a thread
    t = Thread(target=test1, daemon=True)
    t.start()
    logging.info('Main thread Finished')


if __name__ == '__main__':
    main()