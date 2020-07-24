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
            #print(self.config.get('xpath','info_xpath'))
        except :
        
            raise error.notfind()
    def setting_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            setting_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            setting_btn.click()
    def new_device_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            new_device_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            new_device_btn.click()
    def device_type_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            device_type_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_type_btn.click()
    def start_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            start_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            start_btn.click()
    def next_step_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            next_step_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            next_step_btn.click()
    def location_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            location_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            location_btn.click()
    def location_name_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            location_name_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            location_name_textbox.send_keys(dicParm['location_name'])
    def enter_click(self, browser):
            browser.hide_keyboard()
    def start_scan_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            scan_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            scan_btn.click()
    def manual_input_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            input_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            input_btn.click()
    def device_id_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            device_id_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_id_textbox.send_keys(dicParm['deviceID'])
    def admin_psw_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            psw_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            psw_textbox.send_keys(dicParm['psw'])
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
    def wifi_psw_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            wifi_psw_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            wifi_psw_textbox.send_keys(dicParm['wifipsw'])
    def confirm_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            confirm_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            confirm_btn.click()
    def connect_verify(self, browser, value_dict):
            dicParm = dict(value_dict)
            lastPG_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath'])).click()
            device_list_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_list_btn.click()
            try:
                cubeicon = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            except:
                raise error.notfind()
                       
    def info_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            info_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            info_btn.click()
    def logout_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            logout_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            logout_btn.click()
        
    def email_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            email_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            email_textbox.clear()
            email_textbox.send_keys(dicParm['email'])
        
    def psw_set(self, browser, value_dict):
            dicParm = dict(value_dict)
            psw_textbox = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            psw_textbox.send_keys(dicParm['password'])
        
    def login_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            login_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            login_btn.click()
        
    def login_verify(self, browser, value_dict):
            dicParm = dict(value_dict)
            
            try:
                pageNameText = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
                pass
            except:
                raise error.notfind()
    
    def device_list_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            device_list_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_list_btn.click()
    def device_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            device_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            device_btn.click()
    def wifi_setting_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            wifi_item_btn = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']))
            wifi_item_btn.click()
    
    def psw_click(self, browser, value_dict):
            dicParm = dict(value_dict)
            psw_box = browser.find_element_by_xpath(self.config.get("xpath", dicParm['xpath']).send_keys(dicParm['psw']))
