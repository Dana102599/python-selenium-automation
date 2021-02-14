from selenium.webdriver.common.by import By
from behave import given, when, then


links = (By.XPATH, "//div[@id='zg_tabs']//li")
@given('Open Amazon BestSellers page')
def open_BestSellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_links} links')
def verify_links(context, expected_links):
    actual_links = context.driver.find_elements(*links)
    assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but we see {len(actual_links)}'