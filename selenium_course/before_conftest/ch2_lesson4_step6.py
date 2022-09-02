from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.ID, "button")
    button.click()


finally:
    time.sleep(7)
    browser.quit()

    #28.973702190494684