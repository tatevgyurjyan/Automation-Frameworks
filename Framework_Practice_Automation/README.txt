
Application URL to work with: http://automationpractice.com/

DESIGNED TEST SCENARIOS -->

test_registration:              Go to the app
                                Create an account with existing email
                                Register user
                                Check that user is registered successfully

test_sign_in                    Navigate to Sign In page
                                Sign in with registered user
                                Check that user is signed in

test_contact_us_success:        Navigate to Contact Us
                                Fill all fields with valid data
                                Click on Send button
                                Check that successful validation message displays

test_contact_us_error:          Navigate to Contact Us
                                Fill all fields with valid data beside Message field
                                Click on Send button
                                Check that error message displays

test_woman_dresses:             Click on Dresses tab in Home page
                                Take all dresses names and their prices
                                Open file and write there with tuple, like Printed Dress: $26.00


TODO:                           pip install selenium webdriver

Impotred Libraries:             webdriver_manager.chrome, selenium, selenium.webdriver.support,
                                selenium.webdriver.support.ui, selenium.webdriver.common.keys, 
                                selenium.webdriver.support.wait, selenium.webdriver.common.by,
                                string, random, logging, time  

Design Pattern:         Page Object Model (modular structure) 

Selector:               XPATH

Project Modules:        lib --> drivers.py  (includes driver initilisation method)
                                helpers.py  (includes all common methods which are used in 'Pages')
                                        Designed Methods: -->  

                                                'go_to_page'
                                                'find_and_click'
                                                'find_and_send_keys'
                                                'find' 
                                                'find_all'                             
                                                'create_file_and_write'
                                                'waits'
                                                'wait_for_page'
                                                'random_str'
                                            
                                test_logger.py (includes method 'logger') 
                                
                        pages --> 

                                contact_us.py
                                        Designed Methods: -->
                                                'fill_message_details'
                                                'check_alert_message'                                             
                                home.py 
                                        Designed Methods: -->
                                                'get_dresses_names―and_prices'
                                             
                                sign_in.py
                                        Designed Methods: -->
                                                'sign_in_user'

                                sign_up.py
                                         Designed Methods: -->
                                                'click_sign_in_btn'
                                                'create_an_account'
                                                'registration'                                          
                        testdata --> 

                                test_data.py (includes test data, which are used in tests)
Test Cases:                               
                        tests: --> 
                               
                                'test_contact_us_error.py'
                                'test_contact_us_success.py'
                                'test_registration.py'
                                'test_sign_in.py'
                                'test_woman_dresses.py'

Log                     test_log.txt
