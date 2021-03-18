from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazoni page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()


@when('Select electronics department')
def select_department(context):
    context.app.main_page.select_department()


@when('Input Watches into Amazon search field')
def input_amazon_search(context):
    context.app.main_page.input_amazon_search()

@when('Input Watch into Amazon search field')
def input_watch(context):
    context.app.main_page.input_amazon_search()


@when('Click on Amazon search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@then('Product results for Watches are shown on Amazon')
def verify_products_are_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"watches"'

    assert  expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Verify Electronics department is selected')
def verify_department(context):
    context.app.main_page.verify_department()