from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.test_logger import *
from lib.helpers import *


btn_sign_in = (By.XPATH, "//a[@class='login']")
input_email_address = (By.XPATH, "//input[@id='email_create']")
btn_create_acc = (By.XPATH, "//i[@class='icon-user left']")
txt_firstname = (By.XPATH, "//input[@id='customer_firstname']")
txt_lastname = (By.XPATH, "//input[@id='customer_lastname']")
txt_passwrd = (By.XPATH, "//input[@id='passwd']")
txt_firstname_second = (By.XPATH, "//input[@id='firstname']")
txt_lastname_second = (By.XPATH, "//input[@id='lastname']")
txt_address = (By.XPATH, "//input[@id='address1']")
txt_city = (By.XPATH, "//input[@id='city']")
txt_zipcode = (By.XPATH, "//input[@id='vpostcode']")
txt_mobile = (By.XPATH, "//input[@id='phone_mobile']")
txt_assign_alias = (By.XPATH, "//input[@id='alias']")
txt_country = (
    By.XPATH, "//select[@id='id_country']//option[contains(text(),'United States')]")
txt_state = (By.XPATH, "//select[@id='id_state']//option[@value='5']")
btn_register = (By.XPATH, "//button[@id='submitAccount']")
state_california = (By.XPATH, "//select[@id='id_state']//option[6]")
country_united_states = (By.XPATH, "//select[@id='id_country']//option[2]")
home_phone = (By.XPATH, "//input[@id='phone']")
mobile_number = (By.XPATH, "//input[@id='phone_mobile']")
radio_btn_female = (By.XPATH, "//input[@id='id_gender2']")
radio_btn_male = (By.XPATH, "//input[@id='id_gender1']")
input_zipcode = (By.XPATH, "//input[@id='postcode']")
sign_out_btn = (By.XPATH, "//a[@class='logout']")


def click_sign_in_btn():
    logger("sign in")
    find_and_click(btn_sign_in)
    wait_for_page("my-account")


def create_an_account():
    email = f"{random_str(10, True, True)}@{random_str(5, True, False)}.com"
    find_and_send_keys(input_email_address, email)
    logger(f"Email address for create an account: {email}")
    find_and_click(btn_create_acc)
    wait_for_page("account-creation")
    return email


def registration():
    logger("Navigate to 'Registration' page")
    find_and_click(radio_btn_female)
    firstname = random_str(6, True, False)
    lastname = random_str(6, True, False)
    password = random_str(6, True, True)
    firstname_sec = random_str(6, True, False)
    lastname_sec = random_str(6, True, False)
    city = random_str(6, True, False)
    find_and_send_keys(txt_firstname, firstname)
    find_and_send_keys(txt_lastname, lastname)
    find_and_send_keys(txt_passwrd, password)
    find_and_send_keys(txt_firstname_second, firstname_sec)
    find_and_send_keys(txt_lastname_second, lastname_sec)
    find_and_send_keys(txt_address, data.address)
    find_and_send_keys(txt_city, city)
    find_and_click(txt_state)
    find_and_click(state_california)
    find_and_send_keys(input_zipcode, data.zip_code)
    find_and_click(txt_country)
    find_and_click(country_united_states)
    find_and_send_keys(home_phone, data.home_phone)
    find_and_send_keys(txt_mobile, data.mobile_phone)
    find_and_click(btn_register)
    wait_for_page(not_page="account-creation")
