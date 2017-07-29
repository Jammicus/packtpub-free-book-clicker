#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys


def createBrowser():
    chromeOptions = Options()
    chromedriver = "Driver/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chromeOptions.binary_location = ("Browser/Chromium.app/Contents/MacOS/Chromium")
    webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    return webdriver.Chrome(chromedriver, chrome_options=chromeOptions)


def openWebPage(browser):
    browser.get('https://www.packtpub.com/packt/offers/free-learning')


def clickFreeBooLink(browser):
    browser.implicitly_wait(10)
    freeBookLink = browser.find_element_by_id('free-learning-claim')
    type(freeBookLink)
    freeBookLink.click()
    print("We have clicked the free book link")
    browser.find_element_by_xpath("//*[@id='account-right-content']")


def logIn(browser, email, password):
    print("Logging in")
    browser.implicitly_wait(2)
    loginIcon = browser.find_element_by_css_selector(".login-popup .float-left")
    loginIcon.click()
    browser.implicitly_wait(1)
    emailBox = browser.find_elements_by_xpath("// *[ @ id = 'email']")
    emailBox[1].send_keys(email)
    passwordBox = browser.find_elements_by_xpath(" // *[ @ id = 'password']")
    passwordBox[1].send_keys(password)
    loginButton = browser.find_elements_by_xpath("// *[ @ id = 'login-form-submit']")
    loginButton[1].click()
    print("Successfully logged in")


if __name__ == "__main__":
    email = sys.argv[1]
    password = sys.argv[2]
    print("The email address you have given us is " + email)
    print("The password you have given us is " + password)
    browser = createBrowser()
    openWebPage(browser)
    logIn(browser, email, password)
    clickFreeBooLink(browser)
    browser.close()
