#  Blocking vs Non-blocking Sockets
#  Blocking stop
#  Non Blocking runs in the background


import logging
import logging
import select
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


#  Blocking socket
def create_blocking(host, port):
    logging.info('Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info('Blocking - connecting')
    s.connect((host, port))
    logging.info('Blocking - connected')
    logging.info('Blocking - sending...')
    s.send(b'hello\r\n')
    logging.info('Blocking - waiting on response')
    data = s.recv(1024)
    logging.info(f'Blocking - data = {len(data)}')
    logging.info('Blocking - Closing...')
    s.close()


#  Non-blocking Socket
def create_nonblocking(host, port):
    logging.info('NonBlocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info('NonBlocking - connecting')
    ret = s.connect_ex((host, port))
    if ret != 0:
        logging.info('NonBlocking - failed to connect')
        return
    logging.info('NonBlocking - connected!')
    s.setblocking(False)
    inputs = [s]
    outputs = [s]
    while inputs:
        logging.info('NonBlocking - waiting...')
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)
        for s in writable:
            logging.info('NonBlocking - sending...')
            data = s.send(b'hello\r\n')
            logging.info(f'NonBlocking - sent: {data}')
            outputs.remove(s)
        for s in readable:
            logging.info('NonBlocking - reading...')
            data = s.recv(1024)
            logging.info(f'NonBlocking - data: {data}')
            logging.info('NonBlocking - closing...')
            s.close()
            inputs.remove(s)
            break
        for s in exceptional:
            logging.info('NonBlocking - error')
            inputs.remove(s)
            outputs.remove(s)
            break


#  Main function
def main():
    #  create_blocking('voidrealms.com', 80)
    create_nonblocking('voidrealms.com', 80)


if __name__ == '__main__':
    main()