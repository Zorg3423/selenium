import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

CLICK_ME_ALERT = (By.XPATH, "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(CLICK_ME_ALERT)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert
time.sleep(3)

alert.send_keys("))))")
time.sleep(3)

alert.accept()
time.sleep(3)
