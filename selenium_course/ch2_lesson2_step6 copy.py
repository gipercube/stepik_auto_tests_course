from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    checkboxrobot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkboxrobot.click()
    radiorobot = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiorobot.click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()

    #28.884278416061896