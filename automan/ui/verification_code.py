# encoding: utf-8
#!/usr/bin/python

import os, sys, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def get_verification_code_from_web():

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--enable-file-cookies")
    chrome = webdriver.Chrome(os.path.join(os.getcwd(), "chromedriver.exe"))
    chrome.maximize_window()
    chrome.get("https://tempmail.plus/en/#!")
    sleep(3)
    elem = chrome.find_element_by_xpath("/html/body/div[8]/div[1]/div[2]/div[1]/form/div/input")
    for x in range(20):
        elem.send_keys(Keys.BACKSPACE)
    sleep(2)
    elem.send_keys('ndtestmail')
    sleep(2)
    elem.send_keys(Keys.F5)
    sleep(2)
    elem.send_keys(Keys.ENTER),
    sleep(2)
    elem = chrome.find_element_by_xpath("/html/body/div[8]/div[2]/div/div[1]/div[2]/div/div[3]")
    elem.click()
    sleep(2)
    elem = chrome.find_element_by_xpath("/html/body/div[8]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span")
    code = elem.text
    print(code)
    f = open(os.path.join(os.getcwd(), "verification_code.txt"),"w")
    f.write(str(code))
    f.close()
    chrome.quit()

