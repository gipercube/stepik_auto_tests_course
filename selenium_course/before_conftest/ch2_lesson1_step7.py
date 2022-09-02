import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    # x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    checkboxrobot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkboxrobot.click()
    radiorobot = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiorobot.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

    #28.884278416061896