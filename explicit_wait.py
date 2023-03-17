from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get('path')

# my_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.ID,'slow_image'))

my_image = wait.until(EC.visibility_of_element_located((By.ID, 'slow_image')))

print("Image found")

# NOTE : do not mix implicit and explicit waits in the same script or test
# it's recommended to use explicit wait for the most part.
