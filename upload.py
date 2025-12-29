import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(3)

driver.find_element(
    By.XPATH, "//input[@type='file']").send_keys(fr"{os.getcwd()}\downloads\screen.png")

time.sleep(3)
