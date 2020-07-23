# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:29 2020

@author: Dustin Lin
"""
from appium import webdriver
from time import sleep
import automan.tool.error as error
from selenium.webdriver.support.ui import WebDriverWait

class appium_android(object):
    
    def _init_(self):
        pass
    def setting_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        setting_btn = browser.find_element_by_id(dicParm['setting_id'])
        setting_btn.click()
    def new_device_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        new_device_btn = browser.find_element_by_id(dicParm['new_device_id'])
        new_device_btn.click()
    def device_type_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_type_btn = browser.find_element_by_xpath(dicParm['deviceType_xpath'])
        device_type_btn.click()
    def start_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        start_btn = browser.find_element_by_id(dicParm['start_id'])
        start_btn.click()
    def next_step_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        next_step_btn = browser.find_element_by_id(dicParm['next_step_id'])
        next_step_btn.click()
    def location_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        location_btn = browser.find_element_by_id(dicParm['location_id'])
        location_btn.click()
    def location_name_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        location_name_textbox = browser.find_element_by_id(dicParm['location_name_textbox_id'])
        location_name_textbox.send_keys(dicParm['location_name'])
    def enter_click(self, browser):
        browser.hide_keyboard()  
    def start_scan_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        scan_btn = browser.find_element_by_id(dicParm['start_scan_id'])
        scan_btn.click()
    def manual_input_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        input_btn = browser.find_element_by_id(dicParm['manual_input_id'])
        input_btn.click()
    def device_id_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_id_textbox = browser.find_element_by_id(dicParm['device_textbox_id'])
        device_id_textbox.send_keys(dicParm['deviceID'])
    def admin_psw_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        psw_textbox = browser.find_element_by_xpath(dicParm['psw_textbox_xpath'])
        psw_textbox.send_keys(dicParm['psw'])
    def wifi_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        wifi_list_container = browser.find_elements_by_xpath(dicParm['wifi_list_xpath'])
        wifi_list = []
        for item in range(len(wifi_list_container)):
            wifi_list.append(wifi_list_container[item].text)
        print('!!!!!!!!!!!!!')
        print(len(wifi_list_container))
        print(wifi_list)
        print('//*[@text="%s"]' % dicParm['wifi_name'])
        if dicParm['wifi_name'] in wifi_list:
            wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % dicParm['wifi_name'])
            wifi_btn.click()
        else:
            raise error.equalerror()
    def test_wifi_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % dicParm['wifi_name'])
            wifi_btn.click()
        except:
            raise error.equalerror()
    def wifi_psw_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        wifi_psw_textbox = browser.find_element_by_id(dicParm['wifi_psw_textbox_id'])
        wifi_psw_textbox.send_keys(dicParm['wifipsw'])
    def confirm_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        confirm_btn = browser.find_element_by_id(dicParm['confirm_id'])
        confirm_btn.click()  
    def connect_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        lastPG_btn = browser.find_element_by_id(dicParm['setting_id']).click()
        device_list_btn = browser.find_element_by_id(dicParm['device_list_id']).click()
        try:
            cubeicon = browser.find_element_by_id(dicParm['cubeicon_id'])
        except:
            raise error.notfind()
        
           
        
    def info_click(self, browser, value_dict):
        local_dict = dict(value_dict)
        info_btn = browser.find_element_by_id(local_dict['info_id'])
        info_btn.click()
        
    
    def logout_click(self, browser, value_dict):
        local_dict = dict(value_dict)
        logout_btn = browser.find_element_by_id(local_dict['logout_id'])
        logout_btn.click()
        
    def email_set(self, browser, value_dict):
        local_dict = dict(value_dict)
        email_textbox = browser.find_element_by_xpath(local_dict['email_xpath'])
        email_textbox.clear()
        email_textbox.send_keys(local_dict['email'])
        
    def psw_set(self, browser, value_dict):
        local_dict = dict(value_dict)
        psw_textbox = browser.find_element_by_xpath(local_dict['psw_xpath'])
        psw_textbox.send_keys(local_dict['password'])
        
    def login_click(self, browser, value_dict):
        local_dict = dict(value_dict)
        login_btn = browser.find_element_by_id(local_dict['login_id'])
        login_btn.click()
        
    def login_verify(self, browser, value_dict):
        local_dict = dict(value_dict)
        
        try:
            pageNameText = browser.find_element_by_xpath(local_dict['pageName_xpath'])
            pass
        except:
            raise error.notfind()
        
        
        
        
        
    def device_list_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_list_btn = browser.find_element_by_id(dicParm['device_list_id'])
        device_list_btn.click()
    def device_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        device_btn = browser.find_element_by_id(dicParm['device_id'])
        device_btn.click()
    def wifi_setting_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        wifi_item_btn = browser.find_element_by_id(dicParm['wifi_id'])
        wifi_item_btn.click()
    
    def psw_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        psw_box = browser.find_element_by_id(dicParm['psw_id']).send_keys(dicParm['psw'])
    
        
        

        