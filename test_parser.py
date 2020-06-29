link = "http://selenium1py.pythonanywhere.com/"


def test_g(browser):
    
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")