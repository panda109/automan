#coding=utf-8
'''
Created on 2015/04/28

@author: Jason Ma
'''
import time
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
from automan.util.tool  import Tool
import ConfigParser
from selenium.webdriver.common.by import By

config = ConfigParser.ConfigParser()
config.read(".\ini\Eonone.conf")


class eonone_login(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass


    def textbox_username_set(self, ie, value_dict):
        local_dict = dict(value_dict)
        elem = ie.find_element_by_id(config.get("login", "id_signin_username"))
        elem.send_keys(local_dict["key"] )
        
    def textbox_password_set(self, ie, value_dict):
        local_dict = dict(value_dict)
        elem = ie.find_element_by_id(config.get("login", "id_signin_passwd"))
        elem.send_keys(local_dict["key"] )    
    
    def button_login_click(self, ie):
        text = config.get("login", "class_signin_button")
        xpath="//button[@class='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        elem.click()