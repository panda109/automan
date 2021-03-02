#coding=utf-8
"""
Created on 2021/02/03
@author     : Roger Wei
Project     : Ecogenie+ APP
"""
import automan.tool.error as error
import os.path, re, time, json, subprocess, configparser
import xml.etree.ElementTree as ET

class eg_plus_testbed(object):
    
    def _init_(self):
        pass
            
    def qa_list_get(self, valueDict):
        try:
            hFile = open(os.getcwd() + "\\" + valueDict['path'], 'r')
            fileContent = hFile.read() 
            hFile.close()
            
            match = re.findall("([^\r\n]+).qa\n{0,1}", fileContent)
            try:
                match.remove("eg_plus_upload_result")
            except:
                pass
            return match
        except:
            raise error.nonamevalue()
            
    def xml_list_get(self, valueDict):
        ### Get XML content and return then as a list.
        ###
        ### Required parameters:
        ###     list        - QA file list.
        ###     path_prefix - Log file path prefix.
        ###
        try:
            valueDict['list'] in locals().keys()
            valueDict['path_prefix'] in locals().keys()
            qaList = valueDict['list']
            qaList = eval(qaList)
            qaList = json.dumps(qaList)
            qaList = json.loads(qaList)
        except:
            raise error.nonamevalue()

        try:
            resultList = ""
            for item in qaList:
                #print(item)
                filePath = os.getcwd() + "\\log\\" + valueDict['path_prefix'] + item + "\\" + item + ".xml"
                #print(filePath)
                try:
                    hFile = open(filePath, 'r')
                    fileContent = hFile.read() 
                    hFile.close()
                    #print(fileContent)
                    xmlName = re.search("\sname=\"([^\r\n\s=]+)\"\s", fileContent)
                    xmlResult = re.search("\sresult=\"(pass|fail)\"\s", fileContent)
                    xmlTime = re.search("\stime=\"([^\r\n\"]+)\"/", fileContent)
                    resultList = resultList + "['" + xmlName.group(1) + "', '" + xmlResult.group(1) + "', '" + xmlTime.group(1) + "'];"
                except:
                    print(filePath + " not found.")
                    continue
            resultList = resultList[0:len(resultList) - 1]
            print(resultList)
            return resultList
        except:
            raise error.notfind()

    def CMD_response_get(self, valueDict):
        ### Get CMD response with multiply lines.
        ###
        ### Required parameters:
        ###     command        - CMD command.
        ###
        try:
            response = ""
            out = subprocess.Popen(valueDict['command'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in out.stdout:
                line = line.rstrip()
                response += line.decode("big5", "ignore")
            print(response)
            return response
        except:
            raise error.nonamevalue()
        
    def INI_value_get(self, valueDict):
        ### Get value from INI file.
        ###
        ### Required parameters:
        ###     ini         - INI file path and name.
        ###     scope       - Scope of value.
        ###
        #try:
        print(os.getcwd() + "\\" + valueDict['ini'])
        hFile = open(os.getcwd() + "\\" + valueDict['ini'], 'r')
        file_content = hFile.read()
        hFile.close()
        value = re.search(valueDict['scope'] + "=([^\r\n]+)", file_content)
        value = "" if not value else value.group(1)
        print(value)
        return value
        #except:
        #    raise error.nonamevalue()
        
    def app_version_get(self, valueDict):
        ### Get APP version.
        ###
        ### Required parameters:
        ###     command        - CMD command.
        ###
        try:
            response = ""
            out = subprocess.Popen(valueDict['command'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in out.stdout:
                line = line.rstrip()
                response += line.decode("big5", "ignore")
                
            print("Source data: " + response)
            response = re.search("versionName=([^\r\n]+)", response)
            response = "" if not response else response.group(1)
            print("Regexp data: " + response)
            return response
        except:
            raise error.nonamevalue()

    def overall_result_get(self, valueDict):
        ### Merge all result and make them human readable.
        ###
        ### Required parameters:
        ###     text        - Results divide with ";".
        ###         Format: {Result 1};{Result 2};...
        ###         Format(Each result): ['eg_plus_android_ECN_Air_Conditioner', 'pass', '719.0 sec']
        ###     fw_version  - Firmware version.
        ###     app_version - APP version.
        ###
        try:
            valueDict['text'] in locals().keys()
            valueDict['fw_version'] in locals().keys()
            valueDict['app_version'] in locals().keys()
            valueDict['testing_environment'] in locals().keys()
            fwVersion = re.search("\[ro.build.version.release\]: \[([^\r\n]+)\]", valueDict['fw_version'])
            fwVersion = valueDict['fw_version'] if not fwVersion else fwVersion.group(1)
            appVersion = valueDict['app_version']
            testingEnvironment = "QA Staging" if valueDict['testing_environment'] == "qa" else "Not defined"
            testingEnvironment = "Production" if valueDict['testing_environment'] == "production" else testingEnvironment
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
                eachTime = re.search("'([0-9.]+)( sec){0,1}'", result)
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
                    eachTime = re.search("([0-9]+).0( sec){0,1}", result[i])
                    eachResult = re.search("(pass|fail)", result[i])
                    if eachTime:
                        returnText = returnText + time.strftime('%H:%M:%S', time.gmtime(int(eachTime.group(1)))) + marksList[i]
                    elif eachResult:
                        returnText = returnText + (result[i]).upper() + marksList[i]
                    else:
                        returnText = returnText + result[i] + marksList[i]
                returnText = returnText + "\n"
        
            returnText = "--------------------------------------------------\n" + returnText
            totalTime = time.strftime('%H:%M:%S', time.gmtime(int(totalTime)))
            returnText = "Execution time: " + str(totalTime) + "\n" + returnText
            finalResult = "PASS" if finalResult else "FAIL"
            returnText = "Final result: " + finalResult + "\n" + returnText
            returnText = "--------------------------------------------------\n" + returnText
            returnText = "Application version: " + appVersion + "\n" + returnText
            returnText = "Firmware version: " + fwVersion + "\n" + returnText
            returnText = "--------------------------------------------------\n" + returnText
            returnText = "Testing environment: " + testingEnvironment + "\n" + returnText
            returnText = "Ecogenie+ Quick-Scan test finished.\n" + returnText
            print(returnText)
            return returnText
        except:
            raise error.notfind()
