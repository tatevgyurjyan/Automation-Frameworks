from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.helpers import *
import time


dresses_btn = (
    By.XPATH, "//li[@id='category-thumbnail']//following::a[@title='Dresses']")
all_dresses = (
    By.XPATH, "//a[@class='product_img_link']/img[contains(@title, 'Dress' )]")
all_prices = (
    By.XPATH, "//div[@class='right-block']//span[@class='price product-price']")


def get_dresses_names_and_prices():
    try:
        find_and_click(dresses_btn)
        time.sleep(2)
        women_dresses = find_all(all_dresses)
        dresses_prices = find_all(all_prices)

        names = []
        for dress in women_dresses:
            dress_name = dress.get_attribute("title")
            names.append(dress_name)
        prices = []
        for item in dresses_prices:
            price = item.text
            prices.append(price)
        for i in range(0, 5):
            create_file_and_write(data.data_file,
                                  names[i] + " : " + prices[i])

    except Exception as e:
        logger(e, error=True)
