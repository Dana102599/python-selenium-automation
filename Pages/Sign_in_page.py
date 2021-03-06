from Pages.base_page import Page
from selenium.webdriver.common.by import By

class SignIn(Page):

    Orders_link = (By.ID, 'nav-orders')
    Verify_SignIn_page = (By.CSS_SELECTOR, "div.a-box-inner h1")

    def  open_sign_in_page(self):
        self.open_url('https://www.amazon.com/')

    def click_order_link(self):
        self.click(*self.Orders_link)

    def verify_sign_in_page(self):
        actual_text = self.driver.find_element(*self.Verify_SignIn_page).text
        expected_text = 'Sign-In'
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"




