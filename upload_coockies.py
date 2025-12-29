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

driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"\\cookies\\cookie.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)
