from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import Test_Data.test_data as data
from Lib.log_file import *
from Lib.helpers import *
import time

course_search_box = (By.XPATH, "//input[@name='course']")
search_res_titles = (By.XPATH, "//h4[contains(text(), 'Selenium')]")
course_prices = (By.XPATH, "//span[contains(@class, 'zen-course-price')]")


def search_given_course_name():
    try:
        find_and_send_keys(course_search_box, data.search_data)
        find_and_send_keys(course_search_box, Keys.RETURN)
        logger(f"Word '{data.search_data}' is entered to be searched")
        time.sleep(2)
    except Exception as e:
        logger(e, error=True)


def search_results():  # Find and write course titles and their prices
    try:
        results = find_several_elements(search_res_titles)
        res = str(len(results))
        create_file_and_write("Total Number of Found Courses Is " + res)

        prices = find_several_elements(course_prices)
        for title in results:
            for price in prices:
                pass
            create_file_and_write(title.text + " -- " + price.text)

    except Exception as e:
        logger(e, error=True)
