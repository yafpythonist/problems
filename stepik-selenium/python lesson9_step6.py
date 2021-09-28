from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(2)
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    textfield = browser.find_element_by_css_selector('#answer')
    textfield.send_keys(str(calc(int(browser.find_element_by_css_selector('#input_value').text))))
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
