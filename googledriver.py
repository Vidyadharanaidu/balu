from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\Vidyadhar\\Desktop\\chromedriver.exe')
driver.get('https://www.google.com/')
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='gbwa']/div[1]/a").click()
time.sleep(3)
driver.find_element_by_id('gb49').click()
time.sleep(3)
driver.find_element_by_link_text('Go to Google Drive').click()
time.sleep(3)
driver.find_element_by_id('identifierId').send_keys('vidyadharkongara@gmail.com')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(3)
driver.find_element_by_name('password').send_keys('9963535610')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div/div[1]/div/div/div[3]/div[1]/div/button[1]/div[2]').click()
time.sleep(2)
element=driver.find_element_by_link_text('Folder').click()
hover=ActionChains(driver).move_to_element(element).click()
hover.perform()

