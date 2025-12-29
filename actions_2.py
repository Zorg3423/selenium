import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
action = ActionChains(driver)

# COLLUM_A = (By.XPATH, "//div[@id='column-a']")
# COLLUM_B = (By.XPATH, "//div[@id='column-b']")
ITEM = (By.XPATH, "(//div[@class='grid__item'])[2]")
# setTimeout(function() { debugger; }, 5000);
SIDE_BAR = (By.XPATH, "(//div[@class='drop-area__item'])[3]")

# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

item = driver.find_element(*ITEM)
side_bar = driver.find_element(*SIDE_BAR)
# A = driver.find_element(*COLLUM_A)
# B = driver.find_element(*COLLUM_B)

# action.drag_and_drop(A, B).perform()
# time.sleep(2)

action.click_and_hold(item)  \
    .pause(2)  \
    .move_to_element(side_bar)  \
    .release()  \
    .perform()
time.sleep(2)
