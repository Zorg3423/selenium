import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
action = ActionChains(driver)

# LEFT_CLICK = (By.XPATH, "//button[@id='leftClick']")
# DOUBLE_CLICK = (By.XPATH, "//button[@id='doubleClick']")
# RIGHT_CLICK = (By.XPATH, "//button[@id='rightClick']")
# COLOR_BUTTON = (By.XPATH, "//button[@id='colorChangeOnHover']")
MAIN_2 = (By.XPATH, "//a[text()='Main Item 2']")
SUB_LIST = (By.XPATH, "//a[text()='SUB SUB LIST »']")

driver.get("https://demoqa.com/menu")

menu_main = driver.find_element(*MAIN_2)
sublist = driver.find_element(*SUB_LIST)
# left_button = driver.find_element(*LEFT_CLICK)
# double_button = driver.find_element(*DOUBLE_CLICK)
# right_button = driver.find_element(*RIGHT_CLICK)
# color_button = driver.find_element(*COLOR_BUTTON)

action.move_to_element(menu_main).pause(2).move_to_element(sublist).perform()
time.sleep(3)

# action.click(left_button).perform()
# action.double_click(double_button).perform()
# action.context_click(right_button).perform()
# action.click(left_button).double_click(
#     double_button).context_click(right_button).perform()
# action.move_to_element(color_button).perform()

time.sleep(3)
