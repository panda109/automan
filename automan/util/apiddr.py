# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:48:11 2020

@author: Dustin Lin
"""

import automan.tool.error as error
from warrant.aws_srp import AWSSRP
from botocore import UNSIGNED
import configparser
import subprocess
import websocket
import datetime
import requests
import botocore
import time
import json
import boto3
import os
#=======================
#connect DB
from sshtunnel import SSHTunnelForwarder
import psycopg2
#=======================



class apiDdr(object):
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(os.path.join(os.getcwd(), "conf", "apiDdrParam.conf"), encoding = "utf-8")
            self.index = "apiDdrParam"
            

        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()         
        
        pass

    
    def DBconnect_get(self):
        try:
            self.objSshTunnel = SSHTunnelForwarder(
                    ssh_address_or_host = (self.config.get("connectDBParam", "strSshKey"), int(self.config.get("connectDBParam", "strSshHostPort"))), #strSshKey:13.115.81.250 strSshHostPort:20022
                    ssh_pkey = os.path.join(os.getcwd(), self.config.get("connectDBParam", "strFolderName"), self.config.get("connectDBParam", "strFileName")), #foldername: conf, filename: qa.pem
                    ssh_username = self.config.get("connectDBParam", "strSshUserName"),
                    remote_bind_address = (self.config.get("connectDBParam", "strStagingDBPublic"), int(self.config.get("connectDBParam", "strDBHostPort")))
                )
            self.objSshTunnel.start()
            print("=====> Server Connected...")
            self.connectDB = psycopg2.connect(
                database = self.config.get("connectDBParam", "strDBName"),
                user = self.config.get("connectDBParam", "strDBAccount"),
                password = self.config.get("connectDBParam", "strDBPwd"),
                sslmode = self.config.get("connectDBParam", "strSslMode"),
                host = self.config.get("connectDBParam", "strHost"),
                port = self.objSshTunnel.local_bind_port
            )
            self.cursor = self.connectDB.cursor()
            print("=====> Database Connected...")

        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()
  
    def readConfigToDict_get(self):
        listConfigKey = []
        listConfigValue = []
        try:
            #print("=====>Config Section: {}".format(self.config.sections()))
            for item in self.config[self.index]:
                listConfigKey.append(item)
                listConfigValue.append(self.config[self.index][item])
            dicParam = {}
            for keyValue in range(len(listConfigKey)):
                dicParam[listConfigKey[keyValue]] = listConfigValue[keyValue]
            return dicParam
        except:
            print("=====> Error readConfigToDict")
        
    def idToken_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        strAWSRegion = dicParam["str_userpool_id"].split("_")[0]
        try:          
            client = boto3.client('cognito-idp', region_name=strAWSRegion, config = botocore.client.Config(signature_version = UNSIGNED))
            objAWS = AWSSRP(
                    pool_id = dicParam["str_userpool_id"],
                    client_id = dicParam["str_client_id"],
                    username = dicParam["str_username"],
                    password = dicParam["str_password"],       
                    client = client
                )
            dicToken = objAWS.authenticate_user()
            strIDToken = dicToken["AuthenticationResult"]["IdToken"]
            print("=====> Cognito Token: ")
            print(strIDToken)
            return strIDToken
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()
        
    def ndToken_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        try:
            strNdApiServer = dicParam["str_nd_api_server_head"] + "-qa" + dicParam["str_nd_api_server_tail"]            #head = https://api-eg3, tail = .nextdrive.io
            strExchangeUrl = strNdApiServer + dicParam["str_nd_api_server_exchange_path"]                            #/api/v1/oauth2/tokens/exchange
            dicHeader = {
                    dicParam["str_header_autho_key"]: dicParam["str_header_autho_value"],
                    dicParam["str_header_content_key"]: dicParam["str_header_content_value"]
                }
            dicBody = {
                    dicParam["str_aws_type_key"]: dicParam["str_aws_type_value"],
                    dicParam["str_token_key"]: dicParam["strIDToken"],
                    dicParam["str_app_uuid_key"]: dicParam["str_app_uuid_value"]
                }
            jsonBody = json.dumps(dicBody)
            objResponse = requests.post(strExchangeUrl, data = jsonBody, headers = dicHeader)
            print("=====>", objResponse)
            statusCode = objResponse.status_code    #need to confirm if status_code or statusCode
            if dicParam['returnCode'] == str(statusCode):
                dicResponse = objResponse.json()
                print("=====> ND Token:")
                print(dicResponse["accessToken"])    #dicResponse['accessToken'] = ND token
                return dicResponse["accessToken"]
            else:
                raise error.equalerror()     
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()
        
    def generatedashboardsData_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        strNdApiServerHead = dicParam["str_nd_api_server_head"] + "-qa" + dicParam["str_nd_api_server_tail"]            #head:https://api-eg3; tail: .nextdrive.io
        strNdApiServerTail = dicParam["str_nd_api_server_dashboard_head"] + dicParam["str_device_uuid"] + dicParam["str_nd_api_server_dashboard_path_tail"]            #strNdApiServerDashboardPathHead: /api/v1/devices/; strNdApiServerDashboardPathTail: /dashboard      
        strDashboardUrl = strNdApiServerHead + strNdApiServerTail
        strAuthoValue = "{} {}".format(dicParam["str_autho_head"], dicParam["strNDToken"])
        dicHeader = {
                dicParam["str_header_autho_key"]: dicParam["str_header_autho_value"],     #accept: application/json
                dicParam["str_autho_key"]: strAuthoValue,    #strAuthoKey = Authorization
                dicParam["str_content_type_key"]: dicParam["str_content_type_value"]
            }     
        if dicParam["strMissingParam"] == "none":
            pass
        else:
            del dicHeader[dicParam["strMissingParam"]]
            
        listApiData = [strDashboardUrl, dicHeader]
        return listApiData
        
    def dashboardsApi_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        listApiData = eval(dicParam["strApiData"])
        strDashboardUrl = listApiData[0]
        dicHeader = listApiData[1]

        try:
            if dicParam["method"] == "get":
                #correct
                objResponse = requests.get(strDashboardUrl, headers = dicHeader)
                print("=====>", objResponse)
                
            elif dicParam["method"] == "put":
                objResponse = requests.put(strDashboardUrl, headers = dicHeader)
                print("=====>", objResponse)
                
            elif dicParam["method"] == "post":
                objResponse = requests.post(strDashboardUrl, headers = dicHeader)
                print("=====>", objResponse)
                
            else:
                print("=====> Wrong method")
                raise error.equalerror()
            
            
            dicResponse = objResponse.json()
            print(dicResponse)
            statusCode = objResponse.status_code  
            return statusCode

              
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()   
        
        
    def generateControlsData_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        strNdApiServerHead = dicParam["str_nd_api_server_head"] + "-qa" + dicParam["str_nd_api_server_tail"]           
        strNdApiServerTail = dicParam["str_nd_api_server_control_head"] + dicParam["str_device_uuid"] + dicParam["str_nd_api_server_control_path_tail"]         
        strControlsUrl = strNdApiServerHead + strNdApiServerTail
        strAuthoValue = "{} {}".format(dicParam["str_autho_head"], dicParam["strNDToken"])
        dicHeader = {
                dicParam["str_header_autho_key"]: dicParam["str_header_autho_value"],    
                dicParam["str_autho_key"]: strAuthoValue,    
                dicParam["str_content_type_key"]: dicParam["str_content_type_value"]
            }
        
        if dicParam["deviceType"] == "battery":
            dicBody = {
                    dicParam["str_battery_opera_mode_key"]: dicParam["str_battery_opera_mode_value"]
                }
            pass
        elif dicParam["deviceType"] == "airCon":
            dicBody = {
                    dicParam["str_ac_opera_status_key"]: dicParam["str_ac_opera_status_value"]
                    #dicParam["str_ac_oprea_mode_key"]: dicParam["str_ac_oprea_mode_value"],
                    #dicParam["str_ac_power_saving_opera_key"]: dicParam["str_ac_power_saving_opera_value"],
                    #dicParam["str_ac_temp_setting_key"]: dicParam["str_ac_temp_setting_value"],
                    #dicParam["str_ac_air_flow_key"]: dicParam["str_ac_air_flow_value"]
                }
            pass
        elif dicParam["deviceType"] == "EVCharger":
            dicBody = {
                    dicParam["str_ev_opera_mode_key"]: dicParam["str_ev_opera_mode_value"]
                }
            pass
        elif dicParam["deviceType"] == "ecocute":
            dicBody = {
                    dicParam["str_eco_auto_mode_key"]: dicParam["str_eco_auto_mode_value"]
                }
            pass
        else:
            print("=====> Wrong device type")
            raise error.equalerror()
        
        if dicParam["strMissingHeaderParam"] == "none":
            pass
        else:
            del dicHeader[dicParam["strMissingHeaderParam"]]
            
        if dicParam["strMissingBodyParam"] == "none":
            pass
        else:
            del dicBody[dicParam["strMissingBodyParam"]]

        listApiData = [strControlsUrl, dicHeader, dicBody]
        
        print(listApiData)
        return listApiData
        
        
    def controlApi_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        listApiData = eval(dicParam["strApiData"])
        strControlsUrl = listApiData[0]
        dicHeader = listApiData[1]
        strBody = listApiData[2]
        jsonBody = json.dumps(strBody)
        
        print("============")
        print(jsonBody)
        try:
            if dicParam["method"] == "put":
                #correct
                objResponse = requests.put(strControlsUrl, data = jsonBody, headers = dicHeader)
                print("=====>", objResponse)
                pass
            elif dicParam["method"] == "get":
                objResponse = requests.get(strControlsUrl, data = jsonBody, headers = dicHeader)
                print("=====>", objResponse)
                pass
            elif dicParam["method"] == "post":
                objResponse = requests.post(strControlsUrl, data = jsonBody, headers = dicHeader)
                print("=====>", objResponse)
                pass
            else:
                print("=====> Wrong method")
                raise error.equalerror()

            statusCode = objResponse.status_code   
            dicResponse = objResponse.json()
            print(dicResponse)
            
            return statusCode


        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()   
            
    def queryData_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        try:
            strSelectItemSQL = dicParam["str_select_item_sql"]
            strTargetTable = dicParam["str_table_name"]
            strOrdering = dicParam["str_ordering_column"]
            strTime= (datetime.datetime.now() + datetime.timedelta(minutes = -1) + datetime.timedelta(hours = -8)).strftime("%Y-%m-%d %H:%M:%S")
            print(strTime)
            strSQLCmd = "SELECT {0} FROM {1} WHERE {2} >= '{3}' order by {2} desc".format(strSelectItemSQL, strTargetTable, strOrdering, strTime)
            self.cursor.execute(strSQLCmd)
            listResults = self.cursor.fetchall()
            for listNo in range(len(listResults)):
                print("Data {}: {}".format((listNo + 1), listResults[listNo]))
            return listResults
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()          
            
    def closeDBConnection_get(self):
        self.cursor.close()
        self.connectDB.close()
        self.objSshTunnel.stop()    
        
    def returnCode_verify(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        if dicParam["returnCode"] == dicParam["verifyCode"]:
            #verifyCode is the code return from cloud
            #returnCode is the code we expected
            pass
        else:
            raise error.equalerror()        
        
    
    
    def publishCode_verify(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        try: 
            strData = dicParam["dataFromDB"]
            print("=====>")
            print(strData)
            print(type(strData))
            
            listData = eval(strData)
    
            
    
            print(listData[0][2]["data"]["status_code"])
            print(listData[0][2]["data"]["extra"]["uuid"])
       
            
            strDataUuid = dicParam["str_device_uuid"]
            print("=========================")
            print(strDataUuid)
            strTargetDataUuid = listData[0][2]["data"]["extra"]["uuid"]
            strTargetStatusCode = str(listData[0][2]["data"]["status_code"])
            if strTargetDataUuid == strDataUuid:
                if strTargetStatusCode == dicParam["returnCode"]:
                    pass
                else:
                    print("=====> Wrong code")
                    raise error.equalerror()
            else:
                print("=====> Wrong uuid")
                raise error.equalerror()
        except Exception as exceptionError:
            #raise error.equalerror()
            print("Exception---->")
            print(exceptionError)
            #raise error.equalerror()
            if dicParam['except'] == 'ignore':
                #����test case�]�iexcept�O���`�����]�i�Jexcept���G�|��fail�A��#except#=ignore�ɪ������Lexcept�A�j�������G��pass
                pass
            else:
                raise error.equalerror() 
        
        #=====================================
        #note
        """
        step 0. insert data from db
        step 1. check config.file, get device uuid
        step 2. check type "publish" or "requset"
        step 3. publish --> check session_id
        step 4. uses session_id to find the request(session_id must be same)
        step 4. check agent "echonet_lite", "ble", "smart_meter"
        step 5. if type == publish --> check result_status
                if type == request --> chect status
        """
        #=====================================
    '''    
    def DataPreProcess_get(self, valueDict):
        listResponse = []
        listPublish = []
        listTargetResult = []
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(valueDict)
        dicParam = {**dicParam_conf, **dicParam_ini} 
        strAgent = dicParam["strAgent"]
        strDeviceUuid = dicParam["str_device_uuid"]
        print("=====> Target Device Uuid: {}".format(strDeviceUuid))
        try:
            listResult = list(dicParam["listResult"])
            for dataNo in range(len(listResult)):
                if listResult[dataNo]["type"] == "publish":
                    listPublish.append(listResult[dataNo])
                elif listResult[dataNo]["type"] == "response":
                    listResponse.append(listResult[dataNo])
                else:
                    pass
            
            for dataNo in range(len(listPublish)):
                if listPublish[dataNo]["data"][strAgent]["devices"][0]["device_uuid"] == strDeviceUuid:
                    strTargetSessionID = listPublish[dataNo]["session_id"]
                    dicTargetPublishData = listPublish[dataNo]
                    break
                else:
                    pass
                
            for dataNo in range(len(listResponse)):
                if listResponse[dataNo]["session_id"] == strTargetSessionID:
                    dicTargetResponseData = listResponse[dataNo]
                    break
                else:
                    pass
            listTargetResult = [dicTargetResponseData, dicTargetPublishData]
            return listTargetResult
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror() 
        
    def DDRResponse_verify(self, valueDict):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(valueDict)
        dicParam = {**dicParam_conf, **dicParam_ini} 
        strAgent = dicParam["strAgent"]
        try:    
            listTargetResult = list(dicParam["strTargetResult"])
            if listTargetResult[0]["status"] != dicParam["ResponseReturnCode"]: #200
                raise error.equalerror()
            else:
                pass
            
            if listTargetResult[1]["data"][strAgent]["devices"][0]["operation"][0]["result_status"] != dicParam["PublishReturnCode"]: #200
                raise error.equalerror()
            else:
                pass
     
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror() 
        
    ''' 
        
       
    def dashboardPost_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        try:
            strNdApiServerHead = dicParam["str_nd_api_server_head"] + "-qa" + dicParam["str_nd_api_server_tail"]          
            strNdApiServerTail = dicParam["str_nd_api_server_dashboard_head"] + dicParam["str_device_uuid"] + dicParam["str_nd_api_server_dashboard_path_tail"]            #strNdApiServerDashboardPathHead: /api/v1/devices/; strNdApiServerDashboardPathTail: /dashboard      
            strDashboardGetUrl = strNdApiServerHead + strNdApiServerTail
            strAuthoValue = "{} {}".format(dicParam["str_autho_head"], dicParam["strNDToken"])
            dicHeader = {
                    dicParam["str_header_autho_key"]: dicParam["str_header_autho_value"],     
                    dicParam["str_autho_key"]: strAuthoValue,
                    dicParam["str_content_type_key"]: dicParam["str_content_type_value"]
                }
            objResponse = requests.post(strDashboardGetUrl, headers = dicHeader)
            print("=====>", objResponse)
            statusCode = objResponse.status_code    
            if dicParam['returnCode'] == str(statusCode):
                pass
            else:
                raise error.equalerror()
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()  
        
    def dashboardPut_get(self, dicValue):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(dicValue)
        dicParam = {**dicParam_conf, **dicParam_ini}
        try:
            strNdApiServerHead = dicParam["str_nd_api_server_head"] + "-qa" + dicParam["str_nd_api_server_tail"]          
            strNdApiServerTail = dicParam["str_nd_api_server_dashboard_head"] + dicParam["str_device_uuid"] + dicParam["str_nd_api_server_dashboard_path_tail"]            #strNdApiServerDashboardPathHead: /api/v1/devices/; strNdApiServerDashboardPathTail: /dashboard      
            strDashboardGetUrl = strNdApiServerHead + strNdApiServerTail
            strAuthoValue = "{} {}".format(dicParam["str_autho_head"], dicParam["strNDToken"])
            dicHeader = {
                    dicParam["str_header_autho_key"]: dicParam["str_header_autho_value"],     
                    dicParam["str_autho_key"]: strAuthoValue,
                    dicParam["str_content_type_key"]: dicParam["str_content_type_value"]
                }
            objResponse = requests.put(strDashboardGetUrl, headers = dicHeader)
            print("=====>", objResponse)
            statusCode = objResponse.status_code    
            if dicParam['returnCode'] == str(statusCode):
                pass
            else:
                raise error.equalerror()
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""
    def websocketClient_get(self, valueDict):
        dicParam_conf = self.readConfigToDict_get()
        dicParam_ini = dict(valueDict)
        dicParam = {**dicParam_conf, **dicParam_ini}
        strTargetUrl = self.config.get("websocketParam","strTargetUrl")
        dicHeader = {
                self.config.get("websocketParam", "strTypeKey"): self.config.get("websocketParam", "strTypeValue"),
                self.config.get("websocketParam", "strAuthoKey"): dicParam["strNDToken"],
                self.config.get("websocketParam", "strUuidKey"): dicParam["str_app_uuid_value"]
            }

        def receiveData(ws, data):
            print("=====> DATA")
            print(data)
            self.insertData(data)
            print("=====")
        
        def raiseError(ws, error):
            print("=====> ERROR")
            print(error)
            print("=====")
        
        def closeConnect(ws):
            print("=====> CLOSE")
        
        def contentInfo(ws):
            print("=====> OPEN")
            #jsonData = json.dumps(dicData)
            #ws.send(jsonData)
            #print("=====>,", dicData)
            print("=====")
        #===================
        websocket.enableTrace(True)
        
        ws = websocket.WebSocketApp(
                strTargetUrl,
                on_message = receiveData,
                on_error = raiseError,
                on_close = closeConnect,
                header = dicHeader
            )
        ws.on_open = contentInfo
        strTimeStart = time.time()
        ws.run_forever()
        #need to adds close time if combine to apiDdr.py
        strTimeEnd = time.time()
        print("=====> Run Time: {}".format(strTimeEnd - strTimeStart))
    
    def insertData(self, strTargetData):
        try:
            dicTargetData = eval(strTargetData)
            dicInsertData = dicTargetData["data"]
            print(type(dicInsertData))
            jsonInsertData = json.dumps(dicInsertData)
            self.cursor.execute("INSERT INTO testing (product_id, created_on, received_data) VALUES (%s, %s, %s);", ("J2C49CC4B738B410C", "2020-11-14 14:00:23", jsonInsertData))
            self.connectDb.commit()
            print("=====> Insert successful")
            pass
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()        
 """       

    



