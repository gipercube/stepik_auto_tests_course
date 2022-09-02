from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    # x = x_element.text
    y = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    print("x = ", x)
    print("y = ", y)
    sum = x + y
    print("sum = ", sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

    #28.884278416061896