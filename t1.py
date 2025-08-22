import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.google.com")

while True:
    current_url = driver.current_url
    print(datetime.now(), current_url)
        
    if "youtube" in current_url:
        f = open("C:/Users/user/OneDrive/Desktop/t1/log.txt", "r")
        contents = f.readlines()
        f.close()

        number = int(contents[0].strip().split(':')[-1])
        txt = f"num:{number+1}\n"
        for ind in range(len(contents)):
            if ind: txt+=contents[ind]
            
        f = open("C:/Users/user/OneDrive/Desktop/t1/log.txt", "w")
        f.write(txt)

        driver.quit()
        break
        
    time.sleep(3)
