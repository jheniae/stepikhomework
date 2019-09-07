from selenium import webdriver
import time

try:
    link='http://suninjuly.github.io/registration2.html'
    browser=webdriver.Chrome()
    browser.get(link)
    name=browser.find_element_by_css_selector('.first_block>.first_class>input').send_keys("Tom")
    last_name=browser.find_element_by_css_selector('.first_block>.second_class>input').send_keys("Tomson")
    email = browser.find_element_by_css_selector('.first_block>.third_class>input').send_keys('test@test.cin')

    button=browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(1)
    welcome_text_elt=browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text()
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(19)
    browser.quit()