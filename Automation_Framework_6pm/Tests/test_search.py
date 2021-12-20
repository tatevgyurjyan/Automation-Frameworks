from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Helper import test_logger
from Testdata import test_data
from Helper import helpers
from Pages import login
from Pages import search
import config
import time


def test_search_sunglasses():

    test_logger.logger("-------test_search_sunglasses_starts-----------")
    helpers.go_to_page(config.url)
    login.login_user()

    helpers.find_and_send_keys(search.search_field,
                               test_data.search_product_name)
    helpers.find_and_send_keys(search.search_field, Keys.ENTER)
    helpers.find_and_click(search.shop_by_price)
    helpers.find_and_click(search.under_50_link)
    helpers.find_and_click(search.brand_check_box)

    number_of_found_items = helpers.find_all(search.found_result)
    whole_text = helpers.find(search.items_found_text).text
    num_of_result = ''.join(filter(str.isdigit, whole_text))

    assert num_of_result == str(len(number_of_found_items)), "Failed"
    test_logger.logger("Number of sunglasses is equal to Found Result")
    test_logger.logger("-------test_search_sunglasses_finished-----------")

    helpers.driver.quit()


if __name__ == '__main__':
    test_search_sunglasses()
