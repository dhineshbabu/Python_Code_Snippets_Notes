# Logging Basics

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging


# Basic Logging

def test():
    print('-' * 20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log level: {level}')
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warn message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-' * 20)


test()

# Getting and Setting the logging levels
# Allows for filtering
rootlog = logging.getLogger()
print('Level ' + logging.getLevelName(rootlog.getEffectiveLevel()))
# Set it to Debug
rootlog.setLevel(logging.DEBUG)
test()

# Critical only
rootlog.setLevel(logging.CRITICAL)
test()

# Log to file - the below code will work if only root logger is not configured
# logging.basicConfig(filename="app.txt", filemode='w', format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('Hello')

handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('test log from pycharm')
test()
