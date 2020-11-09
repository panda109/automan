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
#import Pillow
import shutil
import os

if __name__ == '__main__':
    for file in next(os.walk(os.path.join(os.getcwd() , 'temp')))[2]:  
        source = (os.path.join(os.getcwd(),"temp",file))
        dist = (os.path.join(os.getcwd(),"temp1",file))
        shutil.copy(source , dist)
        os.remove(source)
        
        

#define
#testsuite

#testcase time result name
#failure message

#testsuite