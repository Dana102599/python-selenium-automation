
import click as click
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/kusia/automation/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
#driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").click()
driver.find_element(By.ID, "continue").click()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, "a-expander-prompt").click()
#driver.find_element(By.ID, "auth-fpp-link-bottom").click()
#driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']").click
#driver.find_element(By.ID,"ap-other-signin-issues-link").click()
#driver.find_element(By.ID,"createAccountSubmit").click()
#driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']").click()
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']").click()