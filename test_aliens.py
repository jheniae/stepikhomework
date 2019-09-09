import time, math
from selenium import webdriver
import pytest
answer = math.log(int(time.time()))
@pytest.fixture(scope='function')
def browser():
    print('\nStart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    time.sleep(3)
    browser.quit()


@pytest.mark.parametrize('page',[str(i) for i in [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]])
def test_aliens_messages(browser, page):
    link = f'https://stepik.org/lesson/{page}/step/1'
    browser.get(link)
    browser.implicitly_wait(2)
    browser.find_element_by_css_selector('.attempt-wrapper .autoresize-textarea, .attempt-wrapper .textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name('submit-submission').click()
    cor = browser.find_element_by_xpath('//pre').text
    assert cor == 'Correct!', \
        f'Wrong answer {cor}'
