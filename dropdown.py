import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT = (By.XPATH, "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT))

all_options = DROPDOWN.options
# DROPDOWN.select_by_value("2")
# DROPDOWN.select_by_visible_text("Option 1")
# DROPDOWN.select_by_index(1)


# for option in all_options:
#     time.sleep(1)
#     if "Option 2" in option.text:
#         print("Option aviable")
#     DROPDOWN.select_by_visible_text(option.text)

# for option in all_options:
#     time.sleep(1)
#     DROPDOWN.select_by_index(all_options.index(option))

# for option in all_options:
#     time.sleep(1)
#     DROPDOWN.select_by_value(option.get_attribute("value"))
