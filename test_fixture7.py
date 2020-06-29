import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language')
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        link = f"http://selenium1py.pythonanywhere.com/{accept-language: ru, en}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза

    #def test_guest_should_see_navbar_element(self, browser, language):
        # этот тест тоже запустится дважды