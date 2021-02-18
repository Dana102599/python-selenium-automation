from selenium.webdriver.common.by import By
from behave import given, when, then


Color_selection = (By.CSS_SELECTOR, "#variation_color_name li")
Selected_Colors = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product page')
def open_BestSellers(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')

@then('Verify user can click through colors')
def verify_color_selection(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage','Vintage Light Wash', 'Washed Black']
    colors = context.driver.find_elements(*Color_selection)

    for i in range(len(colors)):
     colors[i].click()
     selected_color = context.driver.find_element(*Selected_Colors).text
     assert expected_colors[i] == selected_color,  f'Expected {expected_colors[i]} but got {selected_color}'