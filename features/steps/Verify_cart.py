from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input purse into search field')
def input_search(context,):
    search = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search.clear()
    search.send_keys('Purse')
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    sleep(1)

@when('Click on first item from the list')
def click_on_purse(context):
    context.driver.find_element(By.XPATH, "//a[@class='a-link-normal a-text-normal']").click()
    sleep(1)

@when('Add item to the Shopping Cart')
def add_item_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    sleep(1)


@then('Item is present in the Shopping cart')
def verify_item_is_added(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']/h1").text
    expected_text = "Added to Cart"
    assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'


