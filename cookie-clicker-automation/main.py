from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
GAME_DURATION = 5  # minutes
BUY_TIMER = 5  # seconds

buy_delay = time() + BUY_TIMER
duration = time() + GAME_DURATION * 60

driver = webdriver.Chrome()
driver.get(URL)
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

while duration > time():
    if buy_delay <= time():
        upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
        for upgrade in upgrades[::-1]:
            if upgrade.get_attribute("class") == "":
                upgrade.click()
                break
        buy_delay = time() + BUY_TIMER
    cookie.click()
