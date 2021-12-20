from Helper import driver
from Helper import test_logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = driver.get_driver()


def go_to_page(url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(loc, timeout=3):
    try:
        elem = find(loc, timeout)
        elem.click()
        test_logger.logger("The element was successfully found and clicked")
    except Exception as e:
        test_logger.logger(e, True)


def find_and_send_keys(loc, inp_text, timeout=3, click=False):
    try:
        elem = find(loc, timeout)
        if click:
            elem.send_keys(inp_text, Keys.ENTER)
        else:
            elem.send_keys(inp_text)
        test_logger.logger("The data was successfully sent")
    except Exception as e:
        test_logger.logger(e, True)


def find(loc, timeout=3, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(loc))
        test_logger.logger("The element was successfully presented")
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem
    except Exception as e:
        test_logger.logger(e, True)


def find_all(loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(
                                EC.presence_of_all_elements_located(loc),
                                message=f"Elements '{loc}' not found!")
    except Exception as e:
        test_logger.logger(e, True)
        return False
    return elements
