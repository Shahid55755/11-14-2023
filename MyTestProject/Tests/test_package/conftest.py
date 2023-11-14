import inspect

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import logging


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Specify the browser (chrome, firefox, Edge)")


class BaseTest:
    @pytest.fixture(scope="class")
    def setup(self, request):
        browser_name = request.config.getoption("browser_name")

        if browser_name == "chrome":
            # Configure Chrome options
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=chrome_options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        elif browser_name == "Edge":
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Invalid browser name: {browser_name}. Supported values are chrome, firefox, Edge.")

        request.cls.driver = driver
        driver.get("https://www.demoblaze.com/")
        yield
        driver.quit()

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
