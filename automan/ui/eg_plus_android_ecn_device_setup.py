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
        ###     value_mc        - ECN device name
        ###         Format          : {manufacture code}-{instance number}
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
            valueDict['xpath_id'] in locals().keys()
            valueDict['value_mc'] in locals().keys()
            valueDict['value_ia'] in locals().keys()
            valueDict['value_sc'] in locals().keys()
            valueDict['value_loc'] in locals().keys()
            valueDict['xpath_id'] = config.get('ECHONET_Lite_device_Setup', valueDict['xpath_id'])
            valueDict['value_sc'] = config.get('ECHONET_Lite_device_Setup', valueDict['value_sc'])
            valueDict['value_loc'] = re.search("\[persist.sys.locale\]:\s\[([\s\S]+)\]", valueDict['value_loc'])
            valueDict['value_loc'] = (valueDict['value_loc']).group(1)
            valueDict['value_sc'] = (valueDict['value_sc']).split(";")
            if re.search("ja-", valueDict['value_loc']) != None:
                valueDict['value_sc'] = (valueDict['value_sc'])[1]
            elif re.search("zh-", valueDict['value_loc']) != None:
                valueDict['value_sc'] = (valueDict['value_sc'])[0]
            else:
                valueDict['value_sc'] = (valueDict['value_sc'])[2] 
            print("Category: " + valueDict['value_sc'] + "\n" + \
                "ECN device: " + valueDict['value_mc'] + ", " + valueDict['value_ia'])
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
            for i in range(max_swipe):
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
                ECN_index = 1
                max_swipe = max_swipe - i
                for i in range(max_swipe):
                    ECN_found = False
                    Category_endpoint = False
                    
                    ## Check elements below target category
                    check_elem_index = check_elem_index + 1
                    elem = None
                    try:
                        elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                    except:
                        pass
                    while elem != None:
                        elem_text = elem.get_attribute("text")
                        #print("elem_text: ", elem_text)
                        if len(elem_text) != 0 and elem_text != valueDict['value_sc']:
                            ## Meet another category, exit loop
                            print("Meet another category: " + elem_text)
                            Category_endpoint = True
                            ECN_index = -1
                            break
                        elif len(elem_text) == 0:
                            ## Element is not a cateory, it's a container. So find its child's text.
                            elem_text = ""
                            try:
                                elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]" + "/*[1]")
                                elem_text = elem_text + elem.get_attribute("text") + "\n"
                            except:
                                pass
                            try:
                                elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]" + "/*[2]")
                                elem_text = elem_text + elem.get_attribute("text")
                            except:
                                pass
                            #print("Element " , check_elem_index, ": ", elem_text)
                            if elem_text == valueDict['value_mc'] + "\n" + valueDict['value_ia']:
                                print("Found ECN device")
                                ECN_found = True
                                break
                        check_elem_index = check_elem_index + 1
                        ECN_index = ECN_index + 1
                        elem = None
                        try:
                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                        except:
                            pass
                    if Category_endpoint is True:
                        print("Not find ECN device in target category.")
                        raise error.nonamevalue()
                    if ECN_found is False:
                        #print("Not find ECN device in this page.")
                        #print("Swipe up")
                        browser.swipe(x1, y1, x2, y2, 2000)
                        time.sleep(1)
                        check_elem_index = 1
                        ## If target category is in screen, use "check_elem_index" as before.
                        ## If target category is not in screen, reset "check_elem_index"
                        try:
                            elem_category = None
                            elem_category = browser.find_element_by_xpath("//*[@text=\"" + valueDict['value_sc'] + "\"]")
                            if elem_category is not None:
                                #print("Category still on screen.")
                                ## Get "Category" index
                                check_elem_index = check_elem_index + 1
                                elem = None
                                try:
                                    elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                                except:
                                    pass
                                while elem != None:
                                    elem_text = elem.text if len(elem.text) != 0 else elem.get_attribute("text")
                                    #print("elem_text: ", elem_text)
                                    if elem_text == valueDict['value_sc']:
                                        ## Found target category, exit loop
                                        #print("Found target category, index: ", check_elem_index)
                                        break
                                    else:
                                        check_elem_index = check_elem_index + 1
                                        elem = None
                                        try:
                                            elem = browser.find_element_by_xpath(elem_xpath + "/*[" + str(check_elem_index) + "]")
                                        except:
                                            pass
                        except:
                            pass
                    else:
                        elem.click()
                        break
                print("Swipe times: " + str(i) + ", index: " + str(ECN_index))
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
