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

    def new_folder_click(self, ie):
        text = config.get("sharefolder", "class_new_button")
        xpath="//button[@class='replace ']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(ie).move_to_element(elem)
        Hover.click().perform()
        #print elem.text

    def checkbox_smbandcifs_click(self, ie):
        text = config.get("sharefolder_new", "ng-model_smbandcifs_text")
        xpath="//input[@ng-model='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(ie).move_to_element(elem)
        Hover.click().perform()
        
    def foldername_set(self, ie, value_dict):
        local_dict = dict(value_dict)
        text = config.get("sharefolder_new", "validate_folder_text")
        xpath="//input[@validate='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(ie).move_to_element(elem)
        elem.send_keys(local_dict["key"])

    def sharefoldername_set(self, ie, value_dict):
        local_dict = dict(value_dict)
        text = config.get("sharefolder_new", "validate_sharefolder_text")
        xpath="//input[@validate='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(ie).move_to_element(elem)
        elem.clear()
        elem.send_keys(local_dict["key"])

    def sharefoldername_clear(self, ie):
        text = config.get("sharefolder_new", "validate_sharefolder_text")
        xpath="//input[@validate='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        #Hover = ActionChains(ie).move_to_element(elem)
        elem.clear()