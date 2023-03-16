
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/shop/')
#  EXAMPLE: CSS SELECTOR
# cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart > li:nth-child(1) > a')
# cart.click()
# my_acc = driver.find_element(By.CSS_SELECTOR,'#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9')
# my_acc.click()

# time.sleep(3)
# driver.quit()

#  EXAMPLE: XPATH
# NOTE: xpath changes a lot, not recommended to use

cart = driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a')
time.sleep(3)
cart.click()
my_acc = driver.find_element(By.XPATH,'//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
my_acc.click()


# How to find css selector in Console:  $$('.nameoftheclass') or $$('nav.nameoftheclass')

# '.' is for class
# '#' is for id

# Example find the nav bar
# css using id = #site-navigation
# css using id = nav#site-navigation
# css using class = .main-navigation
# css using class = nav.main-navigation
