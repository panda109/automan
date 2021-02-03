#coding=utf-8
"""
Created on 2020/12/24
@author     : Roger Wei
Project     : Ecogenie+ APP
APP Page    : Main > Device > Add device > ECHONET Lite Certificated
"""
import automan.tool.error as error
import configparser
import os
import aircv as ac
import re, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android_ecn_device_setup(object):
    
    def _init_(self):
        pass
        
    def set(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECHONET_Lite_device_Setup', valueDict['xpath_id']))
            elem.send_keys(valueDict['value'])
        except:
            raise error.nonamevalue()

    def click(self, browser, valueDict):
        try:
            elem = browser.find_element_by_xpath(config.get('ECHONET_Lite_device_Setup', valueDict['xpath_id']))
            elem.click()
        except:
            raise error.nonamevalue()
    
    def keyboard_hide(self, browser):
        browser.hide_keyboard()
    
    def element_located_verify(self, browser, valueDict):
        try:
            xpath = valueDict['xpath_id']
            elem_xpath = config.get('ECHONET_Lite_device_Setup', xpath)
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()
    
    def ECN_device_name_click(self, browser, valueDict):
        ### Required parameters:
        ###     xpath_id        - List view where ECN device name located
        ###     value_mc        - ECN device manufacture code
        ###     value_in        - ECN device instance number
        ###     value_ia        - ECN device IP address
        ###     value_sc        - ECN device category text in scan list
        ###         Format          : {Chinese text}/{Japanese text}/{English text}
        ###     value_loc       - Android device system locale
        ###         Input           : [persist.sys.locale]: [{Locale type}]
        ###         Supported locale type
        ###             ja-JP       : Japanese
        ###             zh-TW       : Chinese(Traditional)
        ###             en-US       : English(United States)
        ###
        ### 1. Wait until #xpath_id# appear (Timeout: 120 seconds)
        ### 2. Swipe up (Maximum: 120 times; Interval: 1 second)
        ### 3. Until find #value# in #xpath_id#
        ###
        try:
            valueDict['value_loc'] = re.search("\[persist.sys.locale\]:\s\[([\s\S]+)\]", valueDict['value_loc'])
            valueDict['value_loc'] = (valueDict['value_loc']).group(1)
            if re.search("ja-", valueDict['value_loc']) != None:
                valueDict['value_mc'] = config.get('Manufacture_code', valueDict['value_mc'])
            valueDict['value_mc'] = valueDict['value_mc'] + "-" + valueDict['value_in']
            valueDict['xpath_id'] = config.get('ECHONET_Lite_device_Setup', valueDict['xpath_id'])
            valueDict['value_sc'] = config.get('ECHONET_Lite_device_Setup', valueDict['value_sc'])
            valueDict['value_sc'] = (valueDict['value_sc']).split(";")
            if re.search("ja-", valueDict['value_loc']) != None:
                valueDict['value_sc'] = (valueDict['value_sc'])[1]
            elif re.search("zh-", valueDict['value_loc']) != None:
                valueDict['value_sc'] = (valueDict['value_sc'])[0]
            else:
                valueDict['value_sc'] = (valueDict['value_sc'])[2] 
            #print("Category: " + valueDict['value_sc'] + "\n" + \
            #    "ECN device: " + valueDict['value_mc'] + ", " + valueDict['value_ia'])
        except:
            raise error.nonamevalue()
            
        try:
            ## Step 1: Find category
            elem_xpath = valueDict['xpath_id']
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
            
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.8
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.4
            
            target_xpath = "//*[@text=\"" + valueDict['value_sc'] + "\"]"
            target_loc = ("xpath", target_xpath)
            
            e = None
            max_swipe = 120
            for i in range(max_swipe + 1):
                try:
                    e = WebDriverWait(browser, 1, 0.5).until(EC.presence_of_element_located(target_loc))
                except:
                    pass
            
                if e is not None:
                    ## Find target category! 
                    print("Found category")
                    
                    ## Check all elements in parent container: valueDict['xpath_id']
                    check_elem_index = 1
                    elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                    while elem != None:
                        elem_text = elem.get_attribute("text")
                        if elem_text == valueDict['value_sc']:
                            #print("Target located at: ", check_elem_index)
                            break
                        check_elem_index = check_elem_index + 1
                        elem = None
                        try:
                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                        except:
                            pass
                    break
                elif i < (max_swipe - 1):
                    #print("Swipe up")
                    browser.swipe(x1, y1, x2, y2, 2000)
                    time.sleep(1)
            print("Swipe times: " + str(i))
            
            ## Step 2: Find ECN device
            if e == None:
                print("Not found category")
                raise error.nonamevalue()
            else:
                max_swipe = max_swipe - i
                ECN_found = False
                lastChance = False
                for i in range(max_swipe + 1):
                    startIndex = -1
                    endIndex = -1
                
                    ## 1. Find target category.
                    checkIndex = 1
                    while 1:
                        elem = None
                        try:
                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(checkIndex) + "]")
                            elem_text = elem.get_attribute("text")
                            if len(elem_text) != 0 and elem_text == valueDict['value_sc']:
                                ## Found target category
                                #print("Found target category:", checkIndex)
                                startIndex = checkIndex
                                break
                            checkIndex = checkIndex + 1
                        except:
                            break
                        
                    ## 2. Find another category
                    checkIndex = 1 if startIndex == -1 else startIndex
                    while 1:
                        elem = None
                        try:
                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(checkIndex) + "]")
                            elem_text = elem.get_attribute("text")
                            if len(elem_text) != 0 and elem_text != valueDict['value_sc']:
                                ## Found another category
                                #print("Found another category:", checkIndex)
                                endIndex = checkIndex
                                break
                            checkIndex = checkIndex + 1
                        except:
                            break
                    
                    ## 3. Find ECN device
                    startIndex = 1 if startIndex == -1 else startIndex
                    endIndex = 100 if endIndex == -1 else endIndex
                    #print("startIndex: ", startIndex)
                    #print("endIndex: ", endIndex)
                    while 1:
                        elem = None
                        try:
                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(startIndex) + "]")
                            elem_text = elem.get_attribute("text")
                            if len(elem_text) == 0:
                                ## Found a container
                                #print("Found a container:", startIndex)
                                elem_text = ""
                                try:
                                    elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(startIndex) + "]" + "/*[1]")
                                    elem_text = elem_text + elem.get_attribute("text") + "\n"
                                except:
                                    pass
                                try:
                                    elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(startIndex) + "]" + "/*[2]")
                                    elem_text = elem_text + elem.get_attribute("text")
                                except:
                                    pass
                                #print("Element " , startIndex, ": ", elem_text)
                                if elem_text == valueDict['value_mc'] + "\n" + valueDict['value_ia']:
                                    print("Found ECN device")
                                    ECN_found = True
                                    break
                            startIndex = startIndex + 1
                            if startIndex > endIndex:
                                lastChance = True
                                break
                        except:
                            break
                    
                    if ECN_found == True:
                        break
                    elif lastChance == True:
                        break
                    else:
                        browser.swipe(x1, y1, x2, y2, 2000)
                
                if ECN_found == True:
                    elem.click()
                else:
                    print("Not found ECN device.")
                    raise error.nonamevalue()
        except:
            raise error.equalerror()

    def swipe_up_click(self, browser, valueDict):
        ### Swipe up.
        ###
        ### Required parameters:
        ###     times        : Maximum swipe times.
        ###     
        try:
            swipeTimes = int(valueDict['times'])
            window_bounds = browser.get_window_size()
            x1 = int(window_bounds["width"]) * 0.5
            y1 = int(window_bounds["height"]) * 0.8
            x2 = int(window_bounds["width"]) * 0.5
            y2 = int(window_bounds["height"]) * 0.4
            for i in range(swipeTimes):
                browser.swipe(x1, y1, x2, y2, 2000)
        except:
            raise error.nonamevalue()
    
    #def xpath_find_click(self, browser, valueDict):
    #    ### Swipe up to find target element, and click it.
    #    ###     Maximum swipe   : 10 times
    #    ###
    #    ### Required parameters:
    #    ###     xpath_id        : Element's XPath.
    #    ###     
    #    try:
    #        elem_xpath = valueDict['xpath_id']
    #        elem_loc = ("xpath", elem_xpath)
    #        window_bounds = browser.get_window_size()
    #        x1 = int(window_bounds["width"]) * 0.5
    #        y1 = int(window_bounds["height"]) * 0.8
    #        x2 = int(window_bounds["width"]) * 0.5
    #        y2 = int(window_bounds["height"]) * 0.4
    #        
    #        e = None
    #        for i in range(10):
    #            try:
    #                e = WebDriverWait(browser, 1, 0.5).until(EC.presence_of_element_located(elem_loc))
    #            except:
    #                pass
    #        
    #            if e is not None:
    #                elem = browser.find_element_by_xpath(elem_xpath)
    #                elem.click()
    #                break
    #            elif i < 9:
    #                browser.swipe(x1, y1, x2, y2, 2000)
    #                
    #        if e == None:
    #            raise error.nonamevalue()
    #    except:
    #        raise error.nonamevalue()
