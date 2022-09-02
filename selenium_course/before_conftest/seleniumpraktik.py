from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    # Ваш код, который заполняет обязательные поля
    inpute = browser.find_element(By.CSS_SELECTOR, ".first_block")
    input_first = inpute.find_element(By.CSS_SELECTOR, ".first" )
    input_first.send_keys("debil")

    input_second = inpute.find_element(By.CSS_SELECTOR, ".second" )
    input_second.send_keys("debilovich")

    input_third = inpute.find_element(By.CSS_SELECTOR, ".third")
    input_third.send_keys("debilov")
    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()