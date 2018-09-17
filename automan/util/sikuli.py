# _*_ coding:utf-8 _*_
'''
Created on 2015/04/23
@author: Jack.Lin
Description: Open remote desktop console.

Requirement: pip install -U pyautoit
'''
from jpype import *
from pickle import NONE
import automan.tool.error as error

class Sikuli(object):
    def __init__(self):
        '''
        Constructor
        '''
        jvmPath = getDefaultJVMPath()
        startJVM(jvmPath, '-ea', r'-Djava.class.path=D:\sikuli\sikulixapi.jar')
        self.app = JClass('org.sikuli.script.App')
        Screen = JClass('org.sikuli.script.Screen')
        self.screen = Screen()

    def icon_hover(self, name):
        try:
            x =  self.screen.exists(name['key'])
            if x != "None":
                self.screen.hover(name['key'])
            else:
                raise error.notfind()
        except:
            raise error.notfind()
        
    def icon_wait(self, name):
        try:
            x = self.screen.wait(name['key'],name['value'])
            if x == "None":
                raise error.notfind()
        except:
            raise error.notfind()
        
    def icon_click(self, name):
        try:
            x =  self.screen.exists(name['key'])
            if x != "None":
                self.screen.click(name['key'])
            else:
                raise error.notfind()
        except :
            raise error.notfind()
            
    def text_type(self,text):
        try:
            self.screen.type(text['value'])
        except:
            raise error.notfind()
        
    def enter_type(self):
        try:
            self.screen.type("\n")
        except:
            raise error.notfind()
                
    def __del__(self):
        shutdownJVM()