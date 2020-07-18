from selenium import webdriver
import time


##This is the mail website. 
url = 'https://outlook.live.com/owa/'

driver = webdriver.Firefox('myproject/geckodriver')

driver.get(url)

