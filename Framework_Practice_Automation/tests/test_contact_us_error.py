from pages import contact_us
from lib.test_logger import *
from lib.helpers import *
from lib.driver import *


def test_contact_us_errors():
    logger("--------'contact_us_error' test starts------------")
    go_to_page(data.url)
    contact_us.fill_message_details()
    contact_us.check_alert_message(False)
    assert contact_us.alert_error_msg, "Failed"
    logger("Error message is displayed")

    logger("----------'contact_us_error' test finished--------")
    driver.quit()


if __name__ == '__main__':
    test_contact_us_errors()
