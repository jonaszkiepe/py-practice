import os

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_URL = "https://twitter.com/home?lang=en"
TWITTER_EMAIL = os.environ.get("email")
TWITTER_PASSWORD =os.environ.get("passw")

SPEED_TEST_URL = "https://www.speedtest.net/"

options = ChromeOptions()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot(Chrome):
    def __init__(self):
        super().__init__(options=options)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.get(SPEED_TEST_URL)
        sleep(1)

        cookie_accept = self.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_accept.click()
        sleep(1)

        start_test = self.find_element(By.XPATH, '//*[@id="container"]'
                                                 '/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_test.click()
        sleep(60)
        self.down = self.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                         'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/'
                                                         'div[1]/div/div[2]/span').text
        self.up = self.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]/'
                                                       'div[1]/div[2]/div/div[2]/span').text

    def complain(self):
        self.get(TWITTER_URL)
        sleep(3)

        sign_in = self.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div'
                                              '/div[3]/div[5]/a/div')
        sign_in.click()
        sleep(3)

        email = self.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                            'div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        sleep(2)
        next_btn = self.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                               'div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()
        sleep(3)
        # activity = self.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
        #                                        '/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        password = self.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                               'div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        log_in = self.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                                             '/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        log_in.click()
        sleep(10)

        content = self.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div'
                                              '[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/'
                                              'div/div/div/div/div/label/div[1]/div/'
                                              'div/div/div/div/div[2]/div/div/div/div')
        content.send_keys(f"Hey internet provides why is it that my "
                          f"{self.down}/down - {self.up}/speed is this when it's supposed "
                          f"to be {PROMISED_DOWN}/down and {PROMISED_UP}/up")

        post = self.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]'
                                           '/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/'
                                           'span/span')
        post.click()


complainer = InternetSpeedTwitterBot()

complainer.get_internet_speed()

if int(complainer.down) < PROMISED_DOWN or int(complainer.up) < PROMISED_UP:
    complainer.complain()  # :(!!!
