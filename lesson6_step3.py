from selenium import webdriver
import time
import math
try:
    link = 'http://suninjuly.github.io/find_xpath_form'
    browser = webdriver.Chrome()
    browser.get(link)
    # link2.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('.//*[@type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
