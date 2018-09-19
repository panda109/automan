'''
Created on 2010/12/22

@author: panda.huang
Add print screen (Kevin Chang 2015/06/17)
'''
import os

import time
from automan.tool.execute_command import Execute_command
from automan.tool.log import Log
from automan.tool.parse_file import Parse_file
import datetime
#import pyscreenshot as ImageGrab

class Execute_qa(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.each_session = []
        self.for_session = []
        self.executer = Execute_command()
        '''
        Constructor
        '''
    
    def execute_qa_list(self,qa_file,qa_list):
        self.qa_list = qa_list
        self.qa_file = qa_file
        self.log = Log(qa_file,qa_list)
        for index in range(len(qa_list)):
            self.nowcase = qa_list[index]
            print 'The '+str(index+1)+'th testcase\'s name is : '+qa_list[index]+'\n'
            self.commands = Parse_file().parse_qa(qa_list[index])
            self.systemini = Parse_file().get_ini('system.ini')
            self.commandline(self.commands)
            self.log.parse_case_log(index)
            self.log.result = []
        # sum all qas's log into qas's folder
        self.log.create_hudson_xml()
        
    def commandline(self,commands):
        """
        execution : python qafilname.qa
        """
        os.chdir(os.getcwd())
        each_mode = False
        for command in list(commands):
            if command[1] == 'each' and command[2] == 'start':
                self.each_session.append(command)
                each_mode = True
            elif command[1] == 'each' and command[2] == 'end':
                result = self.execute_each_session()
                self.each_session = []
                each_mode = False
            elif each_mode == True:
                self.each_session.append(command)
            else:
                result = self.execute_normal_session(command)
                #print "=============", result
            if result == 1 and str(self.systemini['keepgoon'])=='no':
                if str(self.systemini['screenshot'])=='yes':
                    self.screenshot()
                    break
                else:
                    break
            if ( result == 1 and str(self.systemini['screenshot'])=='yes'
            and str(self.systemini['keepgoon'])=='yes'):
                self.screenshot()

        status = self.log.finall_status()
        if status == False:
            print "[VP] = " + 'FAIL\n\n'
        else:
            print "[VP] = " + 'PASS\n\n'

    def screenshot(self):
        if len(self.qa_list) == 1 :
            SaveDirectory = os.getcwd()
            SaveAs = os.path.join(SaveDirectory,'log\\'  
                    + time.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg')
            im=ImageGrab.grab()
            time.sleep(2)
            ImageGrab.grab_to_file(SaveAs)
        else:
            self.nowcase = self.nowcase.rstrip(".qa")
            self.nowcase = self.nowcase.lstrip(".\\qa\\")
            SaveDirectory = os.getcwd()
            os.mkdir(SaveDirectory + "\\log\\" + self.nowcase)
            SaveAs = os.path.join(SaveDirectory,'log\\' + self.nowcase + "\\" 
                + time.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg')
            im=ImageGrab.grab()
            time.sleep(2)
            ImageGrab.grab_to_file(SaveAs)
            
    def execute_each_session(self):
        #replace $$
        for param in str(self.each_session[0][3]).split(','):
            for command in self.each_session[1:]:
                temp_list = []
                temp_list = temp_list + command
                temp_list[-1] = str(command[-1]).replace('$$', param)
                result = self.execute_normal_session(temp_list)
                if result == 1 and str(self.systemini['keepgoon'])=='no':
                    break
            if result == 1 and str(self.systemini['keepgoon'])=='no':
                break            
        return result
        
    def execute_normal_session(self,command):
        result = self.executer.execute(command,self.systemini)
        self.log.parse_log(result,command)
        time.sleep(int(str(self.systemini['sleep']))) 
        return result