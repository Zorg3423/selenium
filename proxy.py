import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "37.19.220.129:8443"

options = Options()
options.add_argument(f"--proxy=server={PROXY_SERVER}")
driver = webdriver.Chrome(options=options)

driver.get("https://2ip.ru/")  # 45.132.206.215

time.sleep(3)
