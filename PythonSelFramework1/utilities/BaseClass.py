import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, input_text):
        wait = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, input_text)))

    def select_option_by_test(self, locator,  text):
        sel = Select(locator.get_gender())
        sel.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # Filehandler object
        logger.setLevel(logging.INFO)
        return logger