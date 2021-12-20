from lib.test_logger import *
from lib.helpers import *
from lib.driver import *
from pages import contact_us


def test_contact_us_success():
    logger("----------'contact_us_success' test starts---------------")
    go_to_page(data.url)
    contact_us.fill_message_details()
    contact_us.check_alert_message(True)
    assert contact_us.alert_success_text, "Failed to send message"
    logger(f"{data.message_text} - Message is successfully sent.")

    logger("----------'contact_us_success' Test is finished-----------")
    driver.quit()


if __name__ == '__main__':
    test_contact_us_success()
