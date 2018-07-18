# _*_ coding:utf-8 _*_
'''
Created on 2015/04/23
@author: Jack.Lin
Description: Open remote desktop console.

Requirement: pip install -U pyautoit
'''
from jpype import *
from pickle import NONE

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
            self.screen.hover(name['key'])

    def icon_wait(self, name):
            self.screen.wait(name['key'],name['value'])

    def icon_click(self, name):
        x =  self.screen.exists(name['key'])
        if x != "None":
            self.screen.click(name['key'])
        else:
            raise
         
    def text_type(self,text):
        self.screen.type(text['value'])

    def enter_type(self):
        self.screen.type("\n")
                
    def __del__(self):
        shutdownJVM()