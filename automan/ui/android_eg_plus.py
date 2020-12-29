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

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', "android_eg_plus.conf"), encoding="utf-8")

class android_eg_plus(object):
    
    def _init_(self):
        pass
    
    
    def element_click(self, browser, dicValue):
        dicParam = dict(dicValue)
        objElement = browser.find_element_by_xpath(config.get("xpath", dicParam['xpath']))
        objElement.click()
        pass

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
        #print(picLocation)
        return picLocation
    
    def sourcePic_get(self, browser, dicValue):
        dicParam = dict(dicValue)
        fileLocation = os.path.join(os.getcwd(), "img", "eg_plus_ui", dicParam["imgFileName"])
        #print("=====> fileLocation")
        #print(fileLocation)
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
        y1 = int(fpHeight * 0.95)
        y2 = int(fpHeight * 0.35)
        browser.swipe(x, y1, x, y2, 3000)
        
        
    def wifi_click(self, browser, dicValue):
        dicParam = dict(dicValue)
        listWifi = browser.find_elements_by_xpath(config.get("xpath", dicParam["xpath"]))
        swipeFlag = True
        swipeTime = 0
        try:
            while swipeFlag:
                for i in range(1, len(listWifi)):
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
        
 
            