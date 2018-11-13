

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/python/chromedriver.exe")


def _community():ww


driver.get('https://us.toluna.com/#/')

element = driver.find_element_by_xpath(xpath='//*[@id="jsddm"]/li[1]/a/span[2]')
element.click()

element = driver.find_element_by_xpath(xpath='//*[@id="jsddm"]/li[1]/div/a[2]')
element.click()
