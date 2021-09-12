from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    textfield = browser.find_element_by_css_selector('.form-control')
    textfield.send_keys(str(calc(browser.find_element_by_css_selector('#input_value').text)))
    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    browser.find_element_by_css_selector('[for="robotsRule"]').click()
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
