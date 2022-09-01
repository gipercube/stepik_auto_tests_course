import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
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

    #28.883328241138866