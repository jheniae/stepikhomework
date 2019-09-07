from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
url = 'http://suninjuly.github.io/selects2.html'

def calc(n1, n2):
    return int(n1)+int(n2)
try:
    browser = webdriver.Chrome()
    browser.get(url)
    n1 = browser.find_element_by_css_selector("#num1").text
    n2 = browser.find_element_by_css_selector("#num2").text
    select = Select(browser.find_element_by_tag_name('select'))
    print(n1, n2)
    print(calc(n1, n2))
    select.select_by_value(str(calc(n1, n2)))
    button = browser.find_element_by_css_selector(".btn-default").click()
finally:
    time.sleep(10)
    browser.quit()