from selenium.webdriver.common.by import By
from Testdata import test_data


search_field = (By.XPATH, "//input[@id='searchAll']")
shop_by_price = (By.XPATH, "//button[text()='Shop By Price']")
under_50_link = (By.XPATH, "//a[text()='$50 and Under']")
brand_check_box = (By.XPATH, f"//span[text()='{test_data.brand_name}']")
product_count_text = (By.XPATH, "//span[text()=12]")
found_result = (By.XPATH, "//a[@class='Wj-z']")
items_found_text = (By.XPATH, "//span[@class='Su-z']")
search_box_xpath = "//input[@id='searchAll']"
