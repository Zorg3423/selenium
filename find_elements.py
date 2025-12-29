import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses")

len_elements = len(driver.find_elements(By.CLASS_NAME, "nav-link"))
print(len_elements)
driver.find_elements(By.CLASS_NAME, "nav-link")[3].click()
