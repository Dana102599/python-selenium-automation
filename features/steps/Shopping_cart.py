from behave import given, when, then


@given('Open Amazone page')
def open_amazon(context):
    context.app.Shopping_cart_page.open_amazon_page()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.Shopping_cart_page.click_cart_icon()


@then("Verify 'Your Shopping Cart is empty' text present")
def verify_cart_is_empty(context):
    context.app.Shopping_cart_page.verify_cart_is_empty()