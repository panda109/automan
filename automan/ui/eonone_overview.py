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


class eonone_overview(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass

    def sharefolder_click(self, ie):
        text = config.get("overview", "class_sharefolder")
        xpath="//div[@class='replace']"
        elem = ie.find_element_by_xpath(xpath.replace("replace",text))
        Hover = ActionChains(ie).move_to_element(elem)
        Hover.click().perform()
        #print elem.text
