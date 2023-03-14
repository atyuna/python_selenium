
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/shop/')

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()
# pdb.set_trace()   # to do a breakpoint; c - to continue;
driver.get("http://demostore.supersqa.com/my-account/")
pdb.set_trace()
u_name = driver.find_element(By.ID, "username")
u_name.send_keys("Anya")

# NOTE: to find all available methods just do dir(<variable>)
# Example: dir(cart)  
# Example: dir(driver)
