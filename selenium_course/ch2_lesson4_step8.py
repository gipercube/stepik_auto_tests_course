from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

book_price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button_book = browser.find_element(By.ID, "book")
button_book.click()
x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()
