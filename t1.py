import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.google.com")
current_url = driver.current_url

try:
    while True:
        print(current_url)
        time.sleep(10)
except KeyboardInterrupt:
    driver.quit()
