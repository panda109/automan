'''
Created on 2010/12/10

@author: panda.huang
'''
import time
import os
from automan.tool.parse_file import Parse_file
from automan.tool.userclass import Userclass
from automan.tool.modify_command import Modify_command
from automan.tool.parse_name_value import Parse_name_value
import automan.tool.error as error


class Execute_command(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.userclass = Userclass()
        self.currentlyini = {'debug' : 'off'}
        self.namevalue = {}
        '''
        Constructor
        '''
   
    def execute(self, command, systemini):
        result = 0
        ret = 0
        if self.currentlyini['debug'] == 'on':
            print systemini
            print self.currentlyini
        #need to be merge into userclass
        if len(command) >= 3 and str(command[2]) == 'ie':
            from automan.ui.ie import Ie
        if len(command) >= 4 and str(command[2]) != 'ie':
            self.userclass.check_class(command[2])
        try:
            if list(command).__len__() == 2:
                if command[1] == 'end':
                    try:
                        if self.ie:
                            self.ie.quit()
                    except:
                        pass
            elif list(command).__len__() == 3:
                if command[1] == 'ini':                   
                   self.currentlyini.update(Parse_file().get_ini(str(command[2])))
                elif command[1] == 'sleep':
                    time.sleep(int(command[2]))
                elif command[1] == 'debug' and command[2] == 'on':
                    self.currentlyini.update({'debug':'on'})
                elif command[1] == 'debug' and command[2] == 'off':
                    self.currentlyini.update({'debug':'off'})
            elif list(command).__len__() == 4:
                if command[1] == 'init' and command[2] == 'ie' and command[3].lower() == "chrome":
                   self.ie = Ie(systemini['chrome'],command[3].lower()).ie
                elif command[1] == 'init' and command[2] == 'ie' and command[3].lower() == "firefox":
                    self.ie = Ie(systemini['firefox'],command[3].lower()).ie
                elif command[1] == 'init' and command[2] == 'ie' and command[3].lower() == "ie":
                    self.ie = Ie(systemini['ie'],command[3].lower()).ie
                else:
                    ob = self.userclass.class_object[self.get_objectname(command)]
                    defname = self.get_defname(systemini,command)
                    ret = eval(defname)
            elif list(command).__len__() == 5:
                ob = self.userclass.class_object[self.get_objectname(command)]
                defname = self.get_defname(systemini,command)
                ret = eval(defname)
            elif list(command).__len__() == 6:
                pass
            if str(command[1]).find('$=get')>0:
                self.modify_currentlyini((command[1], ret))
        except error.nonamevalue:
            print "FAIL !! no name or key is in param_dict"
            result = 1
        except error.equalerror:
            print "FAIL !! value is not equal or exist"
            result = 1
        except error.notequalerror:
            print "FAIL !! value is equal or exist"
            result = 1
        except error.notfind:
            print "FAIL !! not find"
            result = 1    
        #except:
        #    result = 1
        return result
    
    def get_objectname(self,command):
        
        if str(command[2]).find('ie.')==0:
            return str(str(command[2]).split('.')[1]).lower()
        else:
            return str(command[2]).lower()
        
    def get_defname(self,systemini,command):
        
        if str(command[1]).find('=') > 0:
            action = str(str(command[1]).split('=')[1]).strip()
        else:
            action = command[1]
        
        if list(command).__len__() == 4:
            if str(command[2]).find('ie.')==0:
                return 'ob.' + command[3] + '_' + action + '(self.ie)'
            else:
                return 'ob.' + command[3] + '_' + action + '()'
        elif list(command).__len__() == 5:
            param = Modify_command().replay_ini(systemini, self.currentlyini,str(command[4]))
            self.namevalue = Parse_name_value().parse_name_value(param)
            if str(command[2]).find('ie.')==0:
                #return 'ob.' + command[3] + '_' + action + '(self.ie,\''+param+'\')'
                return 'ob.' + command[3] + '_' + action + '(self.ie,self.namevalue)'
            else:
                #return 'ob.' + command[3] + '_' + action + '(\''+param+'\')'
                return 'ob.' + command[3] + '_' + action + '('+'self.namevalue'+')'   
    def modify_currentlyini(self,(key,value)):
        self.currentlyini[str(key).split('$')[1]]=str(value)
