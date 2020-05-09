# -*- coding: utf-8 -*-
'''
Created on 2020/05/08

@author: Shawn Lin
'''
import automan.tool.error as error
from automan.ui.common_tools import GetWebPageElement
import configparser

objConfig = configparser.ConfigParser()

class general_login(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass

    def config_file_load(self, browser, value_dict):
        try:
            dicParm = dict(value_dict)
            objConfig.read(dicParm["file"],encoding="utf-8")
        except:
            raise error.notfind()
           
            
    def textbox_username_set(self, browser, value_dict):
        try:
            dicParm = dict(value_dict)
            objElem = GetWebPageElement(browser, 
                                        objConfig.get("web", "username_field_type").lower(),
                                        objConfig.get("web", "username_xpath_value"),
                                        objConfig.get("web", "login_username_field"))
            objElem.send_keys(dicParm["key"] )
        except:
            raise error.notfind()
        
    def textbox_password_set(self, browser, value_dict):
        try:
            dicParm = dict(value_dict)
            objElem = GetWebPageElement(browser, 
                                        objConfig.get("web", "password_field_type").lower(),
                                        objConfig.get("web", "password_xpath_value"),
                                        objConfig.get("web", "login_password_field"))
            objElem.send_keys(dicParm["key"] )
        except:
            raise error.notfind()
        
    def button_login_click(self, browser):
        try:
            objElem = GetWebPageElement(browser, 
                                        objConfig.get("web", "submit_button_type").lower(),
                                        objConfig.get("web", "submit_xpath_value"),
                                        objConfig.get("web", "login_submit_button"))
            objElem.click()
        except:
            raise error.notfind()