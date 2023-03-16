
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

driver.find_element(By.LINK_TEXT,'Cart')

acc_el = driver.find_element(By.LINK_TEXT,'My account')
print(acc_el.text)

acc_el_p = driver.find_element(By.PARTIAL_LINK_TEXT,'account')
print(acc_el.text)

footer_el = driver.find_element(By.PARTIAL_LINK_TEXT,'WooCommerce')
print(footer_el.text)

# must be <a> tag or it will fail
