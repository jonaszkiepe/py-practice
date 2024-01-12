import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

FORM_URL = ""

ZILLOW_URL = ("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible"
              "%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.84119643164063%2C%22east%22%3A-122.0378211875%2C%22"
              "south%22%3A37.54617377277722%2C%22north%22%3A37.99233820530415%7D%2C%22mapZoom%22%3A11%2C%22filterState"
              "%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo"
              "%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3A"
              "false%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price"
              "%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000"
              "%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D")

HEADERS = {
}

content = requests.get(ZILLOW_URL, headers=HEADERS)
soup = BeautifulSoup(content.text, "html.parser")
link_elements = soup.select("[data-test='property-card-link']")
address_elements = soup.select("[data-test='property-card-addr']")
price_elements = soup.select("[data-test='property-card-price']")
addresses = [address.text for address in address_elements]
prices = [price.text for price in price_elements]
links = [link["href"] for link in link_elements[::2]]
total = len(prices) + len(addresses) + len(links)

form_entrys = {}
if total/3 == len(prices):
    for _ in range(int(total/3)):
        form_entrys[_] = {
            "price": prices[_].split("+")[0],
            "link": links[_],
            "address": addresses[_],
        }

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

for _ in range(len(form_entrys)):
    driver.get(FORM_URL)
    form_elements = driver.find_elements(By.CSS_SELECTOR, "input[class='whsOnd zHQkBf']")
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    form_elements[0].send_keys(form_entrys[_]["address"])
    form_elements[1].send_keys(form_entrys[_]["link"])
    form_elements[2].send_keys(form_entrys[_]["price"])
    submit_button.click()
