from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/kusia/automation/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
driver.find_element(By.ID, "createAccountSubmit" ).click()
#driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']").click()
#driver.find_element(By.CSS_SELECTOR, 'div.a-box-inner h1')
#driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
#driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name.a-input-text')
#driver.find_element(By.NAME, "password")
#driver.find_element(By.XPATH, "//div[@class='a-alert-content']")
#driver.find_element(By.CSS_SELECTOR, "input#ap_password_check.a-form-normal")
#driver.find_element(By.ID, "continue").click()
#driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_privacy_notice')]").click()
#driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_condition_of_use')]").click()
driver.find_element(By.LINK_TEXT, "Sign-In").click()
driver.quit()