'''
Created on 2011/2/14

@author: panda109
'''
import time
from appium import webdriver

class test_web(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    if __name__ == '__main__':
        dc = {}
        dc['platformName'] = 'Android'
        dc['deviceName'] = 'GCNPCX025651GHH'
        dc['appActivity'] = ''
        dc['appWaitActivity'] =''
        webdriver.Remote('localhost:4723/wd/hub', desired_capabilities=dc)