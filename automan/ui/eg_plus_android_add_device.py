#coding=utf-8
"""
Created on 2020/12/21
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Add device
"""
import automan.tool.error as error
import configparser
import os
import aircv as ac
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_add_device(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Add_device', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Add_device', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def element_find_click(self, browser, value_dict):
        ### Swipe up to find target element that contains #element_text#, and click it.
        ###     Maximum swipe   : 10 times
        ###
        ### Required parameters:
        ###     element_text    : Element's child must contain this text.
        ###     
        try:
            elem_xpath = "//*[@text=\"" + value_dict['element_text'] + "\"]"
            elem_loc = ("xpath", elem_xpath)
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.8
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.4
            
            e = None
            for i in range(10):
                try:
                    e = WebDriverWait(browser, 1, 0.5).until(EC.presence_of_element_located(elem_loc))
                except:
                    pass
            
                if e is not None:
                    elem = browser.find_element_by_xpath(elem_xpath + "/..")
                    elem.click()
                    break
                elif i < 9:
                    browser.swipe(x1, y1, x2, y2, 2000)
                    
            if e == None:
                raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
   
    
    