# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:29 2020

@author: Dustin Lin
"""
from appium import webdriver
from time import sleep
import automan.tool.error as error
from appium.webdriver.common.touch_action import TouchAction
import os
import configparser
from selenium.webdriver.support.ui import WebDriverWait


class appium_ios(object):
    
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(os.path.join(os.getcwd() , 'ini', "ui_ios.conf"),encoding="utf-8")
            #print(self.config.get('xpath','landingpage_xpath'))
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
            try:
                #browser.hide_keyboard('Done')
                TouchAction(browser).tap(x=375, y=487).perform()
                print(browser.is_keyboard_shown())
            except:
                print('Keyboard not hide ')
                raise error.notfind()
    
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
                wifi_btn = self.locate(browser,value_dict)
                print(wifi_btn)
                wifi_btn.click()
            except:
                raise error.equalerror()
    
    def alert_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            try:
                alert_btn = browser.execute_script('mobile: alert', {'action': 'getButtons'})
                #print(alert_btn[1])
                ret = browser.execute_script('mobile: alert',{'action': 'accept'})
                #print(ret)
                #browser.switch_to.context('Alert1')
                #browser.find_element_by_xpath(config.get("xpath", dicParm['xpath'])).click()
            except:
                #print(ret)
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
