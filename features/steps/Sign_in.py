from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazonu page')
def open_amazon(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Click Amazon Orders link')
def click_order_link(context):
    context.app.sign_in_page.click_order_link()


@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()
