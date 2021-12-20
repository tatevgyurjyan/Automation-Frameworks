from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from lib.driver import get_driver
from lib.test_logger import logger
import random
import string


driver = get_driver()


def go_to_page(url, new_window=False):
    try:
        if new_window:
            driver.execute_script(f"window.open('{url}');")
        else:
            driver.get(url)
            driver.maximize_window()
            logger("The driver was successfully opened")

    except Exception as e:
        logger(e, True)


def find_and_click(loc, timeout=3):
    try:
        elem = find(loc, timeout)
        elem.click()
        logger("The element was successfully found anh clicked")
    except Exception as e:
        logger(e, True)


def find_and_send_keys(loc, inp_text, timeout=3, click=False):
    try:
        elem = find(loc, timeout)
        if click:
            elem.send_keys(inp_text+Keys.ENTER)
        else:
            elem.send_keys(inp_text)
        logger("The data was successfully sent")
    except Exception as e:
        logger(e, True)


def find(loc, timeout=3, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(loc))
        logger("The element was successfully presented")
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem
    except Exception as e:
        logger(e, True)


def find_all(loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(loc),
                                                        message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        return False
    return elements


def create_file_and_write(file_name, text):
    try:
        with open(file_name, 'a+') as f:
            f.write(text + '\n')
    except Exception as e:
        logger(e, True)


def waits(loc, timeout=10, wait_type=""):
    if wait_type == "presence":
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(loc), message=f"Element '{loc}' not found")
    elif wait_type == "all_presence":
        WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(loc),
                                             message=f"Elements '{loc}' not found!")
    elif wait_type == "visibility":
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(loc),
            message=f"Elements '{loc}' not found!")
    elif wait_type == "invisibility":
        WebDriverWait(driver, loc).until(EC.invisibility_of_element_located(loc),
                                         message=f"Element '{loc}' not found")
    elif wait_type == "clickable":
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(loc),
            message=f"Elements '{loc}' not found!")
    elif wait_type == "selected":
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_selected(loc),
            message=f"Elements '{loc}' not found!")
    else:
        logger("Type of wait is incorrect!")


def wait_for_page(page="", not_page="", timeout=10):
    if page:
        WebDriverWait(driver, timeout).until(
            EC.url_contains(page))
    elif not_page:
        WebDriverWait(driver, timeout).until_not(
            EC.url_contains(not_page))


def random_str(symbols_count, letters=True, digits=True):
    if letters and digits:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))
    elif letters:
        return ''.join(random.choices(string.ascii_letters, k=symbols_count))
    else:
        return ''.join(random.choices(string.digits, k=symbols_count))
