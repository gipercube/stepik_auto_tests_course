from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
    input_first.send_keys("first name")
    input_second = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
    input_second.send_keys("last name")
    input_third = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
    input_third.send_keys("email@mail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()