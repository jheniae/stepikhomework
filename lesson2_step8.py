from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#input_value').text
    print(x_element)
    y = calc(x_element)
    input1 = browser.find_element_by_css_selector("#answer").send_keys(y)
    button = browser.find_element_by_css_selector(".btn-primary")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    checkbox_click = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox_click.click()
    radiobox_click = browser.find_element_by_css_selector("#robotsRule")
    radiobox_click.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
