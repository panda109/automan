#coding=utf-8
"""
Created on 2020/12/23
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Smart Meter Dashboard
"""
import automan.tool.error as error
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_smart_meter_dashboard(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def instant_degree_text_get(self, browser, value_dict):
        ### 1. Swipe down to refresh page
        ### 2. Until instant degree is not null
        ###     Maximum     : 60 times
        ###     Interval    : 3 seconds
        ###
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.4
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.8
            
            instantDegree = False
            for i in range(60):
                if elem.text and elem.text != "--":
                    instantDegree = elem.text
                    break
                elif i < 59:
                    browser.swipe(x1, y1, x2, y2, 3000)
                    
            if not instantDegree:
                raise error.nonamevalue()
            else:
                print("Smart Meter - instant degree: " + instantDegree)
                return instantDegree
        except:
            raise error.nonamevalue()
            
    def time_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - time: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def rssi_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - RSSI: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def title_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - device name: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def used_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - used electricity data: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def sold_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - sold electricity data: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def instant_content_title_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - instant content title: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def instant_content_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - instant content value: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    
    def instant_content_time_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - instant content time: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def today_content_title_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - today content title: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def today_content_use_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - today content used value: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def today_content_sold_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - today content sold value: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    
    def today_content_duration_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - today content duration: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def history_title_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - history title: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def history_time_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - history time: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def history_duration_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - history duration: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    def history_value_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Smart_Meter_Dashboard', value_dict['xpath_id']))
            print("Smart Meter - history value: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
            
    