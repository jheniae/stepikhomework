import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, 'price'),"100"))
    message=browser.find_element_by_id('book').click()
    # assert "successful" in message.text
    x_element = browser.find_element_by_css_selector("#input_value").text
    y = calc(x_element)
    input1 = browser.find_element_by_css_selector("#answer").send_keys(y)
    button = browser.find_element_by_css_selector("#solve").click()
finally:
    time.sleep(30)
    browser.quit()
