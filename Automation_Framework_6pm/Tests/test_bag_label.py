from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Helper import test_logger
from Testdata import test_data
from Helper import helpers
from Pages import login
from Pages import search
from Pages import my_bag
import config


def test_bagLabel():

    test_logger.logger("-------test_bagLabel_starts---------")
    helpers.go_to_page(config.url)
    login.login_user()

    helpers.find_and_send_keys(search.search_field,
                               test_data.search_product_name)
    helpers.find_and_send_keys(search.search_field, Keys.ENTER)
    helpers.find_and_click(my_bag.product_item2)
    helpers.find_and_click(my_bag.add_to_bag_btn)
    helpers.driver.back()

    helpers.find_and_click(my_bag.product_item3)
    helpers.find_and_click(my_bag.add_to_bag_btn)
    helpers.driver.back()

    helpers.find_and_click(my_bag.product_item4)
    helpers.find_and_click(my_bag.add_to_bag_btn)
    helpers.driver.back()

    helpers.find_and_click(my_bag.view_bag_btn)

    # check that image quantity in bag and label number are equal
    number_on_corb_label = helpers.find(my_bag.label_number).text
    img_quantity_in_bag = len(helpers.find_all(my_bag.number_of_images_in_bag))

    assert str(img_quantity_in_bag) == number_on_corb_label, "Not Equal"
    test_logger.logger("Quantity of item images and on bag label are Equal")

    my_bag.get_empty_bag()
    assert helpers.find(my_bag.empty_bag_message), "Bag is not EMPTY"
    test_logger.logger("Bag is EMPTY")

    test_logger.logger("-------test_bagLabel_finished---------")
    helpers.driver.quit()


if __name__ == '__main__':
    test_bagLabel()
