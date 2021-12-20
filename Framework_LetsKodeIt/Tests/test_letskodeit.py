from Pages import sign_up_page as register
from Pages import sign_in_page as signin
from Pages import courses_page as courses
import Test_Data.test_data as data
from Lib.log_file import *
from Lib.drivers import *
from Lib.helpers import *


def test_lets_kodeit():

    get_url(data.url_reg)
    register.sign_up_user()

    # compares registered name from UI with given data
    assert signin.verify_user_sign_in() == data.first_name, "Failed"
    logger("Our code rocks!")
    signin.go_to_courses_page()

    courses.search_given_course_name()
    courses.search_results()

    driver.quit()
    logger("Test is Passed!")


if __name__ == '__main__':
    test_lets_kodeit()
