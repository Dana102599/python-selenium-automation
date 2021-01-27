from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/kusia/automation/python-selenium-automation/chromedriver')


driver.get("https://www.amazon.com/gp/help/customer/display.html")
driver.find_element(By.ID, "helpsearch").send_keys("Cancel order")

sleep(5)
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-search']").click()

actual_text = driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=hp_gt_recncl?nodeId=201976060']" ).text
expected_text = "Cancel Items or Orders"
assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'

driver.quit()