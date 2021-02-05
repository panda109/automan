#coding=utf-8
"""
Created on 2021/01/27
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > ECN Fuel Cell
"""
import automan.tool.error as error
import configparser
import os
import re
from automan.tool.verify import Verify
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_ecn_fuel_cell(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECN_Fuel_Cell', valueDict['xpath_id']))
            elem.send_keys(valueDict['value'])
        except:
            raise error.nonamevalue()
    
    def click(self, browser, valueDict):
        try:
            elem_xpath = config.get('ECN_Fuel_Cell', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))

            elem = browser.find_element_by_xpath(config.get('ECN_Fuel_Cell', valueDict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def refresh_until_value_not_null_click(self, browser, valueDict):
        ### Swipe dwon until target value is not null or "--".
        ###
        ### Required parameters:
        ###     xpath_id        : Target element.
        ###     maximum         : Maximum swipe times.
        ###   
        try:
            maximumTimes = int(valueDict['maximum'])
            elem = browser.find_element_by_xpath(config.get('ECN_Fuel_Cell', valueDict['xpath_id']))
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
    
    def element_text_get(self, browser, valueDict):
        try:
            elem_xpath = config.get('ECN_Fuel_Cell', valueDict['xpath_id'])          
            elem = browser.find_element_by_xpath(elem_xpath)
            print("Element text: " + elem.text)
            return elem.text
        except:
            raise error.nonamevalue()
    
    def element_text_verify(self, browser, valueDict):
        try:
            valueDict['xpath_id'] in locals().keys()
            elem_xpath = config.get('ECN_Fuel_Cell', valueDict['xpath_id'])          
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
            if float(valueDict['value']) >= float(valueDict['minimum']) and float(valueDict['value']) <= float(valueDict['maximum']):
                result = True
            valueDict['value'] = result
            valueDict['system_value'] = True
            valueDict['criteria'] = "="
            print("Actual result: ", valueDict['value'], "\nExpected result: ", valueDict['minimum'] + "-" + valueDict['maximum'])
        except:
            raise error.nonamevalue()
    
    def is_integer_verify(self, browser, valueDict):
        ##  Value must be a integer number.
        ##
        ##  Required parameters:
        ##      value           - Value to verify.
        ##        
        try:
            result = False
            match = re.search("^(\d+)$", valueDict['value'])
            if match:
                result = True
            print("Actual result: ", valueDict['value'], "\nExpected result: Integer")
        except:
            raise error.nonamevalue()
        
        try:
            valueDict['value'] = result
            valueDict['system_value'] = True
            valueDict['criteria'] = "="
            Verify().verify(valueDict)
        except error.equalerror:
            raise error.equalerror()
        except error.notequalerror:
            raise error.notequalerror()
        except:
            pass
    
    def is_float_verify(self, browser, valueDict):
        ##  Value must be a float number.
        ##
        ##  Required parameters:
        ##      value           - Value to verify.
        ##        
        try:
            result = False
            match = re.search("(\d+\.\d+)", valueDict['value'])
            if match:
                result = True
            print("Actual result: ", valueDict['value'], "\nExpected result: Float")
        except:
            raise error.nonamevalue()
        
        try:
            valueDict['value'] = result
            valueDict['system_value'] = True
            valueDict['criteria'] = "="
            Verify().verify(valueDict)
        except error.equalerror:
            raise error.equalerror()
        except error.notequalerror:
            raise error.notequalerror()
        except:
            pass

    def element_located_verify(self, browser, valueDict):
        try:
            elem_xpath = config.get('ECN_Fuel_Cell', valueDict['xpath_id'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    #def element_disappear_verify(self, browser, valueDict):
    #    try:
    #        elem_xpath = config.get('ECN_Fuel_Cell', valueDict['xpath_id'])
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
    
    
    
        
    #    try:
    #        Verify().verify(valueDict)
    #    except error.notequalerror:
    #        raise error.notequalerror()
    #    except error.equalerror:
    #        raise error.equalerror()
    #    except:
    #        pass
    #
    #def previous_temperature_click(self, browser, valueDict):
    #    ### Swipe down number picker to select the previous degree.
    #    ###
    #    ### Required parameters:
    #    ###     xpath_id        : XPath of current temperature.
    #    ###   
    #    try:
    #        elem = browser.find_element_by_xpath(config.get('ECN_Fuel_Cell', valueDict['xpath_id']))
    #        elemLocation = elem.location
    #        elemSize = elem.size
    #        window_bounds = browser.get_window_size()
    #        x1 = int(window_bounds["width"]) * 0.5
    #        y1 = int(elemLocation["y"])
    #        x2 = int(window_bounds["width"]) * 0.5
    #        y2 = int(elemLocation["y"]) + int(elemSize["height"])
    #        browser.swipe(x1, y1, x2, y2, 1000)
    #    except:
    #        raise error.nonamevalue()
    #    
    #def next_temperature_click(self, browser, valueDict):
    #    ### Swipe up number picker to select the next degree.
    #    ###
    #    ### Required parameters:
    #    ###     xpath_id        : XPath of current temperature.
    #    ###   
    #    try:
    #        elem = browser.find_element_by_xpath(config.get('ECN_Fuel_Cell', valueDict['xpath_id']))
    #        elemLocation = elem.location
    #        elemSize = elem.size
    #        window_bounds = browser.get_window_size()
    #        x1 = int(window_bounds["width"]) * 0.5
    #        y1 = int(elemLocation["y"]) + int(elemSize["height"])
    #        x2 = int(window_bounds["width"]) * 0.5
    #        y2 = int(elemLocation["y"])
    #        browser.swipe(x1, y1, x2, y2, 1000)
    #    except:
    #        raise error.nonamevalue()
        
    
    
    