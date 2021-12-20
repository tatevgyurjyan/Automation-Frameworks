from selenium.webdriver.common.by import By
from Lib.log_file import *
from Lib.helpers import *


user_profile_img = (By.XPATH, "//img[contains(@src, 'user-profile')]")
my_account = (By.XPATH, "//a[@href='/account']")
home_btn = (By.XPATH, "//a[text()='Home']")
all_courses_link = (By.XPATH, "//a[text()='ALL COURSES']")
first_name_value = (
    By.XPATH, "//label[text()='First Name']//following::input[1]")


def verify_user_sign_in():  # Takes the registered name from UI
    try:
        find_and_click(user_profile_img)
        find_and_click(my_account)
        user_name = find_and_wait_elem(first_name_value)
        logger(f"User '{user_name.get_attribute('value')}'is Logged In")
        return user_name.get_attribute("value")
    except Exception as e:
        logger(e, error=True)


def go_to_courses_page():
    try:
        find_and_click(home_btn)
        find_and_click(all_courses_link)
        logger("We are on 'Courses' Page!")
    except Exception as e:
        logger(e, error=True)
