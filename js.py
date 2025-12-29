import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from scrolls import Scrolls


driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://seiyria.com/bootstrap-slider/")

EX_2 = (By.XPATH, "//h3[text()='Example 2: ']")

ex_2 = driver.find_element(*EX_2)
scrolls.scroll_to_element(ex_2)
time.sleep(2)
