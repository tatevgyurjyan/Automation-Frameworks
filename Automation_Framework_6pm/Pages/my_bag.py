from selenium.webdriver.common.by import By
from Testdata import test_data
from Helper import test_logger
from Helper import helpers
import time
import re


all_sunglasses = (By.XPATH,
                  "//h2[text()='Womens Sunglasses']//following::article")
add_to_bag_btn = (By.XPATH, "//button[@data-track-value='Add-To-Cart']")
view_bag_btn = (By.XPATH, "//a[text()='View ']")
label_number = (By.XPATH, "//span[@class='f-z']")
number_of_images_in_bag = (By.XPATH, "//a[@class='kf-z']")
item_prices_in_bag = (By.XPATH, "//em[contains(text(), '$')]")
subtotal_number_in_bag = (By.XPATH, "//dl[@class='OZ-z']/dd")
remove_item_btn = (By.XPATH, "//button[@aria-label='Remove Item']")
empty_bag_message = (By.XPATH, "//p[contains(text(), 'Fill up your ')]")
remove_btn = (By.XPATH, "//button[text()='Remove']")
bag_btn = (By.XPATH, "//a[@href='/cart']")
subtotal_text = (By.XPATH, "//dt[text()='Subtotal']/span")


def get_sum_of_item_prices_in_bag():
    try:
        total_price = helpers.find_all(item_prices_in_bag)
        sum_of_prices_float = 0

        for i in range(len(total_price)):
            item_price = total_price[i].text
            rest, item_price_txt = re.split(r"\$", item_price)
            sum_of_prices_float += float(item_price_txt)
        sum_of_prices_in_bag, rest = re.split(r"\.", str(sum_of_prices_float))

        return str(sum_of_prices_in_bag)
    except Exception as e:
        test_logger.logger(e)


def add_items_to_bag():
    try:
        sunglasses = helpers.find_all(all_sunglasses)
        for i in range(2):
            sunglasses[i].click()
            helpers.find_and_click(add_to_bag_btn)
            helpers.find_and_click(view_bag_btn)
    except Exception as e:
        test_logger.logger(e)


def get_empty_bag():
    try:
        remove_items = helpers.find_all(remove_item_btn)
        for i in range(len(remove_items)):
            remove_items[i].click()
    except Exception as e:
        test_logger.logger(e)


def get_quantity_from_subtotal_text():
    try:
        quantity_txt = helpers.find(subtotal_text).text
        string_number, rest = re.split(r"\s", quantity_txt)
        res, quantity_digit = re.split(r"\(", str(string_number))
        return quantity_digit
    except Exception as e:
        test_logger.logger(e)
