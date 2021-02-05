from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when('Input Cancel Order into Amazon Search Help Library field')
def input_amazon_help_search(context):
    search_field = context.driver.find_element(By.ID, "helpsearch")
    search_field.send_keys('Cancel order', Keys.ENTER)


@then('Verify that Cancel Items or Orders text is present')
def verify_text_is_present(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_text = "Cancel Items or Orders"
    assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'


