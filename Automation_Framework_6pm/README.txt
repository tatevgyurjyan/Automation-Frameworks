Application URL to work with: https://www.6pm.com/

DESIGNED TEST SCENARIOS -->

test_search:                    Login to 6pm
                                Search Sunglasses
                                Select Shop By Price- $50 and Under
                                Check on any brand checkbox (e.g., Calvin Klein): Brand should be configured 
                                Verify that the Number of available sunglasses is equal to found result


test_bag_functionality          Login to 6pm
                                Search Sunglasses
                                Add one of sunglasses to the Bag
                                Click View Bag
                                Verify that the price and count are correct
                                Add 2nd sunglasses to the bag
                                Verify that the price and count are changed accordingly


test_bag_label:                 Login to 6pm
                                Add several items to the bag
                                Verify that the number of items on the bag label is correct
                                Click View Bag
                                Remove items
                                Verify that the bag is empty


test_favorites:                 Login to 6pm
                                Go to the Accessories department
                                Select Watches
                                Make a few watches as favorites
                                Go to Favorites screen
                                Verify that the favorite data is correct


TODO:                           pip install selenium webdriver

Impotred Libraries:             webdriver_manager.chrome, selenium, selenium.webdriver.support,
                                selenium.webdriver.common.keys, selenium.webdriver.support.wait, 
                                selenium.webdriver.common.by, logging, time, re

Design Pattern:         Page Object Model (modular structure) 

Selector:               XPATH

Project Modules:        Helper --> 
                                helpers.py  (includes all common methods which are used in 'Pages')
                                        Designed Methods: -->  
                                                'go_to_page'
                                                'find_and_click'
                                                'find_and_send_keys'
                                                'find_all' 
                                                'find'       
                                drivers.py  (includes driver initilisation method)  
                                test_logger.py (includes method 'logger')                         
                        Pages --> 

                                favorites.py
                                        Designed Methods: -->      
                                                                                                                           
                                login.py 
                                        Designed Methods: -->
                                                'login_user'   

                                my_bag.py
                                        Designed Methods: -->
                                                'sum_of_item_prices_in_bag'
                                                'empty_bag'

                                search.py
                                         Designed Methods: -->
                                                                                      
                        Testdata --> 
                                test_data.py (includes test data, which are used in tests)

                        congif.py (includes configuration data)
Test Cases:                               
                        Tests: --> 
                               
                                'test_bag_functionality.py'
                                'test_bag_label.py'
                                'test_favorites.py'
                                'test_search.py'
                                                            
Log                     test_log.txt

Tests should be run in Python. 
