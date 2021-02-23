#coding=big5
'''
Created on 2018年7月13日

@author: Tim.Huang
'''
import datetime
from fbchat import Client
from fbchat.models import *
from httplib2 import Http
from json import dumps

class Fb(object):
    def __init__(self):
        '''
        '''
    
    def fbmessage_send(self,key):
        client = Client(key['user'], key['password'])
        #print('Own id: {}'.format(client.uid))
        now = datetime.datetime.now()
        text=key['message']
        text = text + " at " + now.strftime("%Y-%m-%d %H:%M:%S")
        client.send(Message(text), thread_id=client.uid, thread_type=ThreadType.USER)
        client.logout()
        
    def googlemessage_send(self,key):

        url = 'https://chat.googleapis.com/v1/spaces/AAAAfHdGUII/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=FWHoi6eGb0FW9KxtTg4YDfd-HpHAix1qF68IhqmCdso%3D'
        bot_message = {
            'text' : key['message']}
    
        message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    
        http_obj = Http()
    
        http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )