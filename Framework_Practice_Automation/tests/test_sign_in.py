from lib.helpers import *
from testdata import test_data
from pages import sign_in
from lib.test_logger import *
from lib.driver import *


def test_signin():
    logger("------------'sign_in' test starts------------")
    go_to_page(test_data.url)
    sign_in.sign_in_user()
    assert sign_in.sign_out_btn, "Failed"
    logger(f"User {data.first_name} is signed in")

    logger("----------'sign_in' test finished------------")
    driver.quit()


if __name__ == '__main__':
    test_signin()
