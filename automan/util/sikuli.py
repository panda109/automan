# _*_ coding:utf-8 _*_
'''
Created on 2015/04/23
@author: Jack.Lin
Description: Open remote desktop console.

Requirement: pip install -U pyautoit
'''
from jpype import *
import  jpype
from pickle import NONE
import automan.tool.error as error

class Sikuli(object):
    def __init__(self):
        '''
        Constructor
        '''
        jvmPath = jpype.getDefaultJVMPath()
        jpype.startJVM(jvmPath, '-ea', r'-Djava.class.path=sikulixapi.jar')
        self.app = jpype.JClass('org.sikuli.script.App')
        self.Screen = jpype.JClass('org.sikuli.script.Screen')
        self.sn = self.Screen()
        
    def icon_hover(self, name):
        try:
            x =  self.sn.exists(name['key'])
            if x != "None":
                self.sn.hover(name['key'])
            else:
                raise error.notfind()
        except:
            raise error.notfind()
        
    def icon_wait(self, dict):
        try:
            x = self.sn.wait(dict['key'],int(dict['sec']))
            if x == False:
                raise error.notfind()
        except:
            raise error.notfind()

    def icon_waitvanish(self, dict):
        try:
            x = self.sn.wait(dict['key'],int(dict['sec']))
            if x == False:
                raise error.find()
        except:
            raise error.find()
        
    def icon_click(self, name):
        try:
            x =  self.sn.exists(name['key'])
            if x != "None":
                self.sn.click(name['key'])
            else:
                raise error.notfind()
        except :
            raise error.notfind()
            
    def text_type(self,text):
        try:
            self.sn.type(text['value'])
        except:
            raise error.notfind()
        
    def enter_type(self):
        try:
            self.sn.type("\n")
        except:
            raise error.notfind()
                
    def __del__(self):
        jpype.shutdownJVM()
