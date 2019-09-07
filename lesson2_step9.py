from selenium import webdriver
import time
import math
import os
link = "http://suninjuly.github.io/file_input.html"

cur_dir = os.getcwd()
file_path = os.path.join(cur_dir, 'test.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    for element in (['firstname', 'lastname', 'email']):
        browser.find_element_by_name(element).send_keys("wsdada")
    file = browser.find_element_by_id('file').send_keys(file_path)
    button = browser.find_element_by_class_name('btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()
