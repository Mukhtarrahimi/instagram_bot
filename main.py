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
        
        
    def like_photos(self, hashtag_list):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags' + hashtag_list + '/')
        time.sleep(1)
        pic_hrefs  = []
        for i in range(1,2):
            try:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
            except Exception:
                continue
            
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            try:
                time.sleep(random.randint(1,2))
                driver.find_element_by_xpath('//span[@aria-label="Like"]')
                
            except Exception as e:
                time.sleep(2)
                
                
username = 'mukhtarrahimi'
password = 'rahimi111'


ig = InstagramBot(username, password)
ig.login()

hashtag_list = ['programming', 'coding', 'developer']

while True:
    try:
        tag = random.choice(hashtag_list)
        ig.like_photos(tag)

    except Exception:
        ig.close_browser()
        time.sleep(2)
        ig.InstagramBot(username, password)
        ig.login()