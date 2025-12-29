import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/select-menu")

MULTI_SELECT = (By.XPATH, "//input[@id='react-select-4-input']")

driver.find_element(*MULTI_SELECT).send_keys("Gre")
time.sleep(2)
driver.find_element(*MULTI_SELECT).send_keys(Keys.TAB)
time.sleep(2)
driver.find_element(*MULTI_SELECT).send_keys("Bl")
time.sleep(2)
driver.find_element(*MULTI_SELECT).send_keys(Keys.TAB)
driver.find_element(*MULTI_SELECT).send_keys(Keys.TAB)
time.sleep(2)


# SELECT_ONE = (By.XPATH, "//div[@id='selectOne']")
# SELECT_OPTION = (By.XPATH, "//div[text()='Prof.']")
# time.sleep(2)


# driver.find_element(*SELECT_ONE).click()
# time.sleep(2)
# driver.find_element(*SELECT_OPTION).click()
# time.sleep(2)
# time.sleep(2)

# driver.find_element(*SELECT_KEY).send_keys("Ms.")
# driver.find_element(*SELECT_KEY).send_keys(Keys.ENTER)


# driver.find_element(*INPUT_KEY).send_keys("HELLO")
# time.sleep(2)

# driver.find_element(*INPUT_KEY).send_keys(Keys.CONTROL + "A")
# time.sleep(2)

# driver.find_element(*INPUT_KEY).send_keys(Keys.BACKSPACE)
# time.sleep(2)
