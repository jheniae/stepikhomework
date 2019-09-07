from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure").get_attribute('valuex')
    y = calc(x_element)
    input1 = browser.find_element_by_css_selector("#answer").send_keys(y)
    checkbox_click = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox_click.click()
    radiobox_click = browser.find_element_by_css_selector("#robotsRule")
    radiobox_click.click()
    button = browser.find_element_by_css_selector(".btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
