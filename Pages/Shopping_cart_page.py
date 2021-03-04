from Pages.base_page import Page
from selenium.webdriver.common.by import By

class ShoppingCart(Page):

    Cart_Icon = (By.ID, 'nav-cart-count-container')
    Verify_Cart_is_Empty = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")

    def  open_amazon_page(self):
        self.open_url('https://www.amazon.com/')

    def click_cart_icon(self):
        self.click(*self.Cart_Icon)

    def verify_cart_is_empty(self):
        actual_text = self.driver.find_element(*self.Verify_Cart_is_Empty).text
        expected_text = "Your Amazon Cart is empty"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"