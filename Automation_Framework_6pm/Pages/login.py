from selenium.webdriver.common.by import By
from Helper import test_logger
from Helper import helpers
import config as data


login_btn = (By.XPATH, "//a[@class='y-z']")
email = (By.XPATH, "//input[@id='ap_email']")
pswd = (By.XPATH, "//input[@id='ap_password']")
sign_in_btn = (By.XPATH, "//input[@class='a-button-input']")
greeting_text = (By.XPATH, "//h1[text()='Hello, Vahan!']")


def login_user():
    try:
        helpers.find_and_click(login_btn)
        helpers.find_and_send_keys(email, data.username)
        helpers.find_and_send_keys(pswd, data.password)
        helpers.find_and_click(sign_in_btn)
        test_logger.logger("User is LOGGED IN")
        my_greeting = helpers.find(greeting_text)
        test_logger.logger(f"{my_greeting}")

    except Exception as e:
        test_logger.logger(e, True)
