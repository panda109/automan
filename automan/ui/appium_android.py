# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:42:29 2020

@author: Dustin Lin
"""
from appium import webdriver
from time import sleep
import automan.tool.error as error
import configparser
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'ini', "appium_android.conf"))

class appium_android(object):
    
    def _init_(self):
        pass
    def setting_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        
        setting_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        setting_btn.click()
    def info_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        info_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        info_btn.click()
    def logout_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        logout_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        logout_btn.click()
    def email_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        email_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        email_textbox.clear()
        email_textbox.send_keys(dicParm['email'])
    def psw_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        psw_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        psw_textbox.send_keys(dicParm['password'])
    def login_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        login_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        login_btn.click()
    def login_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            pageNameText = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        except:
            raise error.notfind()
    """------------------------------------------------------------"""
    def new_device_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        new_device_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        new_device_btn.click()
    def device_type_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_type_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        device_type_btn.click()
    def start_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        start_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        start_btn.click()
    def next_step_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        next_step_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        next_step_btn.click()
    def location_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        location_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        location_btn.click()
    def location_name_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        location_name_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        location_name_textbox.send_keys(dicParm['location_name'])
    def enter_click(self, browser):
        browser.hide_keyboard()
    def start_scan_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        scan_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        scan_btn.click()
    def manual_input_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        input_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        input_btn.click()
    def device_id_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_id_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        device_id_textbox.send_keys(dicParm['deviceID'])
    def admin_psw_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        psw_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        psw_textbox.send_keys(dicParm['psw'])
    def wifi_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % dicParm['wifi_name'])
            wifi_btn.click()
        except:
            raise error.equalerror()
    def wifi_psw_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        wifi_psw_textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        wifi_psw_textbox.send_keys(dicParm['wifipsw'])
    def confirm_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        confirm_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        confirm_btn.click()
    def connect_step1_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        setting_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        setting_btn.click()
    def connect_step2_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_list_btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        device_list_btn.click()
    def connect_final_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            cubeicon = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        except:
            raise error.notfind()    
        
        