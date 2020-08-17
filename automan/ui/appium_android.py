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
import aircv as ac
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'ini', "appium_android.conf"))

class appium_android(object):
    
    def _init_(self):
        pass
    def element_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        btn = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        btn.click()
    def element_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        textbox = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        textbox.clear()
        textbox.send_keys(dicParm['inputField'])
        #textbox.send_Keys(dicParm['inputField'])
    def keyboard_hide(self, browser):
        browser.hide_keyboard()
    def element_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            element = browser.find_element_by_xpath(config.get("xpath", dicParm['xpath']))
        except:
            raise error.notfind()
    def wifi_set(self, browser, value_dict):
        dicParm = dict(value_dict)
        try:
            wifi_btn = browser.find_element_by_xpath('//*[@text="%s"]' % dicParm['wifi_name'])
            wifi_btn.click()
        except:
            raise error.equalerror()
    '''
    def img_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        path = os.path.join(os.getcwd(),'img',dicParm['imgname']) + '.png'
        imgScreenShot = browser.get_screenshot_as_file(path)
        imgsrc = ac.imread(path)
        imgobj = ac.imread(dicParm['target'])
        match_result = ac.find_template(imgsrc, imgobj, 0.5)
        if match_result is not None:
            imgsrc_height, imgsrc_width = (imgsrc.shape[0], imgsrc.shape[1])
        print(match_result)
        obj_x, obj_y = match_result['result']
        print(browser.get_window_size())
        try:
            browser.tap([(obj_x, obj_y), (obj_x, obj_y)], 100)
        except:
            raise error.notfind()
    '''   
    
    def img_verify(self, browser, value_dict):
        dicParm = dict(value_dict)
        path = os.path.join(os.getcwd(),'img',dicParm['imgname']) + '.png'
        #print(path)
        imgScreenShot = browser.get_screenshot_as_file(path)#對螢幕做節圖
        imgsrc = ac.imread(path)#輸入節圖
        imgobj = ac.imread(dicParm['target'])#輸入要找的目標
        match_result = ac.find_template(imgsrc, imgobj, 0.5)#尋找目標
        if match_result is not None:
            imgsrc_height, imgsrc_width = (imgsrc.shape[0], imgsrc.shape[1])
        print(match_result)

        obj_x, obj_y = match_result['result']

        print(browser.get_window_size())

        try:

            browser.tap([(obj_x, obj_y), (obj_x, obj_y)], 100)
            
        except:
            raise error.notfind()

    def img_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        browser.update_settings({"getMatchedImageReslut": True})
        img = browser.find_element_by_image(dicParm['target'])
        img.click()
    '''
    def img_click(self, browser, value_dict):
        dicParm = dict(value_dict)
        imgsrc = ac.imread(dicParm['template'])
        imgobj = ac.imread(dicParm['target'])
        match_result = ac.find_template(imgsrc, imgobj, 0.5)
        if match_result != None:
            imgsrc_height, imgsrc_width = imgsrc.shape[0], imgsrc.shape[1]
        print("imgsrc H: ", imgsrc_height)
        print("imgsrc W: ", imgsrc_width)
        obj_x, obj_y = match_result['result']
        print("obj_x: ", obj_x)
        print("obj_y: ", obj_y)
        screen_width = browser.get_window_size()['width']
        screen_height = browser.get_window_size()['height']
        print('screen_width', screen_width)
        print('screen_height', screen_height)
        
        position_x = int(obj_x / imgsrc_width * screen_width)
        position_y = int(obj_y / imgsrc_height * screen_height)
        print('position_x', position_x)
        print('position_y', position_y)
        browser.tap([(position_x, position_y), (position_x, position_y)], 100)
    '''  
        
        
        
        
        
        