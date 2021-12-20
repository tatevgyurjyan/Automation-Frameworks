from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Helper import test_logger
from Testdata import test_data
from Helper import helpers
from Pages import login
from Pages import search
from Pages import my_bag
import config
import time
import re


def test_my_bag():

    test_logger.logger("-------test_bag_functionality_starts---------")
    helpers.go_to_page(config.url)
    login.login_user()

    helpers.find_and_send_keys(search.search_field,
                               test_data.search_product_name)
    helpers.find_and_send_keys(search.search_field, Keys.ENTER)
    my_bag.add_items_to_bag()

    # check that price near item and subtotal price in checkout are equal
    mentioned_price_on_image = helpers.find(my_bag.item_prices_in_bag).text
    total_number_of_items_in_checkout = helpers.find(
        my_bag.subtotal_number_in_bag).text

    assert total_number_of_items_in_checkout == mentioned_price_on_image, "F"
    test_logger.logger("Prices on label and in bag subtotal are the Same")

    # check that image quantity in bag and label number are equal
    number_on_corb_label = helpers.find(my_bag.label_number).text
    img_quantity_in_bag = len(helpers.find_all(my_bag.number_of_images_in_bag))

    assert str(img_quantity_in_bag) == number_on_corb_label, "Not Equal"
    test_logger.logger("Quantity of item images and on bag label are Equal")

    helpers.driver.back()
    helpers.driver.back()
    time.sleep(1)

    my_bag.add_items_to_bag()
    time.sleep(1)
    my_bag.get_quantity_from_subtotal_text()

    # check that items sum of price and subtotal price in checkout are equal
    sum_price = my_bag.get_sum_of_item_prices_in_bag()
    subtotal_txt = helpers.find(my_bag.subtotal_number_in_bag).text
    rest, subtotal_fdigit = re.split(r"\$", subtotal_txt)
    subtotal_digit, rest = re.split(r"\.", subtotal_fdigit)

    assert sum_price == subtotal_digit, "Prices are Not Correct"
    test_logger.logger("Prices on label and in bag subtotal are the Same")

    # check that subtotal quantity and label number are equal
    label_digit = helpers.find(my_bag.label_number).text

    assert my_bag.get_quantity_from_subtotal_text() == label_digit, "Not Equal"
    test_logger.logger("Quantities are AGAIN Equal")

    test_logger.logger("-------test_bag_functionality_finished--------")
    helpers.driver.quit()


if __name__ == '__main__':
    test_my_bag()
