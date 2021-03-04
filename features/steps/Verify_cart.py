from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open Amazon page')
def open_amazon(context):
    context.app.add_product_to_cart.open_amazon_page()


@when('Input purse into search field')
def input_search(context,):
    context.app.add_product_to_cart.input_amazon_search()

@when('Click on search icon')
def click_search_icon(context):
    context.app.add_product_to_cart.click_search_icon()


@when('Click on first item from the list')
def click_on_purse(context):
    context.app.add_product_to_cart.click_first_item()


@when('Add item to the Shopping Cart')
def add_item_to_cart(context):
    context.app.add_product_to_cart.add_item_to_cart()
    

@then('Item is present in the Shopping cart')
def verify_item_is_added(context):
    context.app.add_product_to_cart.verify_item_is_added()


