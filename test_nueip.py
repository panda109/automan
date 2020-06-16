# coding=big5
'''
Created on 2011/2/14

@author: panda109
'''
from selenium import webdriver
from appium import webdriver as appium
from automan.tool.parse_file import Parse_file
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time,os
from _ast import If
class test_web(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    if __name__ == '__main__':
        #driver = webdriver.Chrome() aaa
        driver_path = os.getcwd() + '/chromedriver'
        browser = webdriver.Chrome(driver_path)
        browser.get("https://cloud.nueip.com/attendance_record")
        time.sleep(1)
        elem = browser.find_element_by_id('dept_input')
        elem.send_keys("nextdrive")
        elem = browser.find_element_by_id('username_input')
        elem.send_keys("XXXXXX")
        elem = browser.find_element_by_id('password-input')
        elem.send_keys("XXXXX")
        
        elem = browser.find_element_by_id('login-button')
        elem.click()
        
        elem = browser.find_element_by_id('filiter_week')
        elem.click()
        time.sleep(1)
        #get table
        table = browser.find_element_by_xpath('//table[@class="table dataTable no-footer nueip-reflow-dataTable-md reflow-table"]')
        #get rows
        trList = table.find_elements_by_tag_name("tr")
        cols = []
        ln = len(trList)
        index = 0
        for row in trList[::-1]:
              tdList = row.find_elements_by_tag_name("td")
              for col in tdList:
                cols.append(col)
              try : 
                if (cols[4].text.find('日') == -1  and cols[4].text.find('六')) == -1:
                    print(cols[4].text)
                    cols[0].click()
                    time.sleep(2)
                    elem = browser.find_element_by_id('clockin')
                    elem.click()
                    elem = Select(browser.find_element_by_name('hour'))
                    elem.select_by_value('09')
                    elem = browser.find_element_by_name('remark')
                    elem.send_keys("Forget checkin")
                    elem = browser.find_element_by_id('ModalSave')
                    elem.click()
                       
                    cols[0].click()
                    time.sleep(2)
                    elem = browser.find_element_by_id('clockout')
                    elem.click()
                    elem = Select(browser.find_element_by_name('hour'))
                    elem.select_by_value('19')
                    elem = browser.find_element_by_name('remark')
                    elem.send_keys("Forget checkin")
                    elem = browser.find_element_by_id('ModalSave')
                    elem.click()
              except :
                  pass
              cols = []
              index = index + 1
              if index == ln:
                  break
    browser.quit()    
              




