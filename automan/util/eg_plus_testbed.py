#coding=utf-8
"""
Created on 2021/02/03
@author     : Roger Wei
Project     : Ecogenie+ APP
"""
import automan.tool.error as error
import os.path, re, time
import xml.etree.ElementTree as ET

class eg_plus_testbed(object):
    
    def _init_(self):
        pass
            
    def xml_list_get(self, valueDict):
        ### Get XML content and return then as a list.
        ###
        ### Required parameters:
        ###     path        - XML file path.
        ###         Format: {folder}\{file}.xml
        ###
        try:
            valueDict['path'] in locals().keys()
        except:
            raise error.nonamevalue()
        try:
            filePath = os.getcwd() + "\\" + valueDict['path']
            tree = ET.parse(filePath)
            for element in tree.findall(".//testcase"):
                xmlName = element.get('name')
                xmlResult = element.get('result')
                xmlTime = element.get('time')
            print([xmlName, xmlResult, xmlTime])
            return [xmlName, xmlResult, xmlTime]
        except:
            print("Can NOT parse XML: " + filePath)
            return ""
        
    def overall_result_get(self, valueDict):
        ### Merge all result and make them human readable.
        ###
        ### Required parameters:
        ###     text        - Results divide with ";".
        ###         Format: {Result 1};{Result 2};...
        ###         Format(Each result): ['eg_plus_android_ECN_Air_Conditioner', 'pass', '719.0 sec']
        ###
        try:
            valueDict['text'] in locals().keys()
        except:
            raise error.nonamevalue()
        try:
            returnText = ""
            resultList = (valueDict['text']).split(";")
            marksList = [": ", "(", ")"]
            totalTime = 0
            finalResult = True
            for result in resultList:
                if len(result) == 0:
                    continue
            
                ## Get execution time
                eachTime = re.search("'([0-9.]+) sec'", result)
                if eachTime:
                    totalTime = totalTime + float(eachTime.group(1))
                else:
                    continue
                
                ## Get boolean result
                eachResult = re.search("'(pass|fail)'", result)
                if eachResult:
                    finalResult = (finalResult & True) if eachResult.group(1) == "pass" else False
                else:
                    continue
                
                ## Get each value
                result = re.findall("'([^']+)'", result)
                for i in range(len(result)):
                    returnText = returnText + result[i] + marksList[i]
                returnText = returnText + "\n"
    
            returnText = "--------------------------------------------------\n" + returnText
            totalTime = time.strftime('%H:%M:%S', time.gmtime(int(totalTime)))
            returnText = "Execution time: " + str(totalTime) + "\n" + returnText
            finalResult = "PASS" if finalResult else "FAIL"
            returnText = "Final result: " + finalResult + "\n" + returnText
            returnText = "Ecogenie+ Quick-Scan test finished.\n" + returnText
            print(returnText)
            return returnText
        except:
            raise error.notfind()