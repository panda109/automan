# -*- coding: utf-8 -*-
'''
Created on 2020/06/16

@author: Shawn Lin
'''
import automan.tool.error as error
import requests,base64,json
from symbol import except_clause
import os



class apicalls(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass

    
    def pid_format_check(self, pid):
        
        if len(pid) == 16:
            for num in range(0, 6):
                if pid[num] < chr(48) and pid[num] > chr(57) or pid[num] < chr(65) and pid[num] > chr(74):
                    raise error.equalerror()
                else:
                    pass                 
        elif len(pid) == 17:
            for num in range(5, 17):
                if pid[num] < chr(48) and pid[num] > chr(57) or pid[num] < chr(65) and pid[num] > chr(74):
                    raise error.equalerror()
                else:
                    pass
        else:
            raise error.equalerror()
        return print('pid check PASS!')
        
    
    def accesstoken_get(self, value_dict):
        
        bolResult = True
        dicParm = dict(value_dict)
        #print("API dicParm",dicParm)
        
        try:
            strAutho = '%s:%s' % (dicParm['strID'],dicParm['strSecret'])
            byteAutho = strAutho.encode('utf-8')
            base64Autho = base64.b64encode(byteAutho)
            strFinalAutho = '%s %s' % (dicParm['strPrefixOfAutho'],base64Autho.decode('utf-8'))
            
            dicHeader = {dicParm['strHeaderAutho']:strFinalAutho, dicParm['strHeaderContentType']:dicParm['strHeaderConTypeValue']}
            dicBody = {dicParm['strBodyGrantType']:dicParm['strBodyGrantTypeValue'], dicParm['strBodyScope']:dicParm['strScopeRange']}
            objResponse = requests.post(dicParm['strURL'], data=dicBody, headers=dicHeader)
            
            
            dicResponse = objResponse.json()
            
            print("return code: ->")
            print(objResponse.status_code)
            print(objResponse.text)
            #print(objResponse.status_code)
            
            if dicParm['returnCode'] == str(200):
                if objResponse.status_code != 200:
                    raise error.equalerror()
                elif dicResponse["expires_in"] != 3600:
                    raise error.equalerror()
                elif dicResponse["token_type"] != "Bearer":
                    raise error.equalerror()
                else:
                    return dicResponse["access_token"]
                pass
            elif dicParm['returnCode'] == str(400) and objResponse.status_code == 400:
                pass
            else:
                print("else return:", objResponse.status_code)
            
        except Exception as exceptionError:
            #raise error.notfind()
            print("$$$$$Exception error$$$$$")
            print(exceptionError)
            raise error.equalerror()
        

    def gwstate_get(self, value_dict):
        bolResult = True
        dicParm = dict(value_dict)
        #apicalls.pid_format_check(self, dicParm['strProductID'])
        try:
            strGWM_URL = dicParm['strNDAPIServer'] + dicParm['strNDAPIServerPath'] % dicParm['strProductID']
            strGWM_Autho = '%s %s' % (dicParm['strAuthoType'],dicParm['AToken'])
            
            dicGWM_Header = {dicParm['strHeaderAutho']:strGWM_Autho}
            dicGWM_Params={dicParm['strParame_ProID']:dicParm['strProductID']}
            objGWMResponse = requests.get(strGWM_URL, params=dicGWM_Params, headers=dicGWM_Header)
            dicGWMResponse = objGWMResponse.json()
            print(objGWMResponse)
            print("return code: ->")
            print(objGWMResponse.text)
            print(objGWMResponse.status_code)
            print("return code: ->",objGWMResponse.status_code)
            #print("dicGWMResponse",dicGWMResponse)
            
            if dicParm['returnCode'] == str(200) and objGWMResponse.status_code == 200:
                if dicGWMResponse["message"] != "success":
                    raise error.equalerror()
                elif dicGWMResponse["data"]["state"] != dicParm['strGWState']:
                    raise error.equalerror()
            elif dicParm['returnCode'] == str(400) and objGWMResponse.status_code == 400:
                print('#400 Bad Request: Problem with the request')
                pass
            elif dicParm['returnCode'] == str(401) and objGWMResponse.status_code == 401:
                print('#401 Unauthorized: Valid access token is not specified')
                pass
            elif dicParm['returnCode'] == str(403) and objGWMResponse.status_code == 403:
                print('#403 Forbidden: Not authorized to access the resource')
                pass
            elif dicParm['returnCode'] == str(404) and objGWMResponse.status_code == 404:
                print('#404 Not Found: Requesting resource not found')

            else:
                print("else return:", objGWMResponse.status_code)
            
        except Exception as exceptionError:
            
            print("$$$$$Exception error$$$$$")
            print(exceptionError)
            raise error.equalerror()
    
               
        
    def devicelist_get(self, value_dict):
        dicParm = dict(value_dict)
        #apicalls.pid_format_check(self, dicParm['strProductID'])
        
        try:
            strGWM_URL = dicParm['strNDAPIServer'] + dicParm['strNDAPIServerPath'] % dicParm['strProductID']
            strGWM_Autho = '%s %s' % (dicParm['strAuthoType'],dicParm['AToken'])            
            dicGWM_Header = {dicParm['strHeaderAutho']:strGWM_Autho, dicParm['strContentType']: dicParm['strContentDescription']}
            dicGWM_Params={dicParm['strParame_ProID']:dicParm['strProductID']}
            objGWMResponse = requests.get(strGWM_URL, params=dicGWM_Params, headers=dicGWM_Header)
            
            dicGWMResponse = objGWMResponse.json()    
            
            print("return code: ->")
            print(objGWMResponse.text)
            print("return code: ->",objGWMResponse.status_code)
            

            if dicParm['returnCode'] == str(200):
                if objGWMResponse.status_code != 200:
                    raise error.equalerror()
                else:
                    for i in range(len(dicGWMResponse["data"]["rows"])):               
                        if dicGWMResponse["data"]["rows"][i]["accessory_uuid"] != dicParm["strAccessory_uuid"]:
                            raise error.equalerror()
                        elif dicGWMResponse["data"]["rows"][i]["model"] != dicParm["strModel"]:
                            raise error.equalerror()
                        elif str(dicGWMResponse["data"]["rows"][i]["connected"]) != dicParm["strConnected"]:
                            raise error.equalerror()                 
                pass
            elif dicParm['returnCode'] == str(400) and objGWMResponse.status_code == 400:
                print('#400 Bad Request: Problem with the request')
                pass
            elif dicParm['returnCode'] == str(401) and objGWMResponse.status_code == 401:
                print('#401 Unauthorized: Valid access token is not specified')
                pass
            elif dicParm['returnCode'] == str(403) and objGWMResponse.status_code == 403:
                print('#403 Forbidden: Not authorized to access the resource')
                pass
            elif dicParm['returnCode'] == str(404) and objGWMResponse.status_code == 404:
                print('#404 Not found: Requesting resource not found')
            else:
                print("else return:", objGWMResponse.status_code)
            
        except Exception as exceptionError:
            print("$$$$$Exception error$$$$$")
            print(exceptionError)
            raise error.equalerror()
        
        
        
        
    def golden_sample_load(self, value_dict):
        dicParm = dict(value_dict)
        SaveDirectory = os.getcwd()
        fullpath = os.path.join(SaveDirectory,'ini', 'API', 'golden_sample.json')
        
        with open(fullpath) as fileGS:
            golden_sample = json.load(fileGS)
        #print(golden_sample)     
       
        if dicParm['type'] == 'gwstate':    
            tempfilename = dicParm['type'] + '_golden_sample.ini'
            tempfilepath = os.path.join(SaveDirectory, 'ini', 'API', tempfilename)
            tempfile = open(tempfilepath, 'w')
            if 'exclude' in dicParm:
                if dicParm['exclude'] == 'strGWState':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                elif dicParm['exclude'] == 'strProductID':                    
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strGWState=' + golden_sample['gwstate']['state'] + '\n')
                elif dicParm['exclude'] == 'gate_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strGWState=' + golden_sample['gwstate']['state'] + '\n')
                elif dicParm['exclude'] == 'device_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('strGWState=' + golden_sample['gwstate']['state'] + '\n')
                else:
                    raise error.equalerror()
                    #tempfile.write('strGWState=' + golden_sample['gwstate']['state'] + '\n')    
            else:
                tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                tempfile.write('strGWState=' + golden_sample['gwstate']['state'] + '\n')
                          
        elif dicParm['type'] == 'device_list':          
            tempfilename = dicParm['type'] + '_golden_sample.ini'
            tempfilepath = os.path.join(SaveDirectory, 'ini', 'API', tempfilename)
            tempfile = open(tempfilepath, 'w')
            if 'exclude' in dicParm:
                if dicParm['exclude'] == 'strAccessory_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                    tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')
                elif dicParm['exclude'] == 'strModel':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                    tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')                
                elif dicParm['exclude'] == 'strConnected':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                    tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                elif dicParm['exclude'] == 'strProductID':
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                    tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                    tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')
                elif dicParm['exclude'] == 'gateway_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                    tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                    tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')
                elif dicParm['exclude'] == 'device_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                    tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                    tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')
                else:  
                    raise error.equalerror()   
            else:
                tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                tempfile.write('strAccessory_uuid=' + golden_sample['device_list']['accessory_uuid'] + '\n')
                tempfile.write('strModel=' + golden_sample['device_list']['model'] + '\n')
                tempfile.write('strConnected=' + str(golden_sample['device_list']['connected']) + '\n')
      
        elif dicParm['type'] == 'data_retrieval':     
            tempfilename = dicParm['type'] + '_golden_sample.ini'
            tempfilepath = os.path.join(SaveDirectory, 'ini', 'API', tempfilename)
            tempfile = open(tempfilepath, 'w')
            
            if 'exclude' in dicParm:
                if dicParm['exclude'] == 'pid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'accessory_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'scope':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'begin':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'end':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                elif dicParm['exclude'] == 'strProductID':
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'gateway_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                elif dicParm['exclude'] == 'device_uuid':
                    tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                    tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                    tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                    tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                    tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                    tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                    tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')
                else: 
                    raise error.equalerror()
            else:
                tempfile.write('strProductID=' + golden_sample['common']['pid'] + '\n')
                tempfile.write('gateway_uuid=' + golden_sample['common']['gateway_uuid'] + '\n')
                tempfile.write('device_uuid=' + golden_sample['common']['device_uuid'] + '\n')
                tempfile.write('pid=' + golden_sample['data_retrieval']['query'][0]['pid'] + '\n')
                tempfile.write('accessory_uuid=' + golden_sample['data_retrieval']['query'][0]['accessory_uuid'] + '\n')
                tempfile.write('scope=' + golden_sample['data_retrieval']['query'][0]['scope'][0] + '\n')
                tempfile.write('begin=' + str(golden_sample['data_retrieval']['time']['begin']) + '\n')
                tempfile.write('end=' + str(golden_sample['data_retrieval']['time']['end']) + '\n')

        else:
            raise error.equalerror()
        
        tempfile.close()

        