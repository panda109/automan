#coding:utf-8
'''
Created on 2010/12/10
@author: panda.huang
'''
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
class google(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass
    def textbox_search_set(self,browser,value_dict):
        local_dict = dict(value_dict)
        elem = browser.find_element_by_name('q')
        elem.send_keys(local_dict["key"])
        #elem.send_keys("中".decode('utf-8'))
        
    def button_submit_click(self,browser):
        elem = browser.find_element_by_name('q')
        elem.send_keys(Keys.RETURN)

    def button_error_click(self,browser):
        raise
    
    def text_gmail_print(self,browser):
        elem = browser.find_element_by_class_name('gb_g')
        print(elem.text)
