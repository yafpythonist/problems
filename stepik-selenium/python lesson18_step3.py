import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('task', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_alien_messages(browser, task):
    link = f"https://stepik.org/lesson/236{task}/step/1"
    browser.get(link)
    browser.implicitly_wait(15)
    browser.find_element_by_css_selector("textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission").click()
    hint_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert hint_text=="Correct!", f"Got {hint_text}"
