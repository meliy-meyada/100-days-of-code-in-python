import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

CHROME_DRIVER_PATH= r"Your Driver Location Path"
SIMILAR_ACCOUNT = "Accont Instagram Your Follow"
USERNAME = "Your Email Instagram"
PASSWORD = "Your Password Instagram"



class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(25):
            # ในกรณีนี้ เรากำลังรัน Javascript บางตัว นั่นคือสิ่งที่เมธอด execute_script() ทำ
            # วิธีการนี้สามารถรับสคริปต์และองค์ประกอบ HTML ได้
            # โมดอลในกรณีนี้กลายเป็นข้อโต้แย้ง[0] ในสคริปต์
            # จากนั้นเราใช้ Javascript เพื่อพูดว่า: "เลื่อนด้านบนขององค์ประกอบ modal (ป๊อปอัป) ตามความสูงของ modal (ป๊อปอัป)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for follower in all_buttons:
            if follower.text == 'Follow':
                time.sleep(1)
                follower.click()
                random_time = random.randint(2, 4)
                print(random_time)
                time.sleep(random_time)

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


