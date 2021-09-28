import os

from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    textfields = browser.find_elements_by_css_selector('.form-control')
    for tf in textfields:
        tf.send_keys("WTF")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector("#file").send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
