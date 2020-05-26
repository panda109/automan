# -*- coding: utf-8 -*-
'''
Created on 2020/05/09
Tools for web testing

@author: Shawn Lin
'''

def GetWebPageElement(objBrowser,strType,strXPath,strElemName):
    '''
    Return the element object in a web page by its id, name or xpath infor
    objBrowser: a selenium browser object
    
    ref: https://selenium-python.readthedocs.io/locating-elements.html
    '''
    if strType == 'xpath':
        objElement = objBrowser.find_element_by_xpath(strXPath)
    elif strType == 'id':
        objElement = objBrowser.find_element_by_id(strElemName)
    elif strType == 'name':
        objElement = objBrowser.find_element_by_name(strElemName)
    return objElement
