from Pages.base_page import Page
from selenium.webdriver.common.by import By

class AddProductToCart(Page):
    Search_field = (By.ID, 'twotabsearchtextbox')
    Search_icon = (By.ID, 'nav-search-submit-button')
    Cart_Icon = (By.ID, 'nav-cart-count-container')
    First_item = (By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    Add_item_to_cart =(By.ID, "add-to-cart-button")
    Verify_item_added = (By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']/h1")

    def  open_amazon_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self):
        self.input_text('Purse', *self.Search_field)

    def click_search_icon(self):
        self.click(*self.Search_icon)

    def click_first_item(self):
        self.click(*self.First_item)

    def add_item_to_cart(self):
        self.click(*self.Add_item_to_cart)

    def verify_item_is_added(self):
        actual_text = self.driver.find_element(*self.Verify_item_added).text
        expected_text = "Added to Cart"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"