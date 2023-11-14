import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import inspect
from Tests.test_package.conftest import BaseTest


@pytest.mark.usefixtures("setup")
class BasePage(BaseTest):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    # You can add more generic functions for commonly used actions on a page

    def click_element(self, by, value, timeout=10):
        element = self.wait_for_element(by, value, timeout)
        element.click()

    def send_keys_to_element(self, by, value, keys, timeout=10):
        element = self.wait_for_element(by, value, timeout)
        element.send_keys(keys)

    @pytest.mark.usefixtures("setup")
    def getLogger(self):
        # to get the name of the test case file name at runtime
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # FileHandler class to set the location of log file
        # filehandler = logging.FileHandler('logfile.log')
        filehandler = logging.FileHandler(r'C:\Users\Shahid.Ali\PycharmProjects\MyTestProject\logfile.log')

        # Formatter class to set the format of log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # object of FileHandler gets formatting info from setFormatter #method
        filehandler.setFormatter(formatter)
        # logger object gets formatting, path of log file info with addHandler #method
        logger.addHandler(filehandler)
        # setting logging level to INFO
        logger.setLevel(logging.INFO)
        return logger
