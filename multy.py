import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--window-size=1920,1080")
driver_1 = webdriver.Chrome(options=options)

link = ("https://hyperskill.org/login")

LOGIN_FIELD = (By.XPATH, "//input[@type='email']")
PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
SIGN_IN = (By.XPATH, "//button[@type='submit']")

driver_1.get(link)
driver_1.find_element(*LOGIN_FIELD).send_keys("alekseik@ya.ru")
driver_1.find_element(*PASSWORD_FIELD).send_keys("Qwerty132!")
driver_1.find_element(*SIGN_IN).click()
time.sleep(5)
driver_1.close()


driver_2 = webdriver.Chrome(options=options)

driver_2.get(link)
time.sleep(5)
