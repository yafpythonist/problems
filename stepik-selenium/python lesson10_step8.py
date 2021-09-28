from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("#book")
    button.click()
    textfield = browser.find_element_by_css_selector('#answer')
    textfield.send_keys(str(calc(int(browser.find_element_by_css_selector('#input_value').text))))
    # Отправляем заполненную форму
    browser.find_element_by_css_selector("#solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
