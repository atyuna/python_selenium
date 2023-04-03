from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import time

url = "http://demostore.supersqa.com/my-account/"
email_field_id = "reg_email"
pasw_field_id = "reg_password"
logout_btn_css = "li[class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout'] a"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# go to url:
driver.get(url)

wait = WebDriverWait(driver, 10)

# wait for the email field to be visible
email_field = wait.until(EC.visibility_of_element_located((By.ID, email_field_id)))

# generate random email
letters = string.ascii_lowercase
rand_str = ''.join(random.choice(letters) for i in range(15))
random_email = rand_str + '@supersqa.com'

# type in the email field
email_field.send_keys(random_email)

# find password field and enter password
password_field = wait.until(EC.visibility_of_element_located((By.ID, pasw_field_id)))
password_field.send_keys('ANdhf34!))(#')

# wait for the register button to be clickable and click it
register_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')))
register_btn.click()

# wait for the page to redirect
time.sleep(10)
# do something on the redirected page

try:
    logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)
except:
    raise Exception("User not logged in after registration")


if logout_btn.is_displayed():
    print("PASS")
else:
    raise Exception("User not logged in after registration")
