#coding=big5
'''
Created on 2018年7月13日

@author: Tim.Huang
'''
import datetime
from fbchat import Client
from fbchat.models import *

class Fb(object):
    def __init__(self):
        '''
        '''
    
    def message_send(self,key):
        client = Client(key['user'], key['password'])
        #print('Own id: {}'.format(client.uid))
        now = datetime.datetime.now()
        text=key['message']
        text = text + " at " + now.strftime("%Y-%m-%d %H:%M:%S")
        client.send(Message(text), thread_id=client.uid, thread_type=ThreadType.USER)
        client.logout()