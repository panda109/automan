# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:22:29 2020

@author: Dustin Lin
"""
from appium import webdriver
import time
import automan.tool.error as error
import configparser
import os
import aircv as ac
import subprocess
import automan.util.tool as tool
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "eg_plus_android.conf"), encoding="utf-8")

class eg_plus_android(object):
    
    def _init_(self):
        pass
    
    
    def element_click(self, browser, dicValue):
        ## Roger: Need to handle exception to prevent unexpected stop
        try:
            dicParam = dict(dicValue)
            
            ## Roger: Elements will not show on screen immediately
            elem_xpath = config.get("xpath", dicParam['xpath'])
            elem_loc = ("xpath", elem_xpath)
            WebDriverWait(browser, 120, 1).until(EC.presence_of_element_located(elem_loc))
    
            objElement = browser.find_element_by_xpath(config.get("xpath", dicParam['xpath']))
            objElement.click()
        except TimeoutException:
            raise error.nonamevalue()
        except:
            raise error.nonamevalue()

    def element_set(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            objElement = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
            objElement.send_keys(dicParam["strValue"])
        except:
            raise error.notfind()            
        
    def keyboard_hide(self, browser):
        browser.hide_keyboard()
        
    def input_location_tap(self, browser, dicValue):
        #input (x,y) 
        dicParam = dict(dicValue)
        screen_width = browser.get_window_size()['width']
        screen_height = browser.get_window_size()['height']
        x = (float(dicParam['x_axis'])/screen_width) * screen_width
        y = (float(dicParam['y_axis'])/screen_height) * screen_height
        browser.tap([(x, y), (x, y)], duration = 100)
        
    def bleCmd_set(self, browser, dicValue):
        #trigger cube broadcast
        dicParam = dict(dicValue)
        objCmd = subprocess.Popen('adb -s {} shell'.format(dicParam["targetCubeName"]), shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        objCmd.stdin.write("sendevent /dev/input/event0 0001 0116 00000001\n".encode("utf-8"))
        objCmd.stdin.write("sendevent /dev/input/event0 0000 0000 00000000\n".encode("utf-8"))
        objCmd.stdin.write("sendevent /dev/input/event0 0001 0116 00000000\n".encode("utf-8"))
        objCmd.stdin.write("sendevent /dev/input/event0 0000 0000 00000000\n".encode("utf-8"))
        objCmd.stdin.write('exit\n'.encode('utf-8'))
    
    def cubeNameChange_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            strCubeName = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"])).text
            if strCubeName == dicParam["strValue"]:
                pass
            else:
                raise error.equalerror()  
        except:
            raise error.equalerror()  
        

    def pic_format_verify(self, filename):
        return filename.endswith(".png")
        
    def targetPic_get(self, browser, dicValue):
        dicParam = dict(dicValue)
        folderLocation = os.path.join(os.getcwd(), "log", dicParam["logFolderName"])
        #print(folderLocation)
        fileNames = os.listdir(folderLocation)
        objFilename = filter(self.pic_format_verify, fileNames)
        listFilename = list(objFilename)
        listRevFilename = listFilename[::-1]
        #print(listRevFilename)
        
        picLocation = folderLocation + "\\" + listRevFilename[0]
        print("Target image path: ", picLocation)
        return picLocation
    
    def sourcePic_get(self, browser, dicValue):
        dicParam = dict(dicValue)
        fileLocation = os.path.join(os.getcwd(), "img", dicParam["imgFileName"])
        #print("=====> fileLocation")
        print("Source image path: ", fileLocation)
        return fileLocation 

    def authority_verify(self, browser, dicValue):
        #first time open app will ask permission
        dicParam = dict(dicValue)
        try:
            authoBoxBtn = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
            authoBoxBtn.click()
            
        except:
            print("No need to confirm")
            pass   
        
    def smSetup_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        listDevice = []
        try:
            dashboard = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
            print(dashboard)
            for device  in range(1, len(dashboard)):
                
                #strCurrentDeviceName = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]) + "[{}]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]".format(device + 1)).text
                strCurrentDeviceName = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]) + config.get("xpath", dicParam["deviceName"]).format(device + 1)).text
                listDevice.append(strCurrentDeviceName)
            print(listDevice)
            if dicParam["strDeviceName"] in listDevice:
                pass
            else:
                error.equalerror()
        except:
            raise error.equalerror()
        
    def cubeRemove_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            objDeviceList = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
        except:
            raise error.equalerror()
        
    def gwSetup_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            objElement = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
        except:
            raise error.notfind()
        
    def cube_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        flag = True
        retryTime = 0
        while flag:
            strCubeName = browser.find_element_by_xpath(config.get("xpath", dicParam["cubeNameXpath"])).text
            print("=====> current cube id: ", strCubeName)
            if strCubeName == dicParam["targetCubeName"]:
                #nextBtn = browser.find_element_by_xpath(config.get("xpath", dicParam["nextBtnXpath"])).click()
                flag = False
            else:
                searchAgainBtn = browser.find_element_by_xpath(config.get("xpath", dicParam["searchAgainBtnXpath"])).click()
                flag = True
                retryTime = retryTime + 1
                print("=====>", retryTime)
                try:
                    searchCubeFlag = browser.find_element_by_xpath(config.get("xpath", dicParam["searchCubeXpath"]))
                    print("no Cube found")
                    noCubeFoundBtn = browser.find_element_by_xpath(config.get("xpath", dicParam["noCubeFoundXpath"])).click()
                    flag = False
                except:
                    if retryTime >= 10:
                        flag = False
                        print("cannot find cube")
                    else:
                        pass
            time.sleep(1)
            
            
    def noCubeFound_verify(self, browser, dicValue):
        #for searching_cube
        dicParam = dict(dicValue)

        try:
            while True:
                searchAgainBtn = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
                searchAgainBtn.click()

        except:
            pass
        
    def up_swipe(self, browser):
        size = browser.get_window_size()
        fpWidth = size.get("width")
        fpHeight = size.get("height")
        x = int(fpWidth * 0.5)
        y1 = int(fpHeight * 0.75)
        y2 = int(fpHeight * 0.35)
        browser.swipe(x, y1, x, y2, 3000)
        
    def wifi_click(self, browser, dicValue):
        dicParam = dict(dicValue)
        listWifi = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
        swipeFlag = True
        swipeTime = 0
        try:
            while swipeFlag:
                ##  20210201, Roger: The "end" of range must +1
                for i in range(1, (len(listWifi) + 1)):
                    strWifiItem = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]) + "[{}]".format(i) + "/android.widget.TextView")
                    strWifiSsid = strWifiItem.text
                    print(strWifiSsid)
                    if strWifiSsid == dicParam["wifiName"]:
                        strWifiItem.click()
                        swipeFlag = False
                        break
                    else:
                        pass
                if swipeFlag == True:
                    self.up_swipe(browser)
                    swipeTime = swipeTime + 1
                    if swipeTime == 5:
                        swipeFlad == False
                        break
                    else:
                        pass
                else:
                    pass
        except:
            raise error.notfind()

    def left_swipe(self, browser):
        
        size = browser.get_window_size()
        width = size.get('width')
        height = size.get('height')       
        x1 = int(width * 0.9)
        y1 = int(height * 0.5)
        x2 = int(width * 0.1)
        browser.swipe(x1, y1, x2, y1, 1000)
    
    def keyboard_hide(self, browser):
        
        browser.hide_keyboard()
    
    def email_addr_get(self, browser):
        
        ts = calendar.timegm(time.gmtime())
        email_addr = "ndtestmail+{}@mailto.plus".format(ts)
        return email_addr
    
    def verification_code_from_web_get(self, browser):
    
        vc.get_verification_code_from_web()
        
    def verification_code_from_file_get(self, browser):
        
        f = open(os.path.join(os.getcwd(), "verification_code.txt"),'r')
        code = f.read()
        f.close()
        return code
    
    def ecnDeviceType_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        swipeFlag = True
        swipeTime = 0
        target_type = "エアコン".encode('utf-8')
        print("target_type: {}".format(target_type))
        try:
            while swipeFlag:
                try:
                    time.sleep(1)
                    objEcnDeviceType = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
                    strEcnDeviceType = objEcnDeviceType.text
                    byteEcnDeviceType = strEcnDeviceType.encode('utf-8')
                    print("Read: {}".format(byteEcnDeviceType))
                    if byteEcnDeviceType == target_type:
                        swipeFlag = False
                        break
                    else:
                        self.up_swipe(browser)
                except:
                    self.up_swipe(browser)
                swipeTime = swipeTime + 1
                if swipeTime >= 50:
                    swipeFlag = False
                    raise error.notfind()
                else:
                    pass
        except:
            raise error.notfind()
        
    def screen_take(self,browser):
        browser.save_screenshot('./log/app.png')
    
    def device_setup_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        listDevice = []
        try:
            dashboard = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
            print(dashboard)
            for device  in range(1, len(dashboard)):
                
                #strCurrentDeviceName = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]) + "[{}]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]".format(device + 1)).text
                strCurrentDeviceName = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]) + config.get("xpath", dicParam["deviceName"]).format(device + 1)).text
                listDevice.append(strCurrentDeviceName)
            print(listDevice)
            if dicParam["strDeviceName"] in listDevice:
                pass
            else:
                error.equalerror()
        except:
            raise error.equalerror()
    
    def element_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            element_on_screen = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
            element_on_screen.click()
        except:
            raise error.notfind()
          
    def dashboard_no_device_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        try:
            dashboard_device_list = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
            print(len(dashboard_device_list))
            if len(dashboard_device_list) == 1:
                print("There is no other device")
            else:
                print("There is a device not remove yet")
                raise error.equalerror()
        except:
            raise error.notfind()
            
                        
    def down_swipe(self, browser):
        size = browser.get_window_size()
        fpWidth = size.get("width")
        fpHeight = size.get("height")
        x = int(fpWidth * 0.5)
        y1 = int(fpHeight * 0.35)
        y2 = int(fpHeight * 0.75)
        browser.swipe(x, y1, x, y2, 2000)
        
    def string_not_equal_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        swipeFlag = True
        swipeTime = 0
        try:
            
            #print("target: ", dicParam["string_value"])
            print(config.get("text", dicParam["text"]))
            self.down_swipe(browser)
            while swipeFlag:
                time.sleep(2)
                #if str_update_time_text == "- -:- -":
                #if str_update_time_text == dicParam["string_value"]:
                str_update_time_text = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"])).text
                print("current text: ", str_update_time_text)
                if str_update_time_text == config.get("text", dicParam["text"]):
                    self.down_swipe(browser)
                    swipeTime = swipeTime + 1
                    if swipeTime >= 30:
                        raise error.notfind()
                        break
                    else:
                        pass
                else:
                    swipeFlag = False
                    print("swipe time: {}".format(swipeTime))
        except:
            raise error.notfind()
            
    def string_equal_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        swipeFlag = True
        swipeTime = 0
        try:
            
            #print("target: ", dicParam["string_value"])
            print(config.get("text", dicParam["text"]))
            self.down_swipe(browser)
            while swipeFlag:
                time.sleep(2)
                #if str_update_time_text == "- -:- -":
                #if str_update_time_text == dicParam["string_value"]:
                str_update_time_text = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"])).text
                print("current text: ", str_update_time_text)
                if str_update_time_text != config.get("text", dicParam["text"]):
                    self.down_swipe(browser)
                    swipeTime = swipeTime + 1
                    if swipeTime >= 30:
                        raise error.notfind()
                        break
                    else:
                        pass
                else:
                    swipeFlag = False
                    print("swipe time: {}".format(swipeTime))
        except:
            raise error.notfind()            
    def gateway_found_search_again_verify(self, browser, dicValue):
        dicParam = dict(dicValue)
        clickFlag = 0
        try:
            while clickFlag <= 5:
                time.sleep(2)
                try:
                    obj_search_again_btn = browser.find_element_by_xpath(config.get("xpath", dicParam["xpath"]))
                    obj_search_again_btn.click()
                    clickFlag = 0
                except:
                    clickFlag = clickFlag + 1
                    pass
        except:
            raise error.notfind()
            
    def server_type_set(self, browser, valueDict):
        ##  Purpose:
        ##      1. Set persist.server.type to qa/production.
        ##      2. Reboot gateway.
        ##
        ##  Required parameters:
        ##      stage       - QA staging / Production staging
        ##      name        - Gateway's name 
        ##
        try:
            if valueDict['stage'] == "qa":
                command = "adb -s " + valueDict['name'] + " shell \"setprop persist.next.server.type qa\""
                response = ""
                out = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in out.stdout:
                    line = line.rstrip()
                    response += line.decode("big5", "ignore")
                
                command = "adb -s " + valueDict['name'] + " shell \"reboot\""
                out = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in out.stdout:
                    line = line.rstrip()
                    response += line.decode("big5", "ignore")
                print(response)
            else:
                pass
        except:
            raise error.nonamevalue()
            