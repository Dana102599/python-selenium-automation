from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import Page

class ProductPage(Page):

    NEW_ARRIVALS = (By.XPATH, "//a[@href='/s/ref=sr_hi_2/?_encoding=UTF8&bbn=17020138011&ie=UTF8&qid=1498592471&rh=n%3A7141123011%2Cn%3A17020138011&ref_=sv_sl_6']")
    NEW_DEALS = (By.CSS_SELECTOR, ".mm-merch-panel")


    def open_product(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        from time import sleep
        sleep(5)

    def verify_deals_shown(self):
        self.wait_for_element_appear(*self.NEW_DEALS)
