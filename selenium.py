import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get('http://google.com.br')
ele = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
ele.click()
ele.send_keys('Linux')
ele.send_keys(Keys.RETURN)
sleep(2)