from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then

Amazon_applications= (By.XPATH, "//a[@href='https://www.amazon.com/gp/feature.html?docId=1000625601']")
Amazon_new_page = (By.CSS_SELECTOR, ".a-column  p")

@given("Open Amazon T&C page")
def open_amazon_TC_page(context):
 context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Amazon applications link")
def click_on_Amazon_applications(context):
    context.driver.find_element(*Amazon_applications).click()




@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then("Amazon app page is opened")
def verify_page_is_open(context):
    actual_text = context.driver.find_element(*Amazon_new_page).text
    expected_text = "Download the app today!"
    assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'


@then("User can close new window and switch back to original")
def close_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)