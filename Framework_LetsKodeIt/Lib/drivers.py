from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Lib.log_file import *


def get_driver():
    try:
        return webdriver.Chrome(ChromeDriverManager().install())
    except Exception as e:
        logger(e, error=True)
