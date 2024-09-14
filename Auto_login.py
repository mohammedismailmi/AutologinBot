import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def startBot(username, password, url):
    path = "C:\\Users\\DELLL\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

    service = Service(path)

    driver = webdriver.Chrome(service= service)

    print("Opening the login page...")
    driver.get(url)

    print("Filling the username...")
    driver.find_element(By.ID, 'login_field').send_keys(username)

    print("Filling the password...")
    driver.find_element(By.ID, 'password').send_keys(password)

    print("Clicking the login button...")
    driver.find_element(By.NAME, 'commit').click()

    print("Login process  initiated...")
    time.sleep(5)

    driver.quit()


username = "Ismail1234"
password = "12345"
url = "https://github.com/login"
startBot(username, password, url)

