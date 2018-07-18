#coding=big5
'''
Created on 2018年7月13日

@author: Tim.Huang
'''

from fbchat import Client
from fbchat.models import *

class Fb(object):
    def __init__(self):
        '''
        '''
    
    def message_send(self,key):
        client = Client(key['user'], key['password'])
        #print('Own id: {}'.format(client.uid))
        client.send(Message(text=key['message']), thread_id=client.uid, thread_type=ThreadType.USER)
        client.logout()