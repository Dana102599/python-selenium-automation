from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/kusia/automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

driver.find_element(By.XPATH, "//span[@class='nav-cart-icon nav-sprite']").click()
actual_text = driver.find_element(By.ID, "sc-subtotal-label-buybox" ).text
expected_text = "Subtotal (1 item)"
assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'



driver.quit()