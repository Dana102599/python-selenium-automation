from behave import given, when, then



@given('Open page')
def open_product_page(context):
    context.app.product_pages.open_product()


@when('Hover over New Arrivals link')
def hover_add_to_cart_btn(context):
    context.app.product_pages.hover_new_arrivals()


@then('Verify user sees the deals')
def verify_deals_shown(context):
    context.app.product_pages.verify_deals_shown()


