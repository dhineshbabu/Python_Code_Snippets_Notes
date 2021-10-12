#  Communicating with processes in the same and remote machines

import logging
import time
import multiprocessing
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


#  Worker Process
def proc(server='localhost', port=6000, password=b'password'):
    name = process.current_process().name
    logging.info(f'{name} started')
    #  Start listening for connections
    address = (server, port)
    listener = Listener(address, authkey=password)
    conn = listener.accept()
    logging.info(f'{name}: connection from {listener.last_accepted}')
    #  Loop for input from connected process
    while True:
        msg = conn.recv()
        logging.info(f'{name} data in: {msg}')
        if msg == 'quit':
            conn.close()
            break
    listener.close()
    logging.info(f'{name} finished')


#  Main function
def main():
    name = process.current_process().name
    logging.info(f'{name} started')
    #  Setup the process
    address = 'localhost'
    #  any port above 1024 (these are system ports)
    port = 2923
    password = b'password'
    p = Process(target=proc, args=(address, port, password), daemon=True, name="Worker")
    p.start()
    logging.info(f'{name} waiting on the working...')
    time.sleep(1)
    #  Connect to the process
    dest = (address, port)
    conn = Client(dest, authkey=password)
    while True:
        command = input('\r\n Enter a command or type quit:\r\n').strip()
        logging.info(f'{name} command: {command}')
        conn.send(command)
        if command == 'quit':
            break
    #  Cleanup and Shutdown
    if p.is_alive:
        logging.info(f'{name} terminating worker')
        conn.close()
        time.sleep(1)
        p.terminate()
    p.join()
    logging.info(f'{name} finished')


if __name__ == '__main__':
    main()

