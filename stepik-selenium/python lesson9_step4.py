from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    textfield = browser.find_element_by_css_selector('#answer')
    textfield.send_keys(str(calc(int(browser.find_element_by_css_selector('#input_value').text))))
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
