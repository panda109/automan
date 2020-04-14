#coding:utf-8
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
import pyscreenshot as ImageGrab

class Execute_qa(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.each_session = []
        self.until_session = []
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
            print ('The '+str(index+1)+'th testcase\'s name is : '+qa_list[index]+'\n')
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
        until_mode = False
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
            elif command[1] == 'until' and command[2] == 'start':
                self.until_session.append(command)
                until_mode = True
            elif command[1] == 'until' and command[2] == 'end':
                result = self.execute_until_session()
                self.until_session = []
                until_mode = False
            elif until_mode == True:
                self.until_session.append(command)
            else:
                result = self.execute_normal_session(command)
            
                
                
            if command[1] != 'end' :
                if result == 1 and str(self.systemini['screenshot'])=='yes' :
                    self.screenshot()

                elif str(self.systemini['screenshot'])=='step' :
                    self.screenshot()
                 
            elif command[1] == 'end' : 
                if str(self.systemini['screenshot'])=='force'  :
                    self.screenshot()
          
        status = self.log.finall_status()
        #print status
        if status == False:
            print ("[VP] = " + 'FAIL\n\n')
        else:
            print ("[VP] = " + 'PASS\n\n')

    def screenshot(self):
        if len(self.qa_list) == 1 :
            SaveDirectory = os.getcwd()
            SaveAs = os.path.join(SaveDirectory,'log\\'  + self.qa_file.split(".")[0] + "\\"
                    + time.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg')
            im=ImageGrab.grab()
            time.sleep(2)
            #print (SaveAs)
            im.save(SaveAs)
            #ImageGrab.grab_to_file(SaveAs)
        else:
            self.nowcase = self.nowcase.rstrip(".qa")
            self.nowcase = self.nowcase.lstrip(".\\qa\\")
            qas = self.qa_file.split('.')[0]

            if self.nowcase.find("\\") != -1 :
                self.nowcase = self.nowcase.split('\\')[1]
                
            SaveDirectory = os.getcwd()
            os.mkdir(SaveDirectory + "\\log\\" + qas + "\\" + self.nowcase + "\\")
            SaveAs = os.path.join(SaveDirectory,'log\\' + qas + "\\" + self.nowcase + "\\"
                + time.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg')
            im=ImageGrab.grab()
            time.sleep(2)
            ImageGrab.grab_to_file(SaveAs)
            
    def execute_until_session(self):
        result=1
        print("1111")
        print(self.until_session[0])
        if self.until_session[0][3].find("!loop!") != -1:
            loop = self.until_session[0][3].split('=')[1]
            command = ""
            for param in range(int(loop)):
                for command in self.until_session[1:]:
                    temp_list = []
                    temp_list = temp_list + command
                    param = param + 1
                    temp_list[-1] = str(command[-1]).replace('$$', str(param))

                    result = self.executer.execute(command,self.systemini)
                    time.sleep(int(str(self.systemini['sleep'])))
                    
                    if result == 0:
                        self.log.parse_log(result,command)
                        return
            self.log.parse_log(result,command)
            return  result
            
    def execute_each_session(self):
        #replace $$
        result=0
        
        if self.each_session[0][3].find("!loop!") != -1:
            loop = self.each_session[0][3].split('=')[1]
            for param in range(int(loop)):
                for command in self.each_session[1:]:
                    temp_list = []
                    temp_list = temp_list + command
                    param = param + 1
                    temp_list[-1] = str(command[-1]).replace('$$', str(param))
                    result = self.execute_normal_session(temp_list)
                    if result == 1 and str(self.systemini['keepgoon'])=='no':
                        break
                if result == 1 and str(self.systemini['keepgoon'])=='no':
                    break
            
        if self.each_session[0][3].find(",") != -1:
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