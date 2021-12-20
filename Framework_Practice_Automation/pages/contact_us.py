from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.test_logger import *
from lib.helpers import *


contact_us_btn = (By.XPATH, "//a[@title='Contact Us']")
choose_subject_heading_btn = (By.XPATH, "//select[@id='id_contact']")
option_choose = (By.XPATH, "//select[@id='id_contact']//option[1]")
customer_service_option = (By.XPATH, "//select[@id='id_contact']//option[2]")
web_master_option = (By.XPATH, "//select[@id='id_contact']//option[3]")
email_address_input = (By.XPATH, "//input[@id='email']")
order_reference = (By.XPATH, "//input[@id='id_order']")
choose_file_btn = (By.XPATH, "//input[@class='form-control']")
msg_text_area = (By.XPATH, "//textarea[@id='message']")
send_btn = (By.XPATH, "//span[text()='Send']")
alert_success_text = (By.XPATH, "//p[@class='alert alert-success']")
alert_error_msg = (By.XPATH, "//div[@class='alert alert-danger']")


def fill_message_details():
    try:
        find_and_click(contact_us_btn)
        find_and_click(choose_subject_heading_btn)
        find_and_click(customer_service_option)
        find_and_send_keys(email_address_input, data.email_sign_in)
        find_and_send_keys(order_reference, data.order_reference)
    except Exception as e:
        logger(e, True)


def check_alert_message(success_indicator=True):
    try:
        if success_indicator:
            find_and_send_keys(msg_text_area, data.message_text)
            find_and_click(send_btn)
            alert_message = find(alert_success_text).text
        else:
            find_and_click(send_btn)
            alert_message = find(alert_error_msg).text
        logger(f"{alert_message}")

    except Exception as e:
        logger(e, True)
