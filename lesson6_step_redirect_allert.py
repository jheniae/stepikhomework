from selenium import webdriver
import time
import math
link = 'http://suninjuly.github.io/redirect_accept.html'
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.window(browser.window_handles[1])
    magic_numer=browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(magic_numer))
    browser.find_element_by_class_name('btn-primary').click()
finally:
    time.sleep(30)
    browser.quit()
