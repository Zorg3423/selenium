from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Обязательные поля (уникальные селекторы)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("test@test.com")

    # Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверка успешной регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    browser.quit()
