
from selenium.webdriver.common.by import By
from behave import given, when, then



@given("Open Amazon page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Click on the cart icon")
def click_on_cart(context):
    cart_icon = context.driver.find_element(By.ID, "nav-cart")
    cart_icon.click()

@then("Verifies that Your Shopping Cart is Empty")
def verify_text_is_present(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = "Your Amazon Cart is empty"
    assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'
