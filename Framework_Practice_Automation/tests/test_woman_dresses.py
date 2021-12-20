from lib.test_logger import *
from lib.helpers import *
from lib.driver import *
from pages import home


def test_find_dresses_names_and_prices():
    logger("-------------'test_woman_dresses' started!----------------")
    go_to_page(data.url)
    home.get_dresses_names_and_prices()
    logger("----------'test_woman_dresses' test finished'-------------")
    driver.quit()


if __name__ == '__main__':
    test_find_dresses_names_and_prices()
