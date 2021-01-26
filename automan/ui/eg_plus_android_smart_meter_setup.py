#coding=utf-8
"""
Created on 2020/12/21
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Add device > Smart Meter Setup
"""
import automan.tool.error as error
import configparser
import os
import aircv as ac
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_smart_meter_setup(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Setup', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()

    def click(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Setup', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def keyboard_hide(self, browser):
        browser.hide_keyboard()

    def element_located_verify(self, browser, value_dict):
        try:
            xpath = value_dict['xpath_id']
            elem_xpath = config.get('ECHONET_Lite_device_Setup', xpath)
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()

    def device_name_click(self, browser, value_dict):
        ### Wait until target element is displayed (Timeout: 120 seconds)
        try:
            elem_xpath = config.get('Smart_Meter_Setup', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
            elem = browser.find_element_by_xpath(elem_xpath)
            elem.click()
        except:
            raise error.nonamevalue()
    
    def done_btn_click(self, browser, value_dict):
        ### Wait until target element is displayed (Timeout: 120 seconds)
        try:
            elem_xpath = config.get('Smart_Meter_Setup', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
            elem = browser.find_element_by_xpath(elem_xpath)
            elem.click()
        except:
            raise error.nonamevalue()
    