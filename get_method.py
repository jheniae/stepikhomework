import time

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    driver =webdriver.Chrome()

    time.sleep(5)

    driver.get(link)
    time.sleep(5)
    button=driver.find_element(By.ID, "submit_button:")
    button.click()
finally:
    driver.quit()
# textarea.send_keys("get()")
# time.sleep(5)
# submit_button=driver.find_element_by_css_selector(".submit-submission")
# submit_button.click()
# time.sleep(5)
# driver.quit()