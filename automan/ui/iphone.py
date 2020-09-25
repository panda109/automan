#coding:utf-8
'''
Created on 2010/12/10
@author: panda.huang
'''
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
import configparser
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd() , 'conf' , "iphonetest.conf"),encoding="utf-8")

class iphone(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass
   
   
    def set(self,browser,value_dict):
        xpath = value_dict['xpath_id']
        print(xpath)
        elem = browser.find_element_by_xpath(config.get('test', xpath))
        elem.send_keys(value_dict['value'])
    
    def click(self,browser,value_dict):
        xpath = value_dict['xpath_id']
        elem = browser.find_element_by_xpath(config.get('test', xpath))
        elem.click()

    def error_test(self,browser):
        return 1
    
    def errorkey_test(self,browser,dict):
        return 1