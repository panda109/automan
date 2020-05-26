'''
Created on 2011/2/14

@author: panda109
'''
import time
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from app_config import *


class test_web(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    if __name__ == '__main__':
        command_executor = "http://127.0.0.1:4723/wd/hub"
        app_path = '/Users/lawrey/Library/Developer/Xcode/DerivedData/AppiumTest-fubxvjmcpxiewkenopxpcerwhudw/Build/Products/Debug-iphonesimulator/AppiumTest.app'
        
       
        dc = {
  "platformName": "iOS",
  "platformVersion": "13.5",
  "deviceName": "iPhone 8",
  "automationName": "XCUITest",
  "udid": "FA9241B4-A202-4570-B89B-9B8C69D5CF26",
  "app": "/Users/tim/Library/Developer/Xcode/DerivedData/AppiumTest-clgsjcgjpdsyjyeawwrknesnrkuf/Build/Products/Debug-iphonesimulator/AppiumTest.app",
  "noReset": True
}

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=dc)
        el = driver.find_element_by_id('android:id/text1')
        el.click()
        driver.quit()
        
        