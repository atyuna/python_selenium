from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com/my-account/")

u_name = driver.find_element(By.ID, "username")
u_name.send_keys("admin")
# u_name.send_keys(Keys.TAB)
pass_field = driver.find_element(By.ID,"password")
pass_field.send_keys("password")


submit_button = driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
submit_button.click()


# 2 import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()

# driver.get("http://demostore.supersqa.com/")

# search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
# search_field.send_keys("hoodie")
# time.sleep(3)
# search_field.send_keys(Keys.ENTER)
