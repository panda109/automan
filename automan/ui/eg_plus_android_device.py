#coding=utf-8
"""
Created on 2020/12/21
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device
"""
import automan.tool.error as error
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_device(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Device', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Device', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    
            
        
    