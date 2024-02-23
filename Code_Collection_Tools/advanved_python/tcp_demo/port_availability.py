#  Determine port availability
#  Find out if port is already in use
#  Different ways to do the same task


import logging
import socket
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


#  Check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip}: {port}')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.setdefaulttimeout(timeout)
        socket.timeout(timeout)
        con = s.connect_ex((ip, port))
        logging.debug(f'Connection {ip}: {port} = {con}')
        s.close()
        if con == 0:
            ret = False
            logging.debug(f'In use {ip}: {port}')
        else:
            ret = True
            logging.debug(f'Usable {ip}: {port}')
    except Exception as e:
        ret = False
        logging.debug(f'Error {ip}: {port} = {e.msg}')
    finally:
        logging.debug(f'Returning {ip}: {port} = {ret}')
        return ret


#  Checking a range of ports
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


#  See it in action
def main():
    #  Test one port
    p = check_port('localhost', 2594, 2.0)
    logging.info(f'Port 2594 usable: {p}')

    #  Testing a range of ports
    ports = check_range('localhost', range(3300, 3309))
    for k, v in ports.items():
        logging.info(f'Port {k} usable {v}')


if __name__ == '__main__':
    main()