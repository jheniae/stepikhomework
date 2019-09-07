import unittest
from selenium import webdriver
import time
link='http://suninjuly.github.io/registration2.html'
answer= "Congratulations! You have successfully registered!"
def input_data(link):

    try:
        browser=webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector('.first_block>.first_class>input').send_keys("Tom")
        browser.find_element_by_css_selector('.first_block>.second_class>input').send_keys("Tomson")
        browser.find_element_by_css_selector('.first_block>.third_class>input').send_keys('test@test.cin')

        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        welcome_text_elt=browser.find_element_by_tag_name("h1").text
        return welcome_text_elt
    finally:
        time.sleep(1
        )
        browser.quit()
class TestRegistrationForm(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(input_data('http://suninjuly.github.io/registration1.html'), answer, 'Yep' )


    def test_case2(self):
        self.assertEqual(input_data('http://suninjuly.github.io/registration2.html'), answer, 'Yep' )



if __name__ == '__main__':
    unittest.main()
