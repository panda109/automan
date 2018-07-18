'''
Created on 2010/12/10
@author: panda.huang
'''
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
class Google(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass
    def textbox_search_set(self,ie,value_dict):
        local_dict = dict(value_dict)
        elem = ie.find_element_by_name('q')
        elem.send_keys(local_dict["key"] )

    def button_submit_click(self,ie):
        elem = ie.find_element_by_name('q')
        elem.send_keys(Keys.RETURN)

    def button_error_click(self,ie):
        raise
