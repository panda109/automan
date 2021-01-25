#coding=utf-8
"""
Created on 2021/01/20
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Thermo Pixi Setup
"""
import automan.tool.error as error
import configparser
import os
from automan.tool.verify import Verify
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_thermo_pixi_setup(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Setup', value_dict['xpath_id']))
            elem.send_keys(value_dict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, value_dict):
        try:
            elem_xpath = config.get('Thermo_Pixi_Setup', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))

            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Setup', value_dict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def element_attribute_verify(self, browser, valueDict):
        ### Verify attribute of target element.
        ###
        ### Required parameters:
        ###     xpath_id    : XPath of target element.
        ###     attribute   : The attribute will be fetched.
        ###     value       : Expected value of target attribute.
        ###     criteria    : Criteria for comparing expected value and actual value.
        ###
        try:
            valueDict['xpath_id'] in locals().keys()
            valueDict['attribute'] in locals().keys()
            valueDict['value'] in locals().keys()
            valueDict['criteria'] in locals().keys()    
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Setup', valueDict['xpath_id']))
            valueDict['system_value'] = elem.get_attribute(valueDict['attribute'])
            print("Actual result: ", valueDict['system_value'], "\nExpected result: ", valueDict['value'])
        except:
            raise error.nonamevalue()
        try:
            Verify().verify(valueDict)
        except error.notequalerror:
            raise error.notequalerror()
        except error.equalerror:
            raise error.equalerror()
        except:
            pass

    def device_search_verify(self, browser, valueDict):
        ### Refresh #xpath_id# by click #xpath_refresh# until #xpath_id# is equal to #value#.
        ###     Maximum retry times : 60
        ###
        ### Required parameters:
        ###     xpath_id        : XPath of element that show system value.
        ###     xpath_refresh   : XPath of element that can refresh page.
        ###     value           : Expected value on #xpath_id#.
        ###
        try:
            valueDict['xpath_id'] in locals().keys()
            valueDict['xpath_refresh'] in locals().keys()
            valueDict['value'] in locals().keys()
            valueDict['value'] = (valueDict['value']).upper()
        except:
            raise error.nonamevalue()
        
        mac_address_xpath = config.get('Thermo_Pixi_Setup', valueDict['xpath_id'])
        refresh_btn_xpath = config.get('Thermo_Pixi_Setup', valueDict['xpath_refresh'])
        elem_loc = ("xpath", mac_address_xpath)
        
        try:
            for i in range(60):
                WebDriverWait(browser, 10, 1).until(EC.presence_of_element_located(elem_loc))
                elem = browser.find_element_by_xpath(mac_address_xpath)
                if elem.text == valueDict['value']:
                    return
                else:
                    elem_refresh = browser.find_element_by_xpath(refresh_btn_xpath)
                    elem_refresh.click()
            raise error.notfind()
        except:
            raise error.notfind()
        
    def element_located_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('Thermo_Pixi_Setup', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 300, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
            
    #def system_bar_click(self, browser, value_dict):
    #    ### Click system bar for 1 time.
    #    ###
    #    ### Required parameters:
    #    ###     
    #    ###
    #    try:
    #        elem = browser.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.View')
    #        elem.click()
    #    except:
    #        raise error.nonamevalue()
    
    
    
    
'''
    def battery_level_text_get(self, browser, value_dict):
        ### 1. Swipe down to refresh page
        ### 2. Until battery level is not null
        ###     Maximum     : 60 times
        ###     Interval    : 3 seconds
        ###
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_Battery_Dashboard', value_dict['xpath_id']))
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
                print("ECN Battery - battery level: " + instantDegree)
                return instantDegree
        except:
            raise error.nonamevalue()

    def element_text_get(self, browser, value_dict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_Battery_Dashboard', value_dict['xpath_id']))
            print("Element text: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    
    
    
    def element_disappear_verify(self, browser, value_dict):
        try:
            elem_xpath = config.get('ECN_Battery_Dashboard', value_dict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            e = WebDriverWait(browser, 120, 1).until(EC.invisibility_of_element_located(elem_loc))
            if e == True:
                pass
            else:
                raise error.nonamevalue()
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    def element_text_verify(self, browser, value_dict):    
        try:
            value_dict['criteria'] in locals().keys()
            print("Actual result: ", value_dict['value'], "\nExpected result: ", value_dict['system_value'])
        except:
            raise error.nonamevalue()
        
        try:
            Verify().verify(value_dict)
        except error.notequalerror:
            raise error.notequalerror()
        except error.equalerror:
            raise error.equalerror()
        except:
            pass
    
    def element_text_verify(self, browser, value_dict):    
        try:
            value_dict['criteria'] in locals().keys()
            print("Actual result: ", value_dict['value'], "\nExpected result: ", value_dict['system_value'])
        except:
            raise error.nonamevalue()
        
        try:
            Verify().verify(value_dict)
        except error.notequalerror:
            raise error.notequalerror()
        except error.equalerror:
            raise error.equalerror()
        except:
            pass
'''
    