import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
 
def test_items(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    
    assert button == button, "there is no button"
