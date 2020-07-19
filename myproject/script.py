from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


##This is the mail website. 
# url = 'https://outlook.live.com/owa/'
url = 'https://outlook.live.com/owa/?nlp=1&signup=1'
myUsername = "TestingThi3332"


"""
The reason we are using the executable path instead of
simply using webdrive.Firefox() is because geckodriver
is not in our system PATH, so we declare it manually. 
If it was in the path, we could simply do the command
stated above. 
"""

driver = webdriver.Firefox(executable_path='/home/dz/Documents/Code/Repos/OutlookEmails/myproject/geckodriver')

##tells our drive to go to the url
driver.get(url)
# assert "Account" in driver.title
emailAddressInput = driver.find_element_by_id('MemberName')


##clearing out the input section
emailAddressInput.clear()
emailAddressInput.send_keys(myUsername)
emailAddressInput.send_keys(Keys.RETURN)


