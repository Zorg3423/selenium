from selenium import webdriver
import math
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": fr"{os.getcwd()}\downloads"
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# driver.implicitly_wait(5)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# link = "https://suninjuly.github.io/math.html"
# link = "https://suninjuly.github.io/get_attribute.html"
# link = "https://suninjuly.github.io/selects1.html"
# link = "https://suninjuly.github.io/selects2.html"
# link = "https://suninjuly.github.io/execute_script.html"
# link = "https://suninjuly.github.io/file_input.html"
# link = "https://suninjuly.github.io/alert_accept.html"
# link = "https://suninjuly.github.io/redirect_accept.html"
# link = "https://suninjuly.github.io/cats.html"
# link = "http://suninjuly.github.io/wait2.html"
link = "http://suninjuly.github.io/explicit_wait2.html"

driver.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
# number_element = str(math.ceil(math.pow(math.pi, math.e)*10000))
# driver.find_element(By.LINK_TEXT, f"{number_element}").click()

# try:
#     input1 = driver.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = driver.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = driver.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = driver.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = driver.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     driver.quit()
# try:
#     elements = driver.find_elements(By.XPATH, "//input")
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = driver.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     driver.quit()


# не забываем оставить пустую строку в конце файла
# try:
#     robot_checkbox = (By.CSS_SELECTOR, "#robotCheckbox")
#     robot_rule = (By.CSS_SELECTOR, "#robotsRule")
#     SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
#     x_element = (By.CSS_SELECTOR, "#input_value")
#     input = (By.XPATH, "//input[@id='answer']")
#     x = driver.find_element(*x_element).text
#     y = calc(x)
#     driver.find_element(*input).send_keys(y)
#     driver.find_element(*robot_checkbox).click()
#     driver.find_element(*robot_rule).click()
#     driver.find_element(*SUBMIT).click()
# finally:
#     time.sleep(5)
#     driver.quit()
# try:
#     x_element = driver.find_element(By.CSS_SELECTOR, "[id='treasure']")
#     robot_checkbox = (By.CSS_SELECTOR, "#robotCheckbox")
#     robot_rule = (By.CSS_SELECTOR, "#robotsRule")
#     SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
#     input = (By.CSS_SELECTOR, "[id='answer']")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#     driver.find_element(*input).send_keys(y)
#     driver.find_element(*robot_checkbox).click()
#     driver.find_element(*robot_rule).click()
#     driver.find_element(*SUBMIT).click()
# finally:
#     time.sleep(3)
#     driver.quit


# # # SELECT WITH SUM # # #
# text = driver.find_element(By.TAG_NAME, "h2").text

# nums = [int(s) for s in text.split() if s.isdigit()]
# result = nums[0]+nums[1]
# select = Select(driver.find_element(By.ID, "dropdown"))
# select.select_by_value(str(result))

# button = driver.find_element(By.TAG_NAME, "button")
# button.click()
# time.sleep(5)

# driver.execute_script("alert('Robots at work');")
# driver.execute_script("document.title='Script executing';")
# driver.execute_script("document.title='Script executing';alert('Robots at work');")

# # # Scroll BY # # #

# x_element = driver.find_element(By.CSS_SELECTOR, "[id='input_value']").text
# x = calc(x_element)
# answer_input = driver.find_element(By.ID, 'answer')
# robot_chechbox = driver.find_element(By.ID, 'robotCheckbox')
# robot_rule = driver.find_element(By.ID, 'robotsRule')
# submit = driver.find_element(By.TAG_NAME, "button")

# driver.execute_script("window.scrollBy(0, 100);")
# answer_input.send_keys(x)
# robot_chechbox.click()
# robot_rule.click()
# submit.click()


# time.sleep(5)

# # # Download_file # # #

# first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
# last_name = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
# email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
# submit = driver.find_element(By.TAG_NAME, "button")

# first_name.send_keys("name")
# last_name.send_keys("lastname")
# email.send_keys("email@il")

# driver.find_element(By.ID, "file").send_keys(
#     fr"{os.getcwd()}\downloads\validation-upload.txt")

# submit.click()
# time.sleep(5)


# # # alert # # #

# driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
# alert = driver.switch_to.alert
# alert.accept()
# x_element = driver.find_element(By.ID, "input_value").text
# input_answer = driver.find_element(By.ID, "answer")
# submit_button = driver.find_element(By.TAG_NAME, "button")

# x = calc(x_element)
# input_answer.send_keys(x)
# submit_button.click()

# time.sleep(5)


# # # window # # #

# driver.find_element(By.TAG_NAME, "button").click()

# windows = driver.window_handles
# driver.switch_to.window(windows[1])

#
# input_answer = driver.find_element(By.ID, "answer")
# submit_button = driver.find_element(By.TAG_NAME, "button")

# x = calc(x_element)
# input_answer.send_keys(x)
# submit_button.click()

# time.sleep(5)


# # # Implicit и Explicit Waits # # #

price = (By.CSS_SELECTOR, "[id='price']")
wait.until(EC.text_to_be_present_in_element(price, "$100"))
driver.find_element(By.ID, "book").click()

x_element = driver.find_element(By.ID, "input_value").text
input_answer = driver.find_element(By.ID, "answer")
submit_button = driver.find_element(By.ID, "solve")

x = calc(x_element)
input_answer.send_keys(x)
submit_button.click()

alert = wait.until(EC.alert_is_present())
alert_text = driver.switch_to.alert.text
code = alert_text.split(":")[-1].strip()
print(code)
alert.accept()
