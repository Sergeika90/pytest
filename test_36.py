import pytest
from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestMainPage():

    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
    def test_link(self, browser, link):
        link = f"{link}"
        browser.get(link)
        browser.implicitly_wait(15)
        #input = WebDriverWait(browser, 5).until(
        #EC.element_to_be_able((By.ID, "ember120"))
    #)
        input = browser.find_element_by_tag_name("textarea")
        answer = str(math.log(int(time.time())))
        input.send_keys(answer)
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        actual_result = browser.find_element_by_css_selector(".smart-hints__hint")
        assert actual_result.text == "Correct!", "uncorrect 6Jl9lTb"
