import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def answer()
answer = math.log(int(time.time()))
total = []

link1 = "https://stepik.org/lesson/236895/step/1"
link2 = 'https://stepik.org/lesson/236896/step/1'
link3 = 'https://stepik.org/lesson/236897/step/1'
link4 = 'https://stepik.org/lesson/236898/step/1'
link5 = 'https://stepik.org/lesson/236899/step/1'
link6 = 'https://stepik.org/lesson/236903/step/1'
link7 = 'https://stepik.org/lesson/236904/step/1'
link8 = 'https://stepik.org/lesson/236905/step/1'


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    time.sleep(3)
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link1)

        user_login = browser.find_element(By.XPATH, '//*[@id="ember92"]')
        user_login.send_keys(answer)

        p1 = browser.find_element(By.XPATH, '//*[@id="ember108"]/p')
        p1 = p1.text

        if p1 != 'Correct'


        user_pass = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        user_pass.send_keys('230541236Ss')

        button1 = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button')
        button1.click()


        time.sleep(3)


