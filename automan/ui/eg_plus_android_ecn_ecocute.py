#coding=utf-8
"""
Created on 2021/01/25
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > ECN EcoCute
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

class eg_plus_android_ecn_ecocute(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_EcoCute', valueDict['xpath_id']))
            elem.send_keys(valueDict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, valueDict):
        try:
            elem_xpath = config.get('ECN_EcoCute', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))

            elem = browser.find_element_by_xpath(config.get('ECN_EcoCute', valueDict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()

    def ignore_exception_click(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_EcoCute', valueDict['xpath_id']))
            elem.click()
        except:
            pass

    def refresh_until_value_not_null_click(self, browser, valueDict):
        ### Swipe dwon until target value is not null or "--".
        ###
        ### Required parameters:
        ###     xpath_id        : Target element.
        ###     maximum         : Maximum swipe times.
        ###   
        try:
            maximumTimes = int(valueDict['maximum'])
            elem = browser.find_element_by_xpath(config.get('ECN_EcoCute', valueDict['xpath_id']))
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.4
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.8
            
            elementValue = False
            for i in range(maximumTimes):
                if elem.text and elem.text != "--":
                    elementValue = elem.text
                    break
                elif i < (maximumTimes - 1):
                    browser.swipe(x1, y1, x2, y2, 2000)
                    
            if not elementValue:
                raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    def element_located_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('ECN_EcoCute', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()

    def element_text_get(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_EcoCute', valueDict['xpath_id']))
            print("Element text: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    
    def element_text_verify(self, browser, valueDict):    
        try:
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
    
    def element_range_text_verify(self, browser, valueDict):    
        ### Verify value in range.
        ###
        ### Required parameters:
        ###     value           : Value to verify.
        ###     minimum         : Minimum range.
        ###     maximum         : Maximum range.
        ###   
        try:
            result = False
            if int(valueDict['value']) >= int(valueDict['minimum']) and int(valueDict['value']) <= int(valueDict['maximum']):
                result = True
            valueDict['value'] = result
            valueDict['system_value'] = True
            valueDict['criteria'] = "="
            print("Actual result: ", valueDict['value'], "\nExpected result: ", valueDict['minimum'] + "-" + valueDict['maximum'])
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
            elem_xpath = config.get('ECN_EcoCute', valueDict['xpath_id'])
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
    
    
    
    