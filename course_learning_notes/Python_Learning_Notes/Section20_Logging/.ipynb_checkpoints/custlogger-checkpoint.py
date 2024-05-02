import inspect
import logging

def get_custom_logger(level, filename):
    function_name = inspect.stack()[1][3]
    logger_name = function_name  + " logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    
    fileHandler = logging.FileHandler(filename, mode='a')
    fileHandler.setLevel(level)
    
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                 datefmt = '%d/%m/%Y %I/%M/%S %p')
    
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger