from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# instagram bot project code...

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.quit()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def like_photos(self, hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(3)

        pic_hrefs = []
        hrefs_in_view = driver.find_elements(By.TAG_NAME, 'a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '/p/' in elem.get_attribute('href')]

        for link in pic_hrefs[:3]: 
            driver.get(link)
            time.sleep(2)
            try:
                like_button = driver.find_element(By.XPATH, '//span[@aria-label="Like"]')
                like_button.click()
                print(f'Liked photo: {link}')
                time.sleep(random.randint(2, 4))
            except:
                print(f'Already liked or error on: {link}')
                time.sleep(1)

username = 'mukhtarrahimi'
password = 'rahimi111'
ig = InstagramBot(username, password)
ig.login()

hashtags = ['programming', 'coding', 'developer']

while True:
    try:
        tag = random.choice(hashtags)
        ig.like_photos(tag)
        time.sleep(30)  
    except Exception as e:
        print(f'Error: {e}')
        ig.close_browser()
        ig = InstagramBot(username, password)
        ig.login()
