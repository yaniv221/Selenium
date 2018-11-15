
import ChromeWebDriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def _community():
    driver = webdriver.Chrome("C:/Users/yanivova/PycharmProjects/Web_Automation/chromedriver.exe")



    driver.get('https://us.toluna.com/Recent')

    element = driver.find_element_by_xpath(xpath='//*[@id="jsddm"]/li[1]/a/span[2]')
    element.click()

    driver.implicitly_wait(30)
    element = driver.find_element_by_xpath(xpath='//*[@id="jsddm"]/li[1]/div/a[2]')
    element.click()
if __name__== "__main__":
    _community()

