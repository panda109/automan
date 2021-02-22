#coding=utf-8
"""
Created on 2021/01/20
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Thermo Pixi dashboard
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

class eg_plus_android_thermo_pixi_dashboard(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
            elem.send_keys(valueDict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, valueDict):
        try:
            elem_xpath = config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))

            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def ignore_exception_click(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
            elem.click()
        except:
            pass
    
    def thermo_temperature_text_get(self, browser, valueDict):
        ### 1. Swipe down to refresh page
        ### 2. Until thermo temperature is not null
        ###     Maximum     : 60 times
        ###     Interval    : 3 seconds
        ###
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
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
                print("Thermo Pixi - temperature: " + instantDegree)
                return instantDegree
        except:
            raise error.nonamevalue()

    def element_text_get(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
            print("Element text: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()

    def element_located_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    def element_attribute_get(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
            value = elem.get_attribute(valueDict['attribute'])
        except:
            raise error.nonamevalue()
        return value
    
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
            elem = browser.find_element_by_xpath(config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id']))
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
    
    def element_disappear_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id'])
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
    
    def toast_verify(self, browser, valueDict):
        toast_loc = ("xpath", ".//*[contains(@text, '" + valueDict['value'] + "')]")
        toast = WebDriverWait(browser, 3, 0.1).until(EC.presence_of_element_located(toast_loc))
      
    def element_text_verify(self, browser, valueDict):
        try:
            valueDict['xpath_id'] in locals().keys()
            elem_xpath = config.get('Thermo_Pixi_Dashboard', valueDict['xpath_id'])          
            elem = browser.find_element_by_xpath(elem_xpath)
            valueDict['system_value'] = elem.text
        except:
            pass
        
        try:
            valueDict['value'] = str.encode(valueDict['value'])
            valueDict['system_value'] = str.encode(valueDict['system_value'])
            valueDict['criteria'] in locals().keys()
            print("Actual result: ", valueDict['value'], "\nExpected result: ", valueDict['system_value'])
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
    
    #def no_config_toast_verify(self, browser, valueDict):
    #    ### 1. Click #xpath_id# and get the message in toast
    #    ### 2. Timeout: 3 seconds
    #    try:
    #        xpath = valueDict['xpath_id']
    #        elem = browser.find_element_by_xpath(config.get('BRouteConfig', xpath))
    #        elem.click()
    #        
    #        valueDict['value'] = valueDict['value'].replace("\\n", "\n")
    #        
    #        toast_loc = ("xpath", ".//*[contains(@text, '" + valueDict['value'] + "')]")
    #        toast = WebDriverWait(browser, 3, 0.1).until(EC.presence_of_element_located(toast_loc))
    #        valueDict['system_value'] = toast.text
    #        print("Value: " + valueDict['value'] + ", System_value: " + valueDict['system_value'])
    #    except TimeoutException:
    #        raise error.notequalerror()
    #    except:
    #        raise error.nonamevalue()  
    
    
    #def element_disappear_verify(self, browser, valueDict):
    #    try:
    #        elem_xpath = config.get('ECN_Battery_Dashboard', valueDict['xpath_id'])
    #        elem_loc = ("xpath", elem_xpath)
    #        e = WebDriverWait(browser, 120, 1).until(EC.invisibility_of_element_located(elem_loc))
    #        if e == True:
    #            pass
    #        else:
    #            raise error.nonamevalue()
    #    except TimeoutException:
    #        raise error.nonamevalue()
    #    except:
    #        raise error.nonamevalue()
    #
    #def element_text_verify(self, browser, valueDict):    
    #    try:
    #        valueDict['criteria'] in locals().keys()
    #        print("Actual result: ", valueDict['value'], "\nExpected result: ", valueDict['system_value'])
    #    except:
    #        raise error.nonamevalue()
    #    
    #    try:
    #        Verify().verify(valueDict)
    #    except error.notequalerror:
    #        raise error.notequalerror()
    #    except error.equalerror:
    #        raise error.equalerror()
    #    except:
    #        pass
    
    