import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import mail

#Hi, this is my web scraper project. It's purpose is to send me an email, whenever I get a messege on polish marketplace called OLX.
#It logs into my olx account using facebook.Then it checks for the red dot, if it appeared then I have an unread message and the script sends me an email.


#Website properties

class Olx:
    def __init__(self, email, password):
        self.url = 'https://www.olx.pl/mojolx/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        self.page = requests.get(
            self.url, headers=self.headers)
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

#Logginng into olx

    def login(self):
        bot = self.bot
        bot.get(self.url)
        login_by_fb = bot.find_element_by_link_text('Kontynuuj z Facebook')
        login_by_fb.click()
        email = bot.find_element_by_id('email')
        password = bot.find_element_by_id('pass')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        login_to_fb = bot.find_element_by_id('loginbutton')
        login_to_fb.click()
        time.sleep(5)
        messages = bot.find_element_by_partial_link_text('Wiadom')
        messages.click()

#Checking if someone has sent me a message

    def checkMess(self):
        bot = self.bot
        xpath = '//*[@id="answer_row_7023060867"]/td[3]/div/span/span'

#Checking if the red circle appears

        try:
            element = WebDriverWait(bot, 10)
            element.until(EC.element_to_be_clickable(
                (By.XPATH, xpath)))
            notify_circle = bot.find_element_by_xpath(xpath)
            mail.send_email()
            return notify_circle
        except:
            return 'NoSuchElement'

#Closing webbrowser

    def quit(self):
        bot = self.bot
        bot.quit()

#Typing login and password to facebook.

emailSend = Olx('YourLogin', 'YourPassword')



#Right now the loop is set to check for new messages every hour.

while(True):
    emailSend.login()
    emailSend.checkMess()
    emailSend.quit()
    emailSend.sleep(3600)

