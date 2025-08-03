from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def close_browser(self):
        self.driver.close()
    
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        login_button = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')
        login_button.click()
        time.sleep(2)
        user_name_box = driver.find_element_by_xpath('//input[@name="username"]')
        user_name_box.clear()
        user_name_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath('//input[@name="password"]')
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(keys.ENTER)
        time.sleep(1)
        driver.get('https://www.instagram.com/mukhtarrahime')
        
        
        