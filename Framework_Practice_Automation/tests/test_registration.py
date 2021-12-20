from testdata import test_data as data
from lib.test_logger import *
from lib.helpers import *
from lib.driver import *
from pages import sign_up


def test_user_registration():
    logger("-----------'registration' test starts-----------")
    go_to_page(data.url)
    sign_up.click_sign_in_btn()
    sign_up.create_an_account()
    sign_up.registration()
    assert sign_up.sign_out_btn, "Failed"
    logger("User is registered")

    logger("-----------'registration' test finished----------")
    driver.quit()


if __name__ == '__main__':
    test_user_registration()
