from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import Test_Data.test_data as data
from Lib.log_file import *
from Lib.drivers import *
import random
import string

driver = get_driver()


def get_url(url):
    try:
        driver.maximize_window()
        return driver.get(url)
    except Exception as e:
        logger(e, error=True)


def find_and_wait_elem(locator, sec=10):
    try:
        elem = WebDriverWait(driver, sec).until(
            EC.presence_of_element_located(locator))
        return elem
    except Exception as e:
        logger(e, error=True)


def find_several_elements(locator, sec=10):
    try:
        elem = WebDriverWait(driver, sec).until(
            EC.presence_of_all_elements_located(locator))
        return elem
    except Exception as e:
        logger(e, error=True)


def find_and_click(locator):
    try:
        elem = find_and_wait_elem(locator)
        elem.click()
    except Exception as e:
        logger(e, error=True)


def find_and_send_keys(locator, text):
    try:
        elem = find_and_wait_elem(locator)
        elem.send_keys(text)
    except Exception as e:
        logger(e, error=True)


def create_file_and_write(text):
    try:
        with open(data.text_file, mode="a+") as f:
            f.write(text + "\n")
    except Exception as e:
        logger(e, error=True)


def email_generator():
    try:
        email_providers = ["gmail", "yahoo", "mail", "hotmail"]
        domains = [".com", ".de", ".ru", ".org", ".net"]
        str_email_name = "".join([string.ascii_letters, string.digits])
        email_address = "".join(random.choices(str_email_name, k=10)) + \
            "@" + random.choice(email_providers) + random.choice(domains)
        return email_address
    except Exception as e:
        logger(e, error=True)


def password_generator():
    try:
        str_password = "".join(
            [string.ascii_letters, string.digits, '!', '@', '$', '&', '#'])
        my_password = "".join(random.choices(str_password, k=10))
        return my_password
    except Exception as e:
        logger(e, error=True)
