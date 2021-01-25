#coding=utf-8
"""
Created on 2020/12/21
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main
"""
import automan.tool.error as error
import configparser
import os
import aircv as ac
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_main(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('main', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('main', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def layout_btn_click(self, browser, value_dict):
        ### It seems like the first click action will wait until APP execute finished.
        ### So it needs to wait until target element is displayed (Timeout: 120 seconds)
        try:
            elem_xpath = config.get('main', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
            elem = browser.find_element_by_xpath(elem_xpath)
            elem.click()
        except:
            raise error.nonamevalue()

    def keyboard_hide(self, browser):
        browser.hide_keyboard()
        
    def refresh_page_click(self, browser, value_dict):
        ### 1. Swipe down
        ### 2. Wait until target item disappear
        ###     Timeout: 30 seconds
        try:
            elem_xpath = config.get('main', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.4
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.8
            
            browser.swipe(x1, y1, x2, y2, 2000)
            try:
                e = WebDriverWait(browser, 30, 1).until(EC.invisibility_of_element_located(elem_loc))
            except:
                pass
        except:
            raise error.nonamevalue()

    def manufacture_code_get(self, browser, value_dict):
        ### Required parameters:
        ###     value_mc    - Manufacture code(English)
        ###     value_in    - Instance number
        ###     value_loc   - Android device system locale
        ###         Input       : [persist.sys.locale]: [{Locale type}]
        ###         Locale type
        ###             ja-JP   : Japanese
        ###             zh-TW   : Chinese(Traditional)
        ###             en-US   : English(United States)
        ###
        ### 1. Transfer manufacture code to Japanese (If Android's language is ja-JP)
        ### 2. Concat manufacture code and instance number
        ###     Output format: {manufacture code}-{instance number}
        ###
        try:
            value_dict['value_mc'] in locals().keys()
            value_dict['value_in'] in locals().keys()
            value_dict['value_loc'] in locals().keys()
            
            value_dict['value_loc'] = re.search("\[persist.sys.locale\]:\s\[([\s\S]+)\]", value_dict['value_loc'])
            value_dict['value_loc'] = (value_dict['value_loc']).group(1)
            
            if value_dict['value_loc'] == "ja-JP":
                value_dict['value_mc'] = config.get('Manufacture_code', value_dict['value_mc'])
            return value_dict['value_mc'] + "-" + value_dict['value_in']
        except:
            raise error.nonamevalue()

    def keyboard_hide(self, browser):
        browser.hide_keyboard()

    #def element_focus_click(self, browser, value_dict):
    #    elem = browser.find_element_by_xpath('android:id/statusBarBackground')
    #    elem = browser.switch_to.active_element
    #    #value_dict['xpath_id']
    
    #def system_bar_click(self, browser, value_dict):
    #    ### Click system bar for 1 time.
    #    ###
    #    ### Required parameters:
    #    ###     
    #    ###
    #    try:
    #        elem = browser.find_element_by_id('android:id/statusBarBackground')
    #        elem.click()
    #    except:
    #        raise error.nonamevalue()
       
        