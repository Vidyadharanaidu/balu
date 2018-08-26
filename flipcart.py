from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome('C:\\Users\\Vidyadhar\\Desktop\\chromedriver.exe')
driver.get('https://www.flipkart.com/')
user='7019776334'
pin='9963535610'
time.sleep(8)
obj=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(user)
time.sleep(4)
obj1=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(pin)
time.sleep(4)
obj2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button').click()
driver.maximize_window()
obj3=driver.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').send_keys('Honor')
driver.implicitly_wait(4)
obj4=driver.find_element_by_class_name('vh79eN').click()
time.sleep(20)
obj5 = driver.find_elements_by_class_name("Zhf2z-")
print(len(obj5))
