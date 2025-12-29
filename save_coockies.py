import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# options = Options()
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--user-agent=Automation")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)


driver.get("https://www.freeconferencecall.com/global/lt/login")

LOGIN_FIELD = (By.XPATH, "//input[@id='login_email']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
CHECKBOX_BUTTON = (By.XPATH, "//input[@id='gdpr_checkbox']")
SUBMIT_BUTTON = (By.XPATH, "//button[@id='loginformsubmit']")

driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*CHECKBOX_BUTTON).click()
driver.find_element(*SUBMIT_BUTTON).click()

pickle.dump(driver.get_cookies(), open(
    os.getcwd()+"\\cookies\\cookie.pkl", "wb"))
