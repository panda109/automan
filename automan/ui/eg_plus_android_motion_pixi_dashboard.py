#coding=utf-8
"""
Created on 2021/01/22
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Motion Pixi dashboard
"""
import automan.tool.error as error
import configparser
import os
from automan.tool.verify import Verify
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_motion_pixi_dashboard(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Motion_Pixi_Dashboard', valueDict['xpath_id']))
            elem.send_keys(valueDict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, valueDict):
        try:
            elem_xpath = config.get('Motion_Pixi_Dashboard', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))

            elem = browser.find_element_by_xpath(config.get('Motion_Pixi_Dashboard', valueDict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()

    def ignore_exception_click(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Motion_Pixi_Dashboard', valueDict['xpath_id']))
            elem.click()
        except:
            pass

    def element_disappear_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('Motion_Pixi_Dashboard', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            e = WebDriverWait(browser, 120, 1).until(EC.invisibility_of_element_located(elem_loc))
            if e == True:
                pass
            else:
                raise error.nonamevalue()
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    def element_text_get(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Motion_Pixi_Dashboard', valueDict['xpath_id']))
            print("Element text: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    