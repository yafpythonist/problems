from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    textfield = browser.find_element_by_css_selector('#answer')
    textfield.send_keys(str(calc(int(browser.find_element_by_css_selector('#input_value').text))))
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
