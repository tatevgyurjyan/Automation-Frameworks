from selenium.webdriver.common.by import By
from Testdata import test_data
from Helper import test_logger
from Helper import helpers
import random


accessories_link = (By.XPATH, "//a[@href='/accessories']")
watches_link = (By.XPATH, "//article/a[contains(@href, 'women-watches')]")
account_favs = (By.XPATH, "//a[@href='/account/favorites']")
favs_numbers = (By.XPATH, "//a[text()='Hearts']//following::span")
hearts_to_add_favs = (By.XPATH, "//button[@data-test-id='heartButton']")


def add_to_favorites():
    try:
        hearts = helpers.find_all(hearts_to_add_favs)
        for i in range(len(hearts)):
            random.choices(hearts, k=6)[i].click()
        test_logger.logger("Items are favoritized")
    except Exception as e:
        test_logger.logger(e)
