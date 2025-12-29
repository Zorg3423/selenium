import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": fr"{os.getcwd()}\downloads"
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")

ELEMENT = (By.XPATH, "//a")
time.sleep(3)

driver.find_elements(*ELEMENT)[3].click()
time.sleep(5)
