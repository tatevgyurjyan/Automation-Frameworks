Application URL to work with: https://courses.letskodeit.com/register

Test Scenario:
                        . Open the web app in Chrome browser
                        . Sign up into the application
                        . Sign in with the registered user
                        . Check that you are logged in
                        . Navigate to “All Courses”
                        . Search the “Selenium” word
                        . Log search result count, result’s titles and prices in a file


TODO:                   pip install selenium webdriver

Impotred Libraries:     webdriver_manager.chrome, selenium, logging, selenium.webdriver.support,
                        selenium.webdriver.support.ui, selenium.webdriver.common.keys, 
                        selenium.webdriver.common.by, string, random, time  

Design Pattern:         Page Object Model (modular structure) 

Selector:               XPATH

Project Modules:        Lib --> drivers.py  (includes driver initilisation method)
                                helpers.py  (includes all common methods which are used in 'Pages')
                                        Designed Methods: -->  

                                                'get_url'
                                                'find_and_wait_elem' 
                                                'find_several_elements'
                                                'find_and_click'
                                                'find_and_send_keys'
                                                'create_file_and_write' 
                                                'email_generator'                             
                                                'password_generator'

                                log_file.py (includes method 'create_log_file')                              
                        Pages --> 

                                sign_up_page.py
                                        Designed Methods: -->
                                                'sign_up_user'
                                sign_in_page.py 
                                        Designed Methods: -->
                                                'verify_user_sign_in'
                                                'go_to_courses_page'
                                courses_page.py
                                        Designed Methods: -->
                                                'search_given_course_name'
                                                'search_results'

                        Test_Data --> 

                                test_data.py (includes test data, which are used in tests)
Test Runer:                               
                        Tests: --> 
                                test_letskodeit.py (includes method test_lets_kodeit which calls methods from Pages)

Run result files:       test_log.txt
                        search_result.txt

Tests should be run in Python. 
