import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/lt/login")

EMAIL = (By.XPATH, "//input[@id='login_email']")
PASSWORD = (By.XPATH, "//input[@id='password']")
SUBMIT = (By.XPATH, "//button[@title='Submit']")
CHECHBOX = (By.XPATH, "//input[@id='gdpr_checkbox']")

driver.find_element(*EMAIL).send_keys("1234")
time.sleep(2)

driver.find_element(*PASSWORD).send_keys("1234")
time.sleep(2)

driver.find_element(*CHECHBOX).click()
time.sleep(2)

driver.find_element(*SUBMIT).click()
time.sleep(2)
