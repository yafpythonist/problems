from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value = sum((int(element.text) for element in browser.find_elements_by_css_selector('[id^="num"]')))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(value))
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
