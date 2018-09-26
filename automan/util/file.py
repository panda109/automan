'''
Created on 2010/12/28

@author: panda.huang
'''
import hashlib
import automan.tool.error as error
import os
from automan.tool.verify import Verify

class File(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def rdfolder_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1
        
    def mdfolder_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1    
    
    def smbnetuse_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1

    def copy_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1

    def download_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1

    def copy_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1

    def clean_exec(self,dict):
        try:
            os.system(dict['command'])
            return 0
        except:
            return 1

    def getmd5_get(self,dict):
        hash_md5 = hashlib.md5()
        with open(dict['file'], "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    
    def equalmd5_verify(self,dict):
        if (dict['md5'] == dict['ldmd5']):
            return 0
        else:
            raise error.notequalerror()
        