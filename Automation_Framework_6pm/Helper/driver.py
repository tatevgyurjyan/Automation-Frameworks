from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Helper.helpers import *
from Helper import test_logger


def get_driver():
    try:
        return webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
    except Exception as e:
        test_logger.logger(e, True)
