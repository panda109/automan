# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:29 2020

@author: Dustin Lin
"""
from appium import webdriver
from time import sleep
import automan.tool.error as error
import os
import configparser
from selenium.webdriver.support.ui import WebDriverWait


class appium_ios(object):
    
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(os.path.join(os.getcwd() , 'ini', "ui_ios.conf"),encoding="utf-8")
            print(self.config.get('xpath','landingpage_xpath'))
        except :
            raise error.notfind()
    
    def locate(self, browser,value_dict):
            dicParm = dict(value_dict)
            try:
                element = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
                return element
            except:
                raise error.notfind()
    
    def element_click(self, browser, value_dict):
            #dicParm = dict(value_dict)
            btn = self.locate(browser, value_dict)
            btn.click()
    def element_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            textbox = self.locate(browser, value_dict)
            textbox.send_keys(dicParm['input'])
    
    def keyboard_hide(self, browser):
            browser.hide_keyboard()
    
    def wifi_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            wifi_list_container = browser.find_elements_by_xpath(self.config.get("xpath", dicParm['xpath']))
            wifi_list = []
            for item in range(len(wifi_list_container)):
                wifi_list.append(wifi_list_container[item].text)
            print('!!!!!!!!!!!!!')
            print(len(wifi_list_container))
            print(wifi_list)
            print('//*[@text="%s"]' % dicParm['wifi_name'])
            if dicParm['wifi_name'] in wifi_list:
                wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % config.get("xpath", dicParm['xpath']))
                wifi_btn.click()
            else:
                raise error.equalerror()
    
    def test_wifi_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            try:
                wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % config.get("xpath", dicParm['xpath']))
                wifi_btn.click()
            except:
                raise error.equalerror()
    
    def connect_verify(self, browser, value_dict):
            dicParm = dict(value_dict)
            lastPG_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath'])).click()
            device_list_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_list_btn.click()
            try:
                cubeicon = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            except:
                raise error.notfind()
    
    def element_verify(self, browser, value_dict):
            try:
                self.locate(browser, value_dict)
                pass
            except:
                raise error.notfind()
    
    
    '''
    def psw_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            psw_box = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']).send_keys(dicParm['psw']))
    '''
