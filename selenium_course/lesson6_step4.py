from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# link1 = "http://suninjuly.github.io/simple_form_find_task.html"
# link2 = "http://suninjuly.github.io/find_link_text"
linkxpath = "http://suninjuly.github.io/find_xpath_form"

# strlink = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(linkxpath)

    # input0 = browser.find_element(By.PARTIAL_LINK_TEXT, strlink)
    # input0.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    input5 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    input5.click()

finally:
    time.sleep(10)
    browser.quit()

    ## 22.32985530842168
    ## 25.22022919637429
    ## 25.27429721190174