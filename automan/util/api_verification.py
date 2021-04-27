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
import json
import csv
import os

class api_verification(object):
    def __init__(self):  
        pass

    def read_csv_get(self, dic_value): 
        ## Read csv file and find the target response
        ##
        ## Parameters:
        ##    - csv_filename
        ##    - testcase_name
        ##
        dic_param = dict(dic_value)
        try:
            #define csv file:
            str_file_path = os.path.join(os.getcwd(), "newman", dic_param["csv_filename"])
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
        list_response = eval(str_response)
        #print(list_response)
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
        os.system(dic_param["command"])
        
    def file_list_get(self, dic_value):
        ## Get file list in folder which stored response csv file
        ## Parameters:
        ##     - folder_path
        ##
        dic_param = dict(dic_value)
        print(os.getcwd())
        str_path = os.path.join(os.getcwd(), dic_param["folder_path"])
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
        str_file_path = os.path.join(os.getcwd(), dic_param["expected_result"])

        
        obj_expected_result = open(str_file_path, "r")
        str_expected_result = obj_expected_result.read()
        print(str_expected_result)
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
