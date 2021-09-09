from keep_alive import keep_alive
import os
from selenium_driver import driver
from pages import page
import telebot
import time

bot_chatID = os.environ['bot_chatID']
bot_token = os.environ['bot_token']

tb = telebot.TeleBot(bot_token)

def getUpdateText(driver):
    text = driver.find_element_by_css_selector('.entry-header > div > span.date.meta-item.tie-icon').get_attribute('textContent')
    return text

def getAnimeTitle(driver):
    title = driver.find_element_by_css_selector('.entry-header > h1.post-title.entry-title').get_attribute('textContent')
    return title

def sendMessage(text):
    ret_msg = tb.send_message(bot_chatID, text)
    assert ret_msg.message_id

def checkWebsite(url):
    driver.get(url)
    updateText = getUpdateText(driver)
    title = getAnimeTitle(driver)
    if updateText == '5 minutes ago':
        sendMessage(title + ' ' + updateText)

keep_alive()
while True:
    for url in page:
        checkWebsite(url)
    time.sleep(30)

