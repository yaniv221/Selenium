import time
from selenium import webdriver
from After_login import  _community
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/python/chromedriver.exe")
driver.get("http://www.google.com/")

#open tab

# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
driver.get('https://us.toluna.com/#/')
# Make the tests..
driver.implicitly_wait(30)
element = driver.find_element_by_xpath(xpath='//*[@id="root"]/nav/div/div[2]/span/a/span[2]')
element.click()

inputElement = driver.find_element_by_id(id_='Username')
inputElement.send_keys('yan257')

inputElement = driver.find_element_by_id(id_='Password')
inputElement.send_keys('adinoa02')

element = driver.find_element_by_xpath(xpath='//html/body/div[6]/div[2]/div/div/div[2]/div/button')
element.click()

driver.implicitly_wait(99)














