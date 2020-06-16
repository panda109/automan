'''
Created on 2010/12/20

0 Mon Dec 20 15:36:16 2010

@author: panda.huang
'''
#   <?xml version="1.0" encoding="US-ASCII"?>
#    <testsuite tests="2" time="" failures="1" error="0" name="[09-07][16-44-18][device_list_1]]">
#      <testcase time="0.0 sec" result="fail" name="test_db_1">
#        <failure message="FAIL !!"/>
#      </testcase>
#      <testcase time="2.0 sec" result="pass" name="test_db">
#      </testcase>
#    </testsuite>
from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAA7ccVMDQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=kLudwcL7NnrteboFxTN6WGXJPrZSFBOn0gvDEE1kjzw%3D'

    bot_message = {
      "cards": [
        {
          "sections": [
            {
              "widgets": [
                {
                  "image": {
                    "imageUrl": "file://www.nextdrive.io/wp-content/uploads/2020/03/Illustration-19-2-e1584596166223.png",
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
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()

#define
#testsuite

#testcase time result name
#failure message

#testsuite