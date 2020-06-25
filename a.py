import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("Smolensk@aa.ss")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
            
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected = "Congratulations! You have successfully registered!"

        self.assertEqual(expected, actual)
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("Smolensk@aa.ss")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected = "Congratulations! You have successfully registered!"

        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()