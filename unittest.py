import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        required_input_labels = ['First name*', 'Last name*', 'Email*']
        for input_label in required_input_labels:
            element = browser.find_element(By.XPATH, f"//label[text()='{input_label}']/following-sibling::input[@required]")
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Регистрация первой страницы не пройденна")

        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        required_input_labels = ['First name*', 'Last name*', 'Email*']
        for input_label in required_input_labels:
            element = browser.find_element(By.XPATH, f"//label[text()='{input_label}']/following-sibling::input[@required]")
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Регистрация второй страницы не пройденна")

        
if __name__ == "__main__":
    unittest.main()