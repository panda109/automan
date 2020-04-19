'''
Created on 2011/2/14

@author: panda109
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from saker.fuzzers.fuzzer import Fuzzer 
from saker.core.mutator import Mutator
from saker.brute.brute import Brute
from saker.cmdline.fuzz import fuzz

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
        driver.get('https://www.hepsiburada.com/')
        
        options = {
            "url": "http://127.0.0.1:7777/",
            "params": {
                "test": "test"
            }
        }
           
        mut = Mutator({}) 
        for payload in mut.fuzzdata('/v1/service/',"ssrf")   :
            print (payload)   
        print (Fuzzer.randomCStr(129))
        #driver = webdriver.Firefox()
        #driver.get("http://www.python.org")
        #elem = driver.find_element_by_name('q')
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #for handle in driver.window_handles:
        #    print "Handle = ",handle
        #driver.close()