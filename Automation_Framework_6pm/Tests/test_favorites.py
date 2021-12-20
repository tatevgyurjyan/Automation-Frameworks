from selenium.webdriver.common.by import By
from Helper import test_logger
from Testdata import test_data
from Pages import favorites
from Helper import helpers
from Pages import login
import config
import time


def test_favorites():

    test_logger.logger("-------test_favorites_starts--------------")
    helpers.go_to_page(config.url)
    login.login_user()

    helpers.find_and_click(favorites.accessories_link)
    helpers.find_and_click(favorites.watches_link)
    favorites.add_to_favorites()
    time.sleep(1)
    helpers.find_and_click(favorites.account_favs)
    time.sleep(1)
    txt_favs = helpers.find(favorites.favs_numbers).text
    favs_digit = "".join(filter(str.isdigit, txt_favs))

    assert int(favs_digit) > 0, "Didn't work"
    test_logger.logger(f"You have {favs_digit} items in your favorites")

    test_logger.logger("-------test_favorites_finished--------------")
    helpers.driver.quit()


if __name__ == '__main__':
    test_favorites()
