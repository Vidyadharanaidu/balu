from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\Vidyadhar\\Desktop\\chromedriver.exe')
driver.get('https://www.gmail.com/')
time.sleep(5)
obj=driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('vidyadharkongara@gmail.com')
time.sleep(4)
obj=driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(3)
obj=driver.find_element_by_xpath('//input[@type="password"]').send_keys('9963535610')

#//input[@type="email"]