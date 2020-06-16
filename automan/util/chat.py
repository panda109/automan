#coding=big5
'''
Created on 2018年7月13日

@author: Tim.Huang
'''
from httplib2 import Http
from json import dumps

class chat(object):
    def __init__(self):
        '''
        '''
    
    def message_send(self,key):
        print(key)
        URL = key['uri']
        message = key['message']
        bot_message = {
            'text' : message}
    
        message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    
        http_obj = Http()
    
        response = http_obj.request(
            uri=URL,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )
        #print(response)
        
    def message_sendpic(self,key):
        URL = key['uri']
        imageurl = key['imageurl']
        #print('Own id: {}'.format(client.uid))
        bot_message = {
          "cards": [
            {
              "sections": [
                {
                  "widgets": [
                    {
                      "image": {
                        "imageUrl": imageurl,
                        "onClick": {
                          "openLink": {
                            "url": "https://www.nextdrive.io/"
                          }
                        }
                      }
                    }
                  ]
                }
              ]
            }
          ]
        }
    
        message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    
        http_obj = Http()
    
        response = http_obj.request(
            uri=URL,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )
        #print(response)