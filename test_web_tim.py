'''
Created on 2011/2/14

@author: panda109
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_web(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    if __name__ == '__main__':

        driver = webdriver.Ie()
        driver.get('http://google.com.tw')
        #driver = webdriver.Firefox()
        #driver.get("http://www.python.org")
        elem = driver.find_element_by_name('q')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        for handle in driver.window_handles:
            print "Handle = ",handle
        #driver.close()