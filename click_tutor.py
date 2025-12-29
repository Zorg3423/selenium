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

email_field = (driver.find_element(*EMAIL))
password_field = driver.find_element(*PASSWORD)

email_field.clear()
password_field.clear()

email_field.send_keys("email")
password_field.send_keys("password")

print(email_field.get_attribute("value"))
print(password_field.get_attribute("value"))
