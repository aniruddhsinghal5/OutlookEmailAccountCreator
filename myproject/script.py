from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import random
import string
import time


##This is the mail website. 
# url = 'https://outlook.live.com/owa/'
url = 'https://outlook.live.com/owa/?nlp=1&signup=1'
myUsername = "TestingThi3332"



def get_random_string(length):
    lower = string.ascii_letters
    result_str = ''.join(random.choice(lower) for i in range(length))
    return result_str
 
myPassword = get_random_string(8) + "$69"
firstName = "Daquan"
lastName = "Toney"

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

##note, we will need to make this more human
emailAddressInput.send_keys(myUsername)
time.sleep(2)
emailAddressInput.send_keys(Keys.RETURN)


## Entering the password phase - we're now choosing our password here
# passwordInput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]")


##Vital for allowing the page to reload.
time.sleep(2)


passwordInput = driver.find_element_by_id("PasswordInput")
passwordInput.clear()
passwordInput.send_keys(myPassword)
##gives time for the page to load
time.sleep(2)
passwordInput.send_keys(Keys.RETURN)

time.sleep(2)

##Name
firstNameInput = driver.find_element_by_id("FirstName")
lastNameInput = driver.find_element_by_id("LastName")

firstNameInput.send_keys(firstName)
time.sleep(1)
lastNameInput.send_keys(lastName)
lastNameInput.send_keys(Keys.RETURN)

##Demographics
time.sleep(2)
countryInput = driver.find_element_by_id("Country")
birthMonthInput = driver.find_element_by_id("BirthMonth")
birthDayInput = driver.find_element_by_id("BirthDay")
birthYearInput = driver.find_element_by_id("BirthYear")

##USA


##drop down menu
actions = ActionChains(driver)
actions.move_to_element(countryInput)
actions.click()

time.sleep(2)

# ourCountry = driver.find_element_by_id("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[3]/div/select/option[244]")
# actions.move_to_element(ourCountry)
# actions.click(ourCountry)
actions.perform()
time.sleep(2)


selectCountry = ActionChains(driver)
selectCountry.move_to_element(ourCountry)
selectCountry.click()
time.sleep(2)
selectCountry.perform()



##all done
# driver.close()