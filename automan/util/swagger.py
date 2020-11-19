#coding=utf-8
'''
Created on 2010/12/28

@author: panda.huang
'''
import automan.tool.error as error
from automan.tool.verify import Verify
import os,requests
import configparser
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd() , 'ini' , 'test.conf'),encoding="utf-8")

class Swagger(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def eis_health_get(self,dict_value):
        response = requests.get("https://eis-api-qa.nextdrive.io/health")
        ret = response.json()
        if ret['status'] != dict_value['result']:
            raise error.notequalerror()
        return("PASS")
    
    
    def ioe_health_get(self,dict_value):
        response = requests.get("https://ioe-suite-api-qa.nextdrive.io/health")
        ret = response.json()
        if ret['status'] != dict_value['result']:
            raise error.notequalerror()
        return("PASS")

#{"status":"ok","info":{},"error":{},"details":{}}