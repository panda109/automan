#coding=utf-8
'''
Created on 2015/04/28

@author: Jason Ma
'''
import time
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
from automan.util.tool  import Tool
import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

config = ConfigParser.ConfigParser()
config.read(".\ini\Eonone.conf")


class eonone_sharefolder(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass
#layer 2
    def newfolder_click(self, browser):
        text = config.get("setting", "class_new_button")
        xpath="//button[@class='replace ']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(browser).move_to_element(elem)
        Hover.click().perform()
        #print elem.text

#layer 3 : popup
    def popup_comfirm_click(self, browser):
        text = config.get("sharefolder_popup", "class_comfirm_button")
        xpath="//button[@ng-click='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(browser).move_to_element(elem)
        Hover.click().perform()

#lauer 3 : common
    def aclsetfolder_click(self, browser):
        text = config.get("sharefolder_common", "class_aclsetfolder_button")
        xpath="//ul//li[contains(.,'replace')]"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(browser).move_to_element(elem)
        Hover.click().perform()

    def save_click(self, browser):
        text = config.get("sharefolder_common", "class_save_button")
        xpath="//button[@ng-click='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(browser).move_to_element(elem)
        Hover.click().perform()

#layer 3 : quota

#layer 3 : hash

#layer 3 : permission

#layer 3 : normal
    def nor_checkbox_smbandcifs_click(self, browser):
        text = config.get("sharefolder_normail", "ng-model_smbandcifs_text")
        xpath="//input[@ng-model='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(browser).move_to_element(elem)
        Hover.click().perform()
        
    def nor_text_foldername_set(self, browser, value_dict):
        local_dict = dict(value_dict)
        text = config.get("sharefolder_normail", "placeholder_folder_text")
        xpath="//input[@placeholder='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(browser).move_to_element(elem)
        elem.send_keys(local_dict["key"])

    def nor_text_sharefoldername_set(self, browser, value_dict):
        local_dict = dict(value_dict)
        text = config.get("sharefolder_normail", "placeholder_sharefolder_text")
        xpath="//input[@placeholder='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(browser).move_to_element(elem)
        #elem.clear()
        elem.send_keys(local_dict["key"])

    def nor_text_sharefoldername_clear(self, browser):
        text = config.get("sharefolder_normail", "placeholder_sharefolder_text")
        xpath="//input[@placeholder='replace']"
        elem = browser.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(browser).move_to_element(elem)
        elem.clear()