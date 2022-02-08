from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

username = "ian.nelson62@yahoo.com"
password = "Facebook1"
browser = webdriver.Firefox()

browser.get('https://play.nlop.com/signin?DLClient=&promoID=&mchID=5916855&affID=5916806&zenSuID=')

try:
        element = WebDriverWait(browser, 10).unitl(
                    EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
finally:
    browser.quit()

browser.find_element_by_id("user_session[email]").send_keys(username)
browser.find_element_by_id("user_session[password]").send_keys(password)
