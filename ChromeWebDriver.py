import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/Users/yanivova/PycharmProjects/Web_Automation/chromedriver.exe")
driver.get("http://www.google.com/")

#open tab

# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
driver.get('https://us.toluna.com/#/')
# Make the tests..
driver.implicitly_wait(30)
element = driver.find_element_by_xpath(xpath='//*[@id="root"]/nav/div/div[2]/span/a/span[2]')
element.click()




