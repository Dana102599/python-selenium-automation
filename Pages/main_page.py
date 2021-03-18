from Pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class MainPage(Page):
    Search_Field = (By.ID, 'twotabsearchtextbox')
    Search_Icon = (By.ID, 'nav-search-submit-button')
    Search_dropdown_btn = (By.CSS_SELECTOR, ".nav-search-dropdown")
    SELECTED_DEPARTMENT_CATEGORYS = (By.CSS_SELECTOR, "#nav-subnav[data-category='electronics']")

    def  open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self):
        self.input_text('watch', *self.Search_Field)

    def click_search_icon(self):
        self.click(*self.Search_Icon)

    def select_department(self):
        select = Select(self.find_element(*self.Search_dropdown_btn))
        select.select_by_value('search-alias=electronics')
        from time import sleep
        sleep(4)

    def verify_department(self):
        self.wait_for_element_appear(*self.SELECTED_DEPARTMENT_CATEGORYS)

