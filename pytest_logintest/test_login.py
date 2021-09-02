from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(executable_path="C:\\Users\\Sarvotam\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

def test_site():
    driver.get("https://preprlabs.org/login")
    ActualTitle = driver.getTitle()
    ExpectedTitle = "https://preprlabs.org/login"
    assert ActualTitle == ExpectedTitle, "Navigated to Prepr login page"

def test_linkedln_login():
    driver.find_element_by_link_text('Continue with LinkedIn').click()
    user_input = driver.find_element_by_id('username')
    driver.implicitly_wait(50)
    user_input.send_keys('testmailsomething0@gmail.com')
    password_input = driver.find_element_by_id('password')
    password_input.send_keys('Prepr@123')
    driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()
    driver.find_element_by_name('action').click()

def test_microsoft_login():
    driver.find_element_by_link_text('Continue with Microsoft').click()
    driver.implicitly_wait(50)
    user_input = driver.find_element_by_id('i0116')
    user_input.send_keys('testmailsomething0@gmail.com')
    next_key = driver.find_element_by_id('idSIButton9')
    next_key.click()
    driver.implicitly_wait(100)
    password_input = driver.find_element_by_id('i0118')
    password_input.send_keys('Prepr@123')
    submit_key = driver.find_element_by_id('idSIButton9').click()

def test_google_login():
    driver.find_element_by_link_text('Continue with Google').click()
    user_input = driver.find_element_by_name('identifier')
    user_input.send_keys('testmailsomething0@gmail.com')
    next_key = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]')
    driver.implicitly_wait(50)
    next_key.click()

def test_magnet_login():
    driver.find_element_by_link_text('Continue with Magnet').click()
    user_input = driver.find_element_by_id('email')
    user_input.send_keys('testmailsomething0@gmail.com')
    password_input = driver.find_element_by_id('password')
    password_input.send_keys('Prepr@123')
    driver.find_element_by_id('sign-in').click()

def test_apple_login():
    driver.find_element_by_id('appleid-signin').click()
    user_input = driver.find_element_by_id('account_name_text_field')
    user_input.send_keys('testmailsomething0@gmail.com')
    driver.find_element_by_tag_name('i').click()
    driver.implicitly_wait(50)
    password_input = driver.find_element_by_id('password_text_field')
    password_input.send_keys('Prepr@123')
    driver.find_element_by_tag_name('i').click()

#apple_login()
#google_login()
#microsoft_login()
#linkedln_login()
#apple_login()
#magnet_login()
test_site()

