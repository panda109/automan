#coding:utf-8
'''
Created on 2010/12/10

@author: panda.huang
'''
import os   
import automan.tool.error as error

class Parse_file(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def parse_suite_log(self,log_list,testsuite,testcasename):
        #create suite folder 
        fhd= open('.\\log\\'+str(testsuite)+'\\'+str(testcasename)+'.log','w')
        for logs in log_list:
            print logs
            fhd.write(logs[0] +' '+ logs[1]+'\n')
            
        
    def parse_qa(self,filename):
        qa = []
        include = []
        i = 0
        for line in open(filename):
            #!= 'include'
            if len(line.strip()) > 1 and line[0] != '#' and str(line).strip().find('include') != 0:
                qa.append(['main '+str(i)]+[str(x).strip() for x in str(line).strip().split('\t') if x != ''])
            elif len(line.strip()) > 1 and line[0] != '#' and str(line).strip().find('include') == 0 :
                includename = line.strip().split('\t')[2]
                include = self.parse_include(self.get_include_file(includename))
                qa = qa + include
                include = []
            i = i + 1    
        return qa
    
    def parse_include(self,filename):
        include = []
        i = 0
        for line in open(filename):
            if len(line.strip()) > 1 and line[0] != '#' :
                include.append([filename+' '+str(i)]+[str(x).strip() for x in str(line).strip().split('\t') if x != ''])
            i = i + 1    
        return include
        pass
        
        
    def get_include_file(self,filename):
        include_list = []
        for dirname, dirnames, filenames in os.walk('.\qa'):     
            try:
                if open(dirname + '\\' + filename):
                    include_list.append(dirname + '\\' + filename)
                    break
            except:
                pass
        if len(include_list) == 0 :
            raise error.notfindincludefile()
        else:
            return include_list[0]
        
    
    def search_file(self,qa_filename):
        qa_list = []
        if str(qa_filename).find('.qas') > 0:
            for dirname, dirnames, filenames in os.walk('.\qa'):  
                try:
                    if open(dirname + '\\' + qa_filename):
                        qas_file = dirname + '\\' + qa_filename
                        break
                        #print self.get_qa_file((dirname + '\\' + qa_filename))
                        #self.qa_list.append(self.get_qa_file((dirname + '\\' + qa_filename)))
                except:
                    pass
            for qa_filename in open(qas_file):
                qa_list.append(self.get_qa_file(str(qa_filename).strip()))
                
        elif str(qa_filename).find('.qa') > 0:
            qa_list.append(self.get_qa_file(qa_filename))
        return qa_list
        
    def get_qa_file(self,filename):
        qa_list = []
        for dirname, dirnames, filenames in os.walk('.\qa'):     
            try:
                if open(dirname + '\\' + filename):
                    qa_list.append(dirname + '\\' + filename)
                    break
            except:
                pass
        if len(qa_list) == 0 :
            raise error.notfindqafile()
        else:
            return qa_list[0]

    def get_ini(self,filename):
        system={}
        try:
            lines = os.path.join(".//ini//", filename)
            for line in open(lines):
                temp = str(line).strip().split('=')[1]
                temp = self.modify(temp)
                system[str(line).strip().split('=')[0]] = temp
            return system
        except:
            print "can't find "+filename
            raise error.notfindinifile()
    
    def modify(self,tempstring):
        temp = tempstring.split('\\x')
        #print tempstring
        for index in range(len(temp)):
            if index > 0:
                ascii = temp[index][:2]
                tempstring = tempstring.replace("\\x" + ascii , chr(int(ascii,16)) , 1)
        #print len(tempstring),tempstring
        return tempstring
