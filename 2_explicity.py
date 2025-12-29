import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

ENABLE_BUTTON = (By.XPATH, "//button[text()='Enable']")
TEXT_INPUT = (By.XPATH, "//input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable(TEXT_INPUT)).send_keys('ALO')
time.sleep(2)
wait.until(EC.text_to_be_present_in_element_value(TEXT_INPUT, "ALO"))
time.sleep(2)

print("EBAT RABOTAET")
