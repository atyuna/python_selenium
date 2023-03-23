from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = 'file:///Users/anna/Downloads/python_selenium_course_material%202/SELENIUM_SECTION/Drop_Down/drop_down_example.html'
driver.get(url)

# Option 1 is using the Select Class:
# my_dropdown = driver.find_element(By.ID, 'age-range-select')
# dropdown_obj = Select(my_dropdown)
# dropdown_obj.select_by_index(2)
# dropdown_obj.select_by_value('21-40')
# all_options = dropdown_obj.options
# for option in all_options:
#     print(option.text)
# import pdb; pdb.set_trace()

# Option 2
dropdown_button = driver.find_element(By.ID, 'dropdownMenuButton')
dropdown_button.click()
driver.implicitly_wait(3)   # checks every second, after 10 sec fails
my_option = dropdown_button.find_element(By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[2]/a')
my_option.click()

import pdb; pdb.set_trace()

