'''
Created on 2010/12/20

0 Mon Dec 20 15:36:16 2010

@author: panda.huang
'''
#pip install pipwin
#pipwin install pyaudio
from httplib2 import Http
from json import dumps

if __name__ == '__main__':
    
    url = 'https://chat.googleapis.com/v1/spaces/AAAAfHdGUII/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=FWHoi6eGb0FW9KxtTg4YDfd-HpHAix1qF68IhqmCdso%3D'
    bot_message = {
        'text' : 'EIS Swagger test finished!!'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )


