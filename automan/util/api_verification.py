#coding=utf-8
"""
Created on 2021/04/15
@author     : Dustin Lin
Project     : Postman Automan Integration
"""
import automan.tool.error as error  
from automan.tool.verify import Verify
import configparser
import subprocess
import botocore
from botocore import UNSIGNED
from warrant.aws_srp import AWSSRP
import boto3
import json
import csv
import sys
import os
import re

class api_verification(object):
    def __init__(self):  
        self.total = 0
        pass

    def read_csv_get(self, dic_value): 
        ## Read csv file and find the target response
        ##
        ## Parameters:
        ##    - csv_filename
        ##    - testcase_name
        ##
        dic_param = dict(dic_value)
        
        maxInt = sys.maxsize
         
        while True:
            # decrease the maxInt value by factor 10 
            # as long as the OverflowError occurs.
            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                maxInt = int(maxInt/10)

        try:
            #define csv file:
            str_file_path = os.path.join(os.getcwd(), "ini", "API_NextDrive", "newman", dic_param["csv_filename"])
            list_data = []
            str_target_data = ""
            #open csv file and write into a list:
            with open(str_file_path, newline = "", encoding = "utf-8") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    list_data.append(row)
            #delete first line of the csv:
            del list_data[0]
            
            #choose which response data you want:
            for data_no in range(len(list_data)):
                if dic_param["testcase_name"] in list_data[data_no]:
                    str_target_data = list_data[data_no]
                    print(str_target_data)
                else:
                    pass
            #return response
            return str_target_data
            
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()         
        pass
    
    
    def status_code_get(self, dic_value):
        ## Get status code of API response
        ## Parameters:
        ##     - api_response
        ##
        dic_param = dict(dic_value)
        str_response = dic_param["api_response"]
        print(str_response)
        #print(type(str_response))
        list_response = eval(str_response)
        print(list_response)
        for i in range(len(list_response)):
            if "http" in list_response[i]:
                #print(list_response[i + 2])
                str_status_code = list_response[i + 2]
                break
            else:
                pass
        return str_status_code
            
    def response_body_get(self, dic_value):
        ## Get response body of API response
        ## Parameters:
        ##     - api_response
        ##
        dic_param = dict(dic_value)
        str_response = dic_param["api_response"]
        list_response = eval(str_response)
        #find response body:
        for i in range(len(list_response)):
            if "http" in list_response[i]:
                #To check if has response body:
                if i + 5 >= len(list_response):
                    str_response_body = "No body"
                    print("No body")
                    break
                else:
                    pass
                    #To find the response body:
                    print(list_response[i+5])
                    str_response_body = list_response[i+5]
                    str_response_body = str_response_body.replace("Response Body", "")
                    print(str_response_body)
                return str_response_body
            else:
                pass
    
    def status_code_verify(self, dic_value):
        ## Verify status code from api response
        ## Parameters:
        ##     - api_response
        ##
        dic_param = dict(dic_value)
        #Loading response and transfer to json format:
        str_response = dic_param["api_response"]
        #print(str_response)
        if str_response == dic_param["expected_status_code"]:
            print("Status code: EQUAL")
            pass
        else:
            raise error.equalerror()
        #json_response = json.loads(str_response)
        
    def path_get(self):
        ## Get executed location
        str_path = os.getcwd()
        return str_path
        
    def cmd_path_set(self, dic_value):
        ## Set location
        ## Parameters:
        ##    - environment_path
        ##
        dic_param = dict(dic_value)
        os.chdir(dic_param["environment_path"])
        
    def cmd_exec(self, dic_value):
        ## Executes command
        ## Parameters:
        ##     - command
        ##
        dic_param = dict(dic_value)
        os.chdir(os.path.join(os.getcwd(),dic_param["run_environment_path"]))
        os.system(dic_param["command"])
        os.chdir(dic_param["original_path"])
        
    def file_list_get(self, dic_value):
        ## Get file list in folder which stored response csv file
        ## Parameters:
        ##     - folder_path
        ##
        dic_param = dict(dic_value)
        print(os.getcwd())
        str_path = os.path.join(os.getcwd(), "ini", "API_NextDrive", dic_param["folder_path"])
        print(str_path)
        list_file_name = os.listdir(str_path)
        str_target_file_name = list_file_name[-1]
        print(list_file_name)
        print(str_target_file_name)
        return str_target_file_name
    
    
    def expected_result_get(self, dic_value):
        ## Get expected result
        ## Parameters:
        ##     - expected_result
        ##
        dic_param = dict(dic_value)
        str_file_path = os.path.join(os.getcwd(), "ini", "API_NextDrive", dic_param["expected_result"])

        
        obj_expected_result = open(str_file_path, "r", encoding = 'utf-8')
        str_expected_result = obj_expected_result.read()
        #print(str_expected_result)
        obj_expected_result.close()
        
        
        return str_expected_result
        
    def dict_keys_verify(self, dic_value):
        ## Verify dictionary keys
        ## Parameters:
        ##     - expected_result
        ##     - actual_result
        ##
        try:
            dic_param = dict(dic_value)
            dic_expected_result = json.loads(dic_param["expected_result"])
            dic_actual_result = json.loads(dic_param["actual_result"])
            list_expected_keys = list(dic_expected_result.keys())
            list_actual_keys = list(dic_actual_result.keys())
            print("***********************************************")
            print("***********************************************")
            print("Expected result")
            print(dic_expected_result)
            print("Actual result")
            print(dic_actual_result)
            print("***********************************************")
            print("***********************************************")
            print("***********************************************")
            print("Expected keys")
            print(list_expected_keys)
            print("Actual keys")
            print(list_actual_keys)
            print("***********************************************")
            print("***********************************************")
            for i in range(len(list_expected_keys)):
                if list_expected_keys[i] in list_actual_keys:
                    print("Key \"{}\"".format(list_expected_keys[i]).ljust(25) + "exists")
                else:
                    print("missing key: ", list_expected_keys[i])
                    raise error.equalerror()
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()         
        pass

    def dict_content_verify(self, dic_value):
        ## Verify dictionary values
        ## Parameters:
        ##     - expected_result
        ##     - actual_result
        try:
            dic_param = dict(dic_value)
            dic_expected_result = json.loads(dic_param["expected_result"])
            dic_actual_result = json.loads(dic_param["actual_result"])
            list_expected_keys = list(dic_expected_result.keys())
            list_actual_keys = list(dic_actual_result.keys())
            print("***********************************************")
            print("***********************************************")
            for i in range(len(list_expected_keys)):
                print("EXPECTED RESULT")
                print(dic_expected_result[list_expected_keys[i]])
                print("=====")
                print("ACTUAL RESULT")
                print(dic_actual_result[list_expected_keys[i]])
                print("=====")
                if dic_expected_result[list_expected_keys[i]] == dic_actual_result[list_expected_keys[i]]:
                    print("Expected result: {}".format(dic_expected_result[list_expected_keys[i]]).ljust(50) + "||" + "Actual result: {}".format(dic_actual_result[list_expected_keys[i]]).rjust(50))
                else:
                    raise error.equalerror()
            print("***********************************************")
            print("***********************************************")
        except Exception as exceptError:
            print("=====> Exception")
            print(exceptError)
            raise error.equalerror()         
        pass        

    def environment_token_set(self, dic_value):
        ## To change cognito token in environment.json file
        ##
        dic_param = dict(dic_value)
        file_name = dic_param["environment_name"]
        file_path = os.path.join(os.getcwd(), "ini", "API_NextDrive", file_name)
        print(file_path)
        f = open(file_path, "r+")
        file = f.read()
        f.close()
        dic_file = json.loads(file)
        for i in range(len(dic_file["values"])):
            if dic_file["values"][i]["key"] == "cognito_token":
                dic_file["values"][i]["value"] = dic_param["new_token"]
                break
            else:
                pass
        
        new_file = open(file_path, "w")
        new_file.write(json.dumps(dic_file))
        new_file.close()
        
    def collection_token_set(self, dic_value):
        ## To change cognito token in collection.json file
        ##
        dic_param = dict(dic_value)
        file_name = dic_param["collection_name"]
        file_path = os.path.join(os.getcwd(), "ini", "API_NextDrive", file_name)
        target = ""
        target2 = ""
        target3 = ""
        print(file_path)
        f = open(file_path, "r")
        file = f.read()
        f.close()
        
        dic_file = json.loads(file)
        print(dic_file["item"][0]["name"])
        if dic_file["item"][0]["name"] == dic_param["testcase_name"]:
            target = dic_file["item"][0]["event"][0]["script"]["exec"][12]
            target2 = re.sub(r"^\s+", "", target)
            print(target)
            print("target2")
            print(target2)
        else:
            print("error 1")
        
        if "token" in target2:
            target3 = target2[0:7]
            print("target3")
            print(target3)
        else:
            print("error 2")
        final_target = target3 + "\"" + dic_param["new_token"] + "\","
        dic_file["item"][0]["event"][0]["script"]["exec"][12] = final_target
        print(dic_file)
        json_file = json.dumps(dic_file)
        print("========================================================")
        print(json_file)
        
        file1 = open(file_path, "w")
        file1.write(json_file)
        file1.close()
        
    def id_token_get(self): 
        ## will modify, move parameter to ini file
        strAWSRegion = 'ap-northeast-1'
        str_ID_token = ""
        try:
            client = boto3.client('cognito-idp', region_name=strAWSRegion, config = botocore.client.Config(signature_version = UNSIGNED))
            objAWS = AWSSRP(
                    username = 'automan+99@nextdrive.io', 
                    password = 'link4581', 
                    pool_id = 'ap-northeast-1_6g3pjHvHo', 
                    client_id = '4lmvkrpfbpurass53hv0vglr0r', 
                    client = client
                )
            dicToken = objAWS.authenticate_user()
            str_ID_token = dicToken['AuthenticationResult']['IdToken']
            #print(dicToken)
            print("Cognito token")
            print(str_ID_token)
        except Exception as exceptionError:
            #raise error.equalerror()
            print("Exception---->")
            print(exceptionError)
            #raise error.equalerror()
            #raise error.equalerror() 
        return str_ID_token
    
    def api_count_get(self):
        self.total = self.total + 1

        final_result = self.total - 1
        
        return final_result