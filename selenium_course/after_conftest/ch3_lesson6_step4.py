from tkinter import Button
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")


links = ['http://stepik.org/lesson/236895/step/1']
#,'https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1','https://stepik.org/lesson/236899/step/1','https://stepik.org/lesson/236903/step/1','https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1']

answer = math.log(int(time.time()))

@pytest.mark.parametrize('links', links)
def test_guest_should_see_login_link(browser, links):
    link = f"{links}"
    browser.get(link)
    textarea = browser.find_element(By.CSS_SELECTOR, "#ember87")
    textarea.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
