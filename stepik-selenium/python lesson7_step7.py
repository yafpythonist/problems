from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    textfield = browser.find_element_by_css_selector('#answer')
    textfield.send_keys(str(calc(browser.find_element_by_css_selector('#treasure').get_attribute('valuex'))))
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
