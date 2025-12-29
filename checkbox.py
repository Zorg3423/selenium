import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

RADIO_YES_STATUS = (By.XPATH, "//input[@id='yesRadio']")
RADIO_NO_STATUS = (By.XPATH, "//input[@id='noRadio']")
RADIO_YES = (By.XPATH, "//label[@for='yesRadio']")
RADIO_NO = (By.XPATH, "//label[@for='noRadio]")

driver.get("https://demoqa.com/radio-button")
print(driver.find_element(*RADIO_NO_STATUS).is_enabled())
print(driver.find_element(*RADIO_YES_STATUS).is_selected())
driver.find_element(*RADIO_YES).click()
print(driver.find_element(*RADIO_YES_STATUS).is_selected())

time.sleep(3)
