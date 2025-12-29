import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.switch_to.new_window("window")  # window/tab
time.sleep(2)

driver.get("https://ya.ru")
time.sleep(2)

# FOR_BUSINES = (By.XPATH, "//a[text()=' For Business ']")
# START_FREE = (By.XPATH, "//div[text()='Start a free trial']")

# driver.get("https://hyperskill.org/courses")
# time.sleep(5)

# windows = driver.window_handles

# driver.switch_to.window(windows[1])

# driver.get("https://ya.ru")
# time.sleep(2)
# driver.find_element(*FOR_BUSINES).click()
# time.sleep(2)

# TABS = driver.window_handles
# driver.switch_to.window(TABS[1])

# driver.find_element(*START_FREE).click()
# time.sleep(2)
