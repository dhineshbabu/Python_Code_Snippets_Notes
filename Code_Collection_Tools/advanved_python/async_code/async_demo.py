#  Async Demo
#  Async code run in the same thread
#  Async uses coroutines which run on the same thread
#  We also introduce the "async" and "await" keywords


import threading
import multiprocessing
import logging
import asyncio
import random
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


#  Functions
def display(msg):
    thread_name = threading.current_thread().name
    process_name = multiprocessing.current_process().name
    logging.info(f'{process_name}\{thread_name}: {msg}')


async def work(name):
    display(name + ' starting')
    #  Do some work here
    await asyncio.sleep(random.randint(1, 10))
    display(name + ' finished')


async def run_async(max):
    tasks = []
    for x in range(max):
        name = 'Item' + str(x)
        tasks.append(asyncio.ensure_future(work(name)))
    await asyncio.gather(*tasks)


#  Main function
def main():
    display('Main Started')
    loop = asyncio.get_event_loop()
    #  Loop until an async task is done
    loop.run_until_complete(run_async(50))
    #  will run forever!
    # loop.run_forever()
    #  Stop looping and free up resources
    loop.close()
    display('Main Finished')


if __name__ == '__main__':
    main()