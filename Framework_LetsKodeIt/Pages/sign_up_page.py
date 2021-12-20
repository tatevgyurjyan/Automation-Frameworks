from selenium.webdriver.common.by import By
import Test_Data.test_data as data
from Lib.log_file import *
from Lib.helpers import *


first_name = (By.XPATH, "//input[@placeholder='First Name']")
last_name = (By.XPATH, "//input[@id='last_name']")
email_sign_up = (By.XPATH, "//div[@class='form-group']/input[@id='email']")
pswd_sign_up = (By.XPATH, "//input[@id='password']")
pswd_confirm = (By.XPATH, "//input[@id='password_confirmation']")
sign_up_btn = (By.XPATH, "//input[@value='Sign Up']")


def sign_up_user():
    try:
        email = email_generator()
        password = password_generator()
        find_and_send_keys(first_name, data.first_name)
        find_and_send_keys(last_name, data.last_name)
        find_and_send_keys(email_sign_up, email)
        find_and_send_keys(pswd_sign_up, password)
        find_and_send_keys(pswd_confirm, password)
        find_and_click(sign_up_btn)
        logger(f"Generated email = {email} and password={password}")
        logger(f"Success! '{data.first_name} {data.last_name}' is Registered")
    except Exception as e:
        logger(e, error=True)
