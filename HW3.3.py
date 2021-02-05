from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/kusia/automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, "nav-cart").click()

actual_text = driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
expected_text = "Your Amazon Cart is empty"
assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'
driver.quit()