
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)   # checks every second, after 10 sec fails

driver.get('path')
my_image = driver.find_element(By.ID,'slow_image')
my_image.click()
