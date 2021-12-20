from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.helpers import *


sign_in_btn = (By.XPATH, "//a[@class='login']")
email_sign_in = (By.XPATH, "//input[@id='email']")
pswd_sign_in = (By.XPATH, "//input[@id='passwd']")
login_btn = (By.XPATH, "//i[@class='icon-lock left']")
sign_out_btn = (By.XPATH, "//a[@class='logout']")


def sign_in_user():
    try:
        find_and_click(sign_in_btn)
        find_and_send_keys(email_sign_in, data.email_sign_in)
        find_and_send_keys(pswd_sign_in, data.sign_in_pswd)
        find_and_click(login_btn)
        logger(f"User {data.first_name} is logged in")
    except Exception as e:
        logger(e, error=True)
