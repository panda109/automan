#coding=utf-8
"""
Created on 2021/05/06
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

class api_eis(object):
    def __init__(self):  
        pass
    def program_gw_download_pid_get(self, dic_value):
        ## Get pid in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_pid = []
        for i in range(len(json_file["data"])):
            list_pid.append(json_file["data"][i]["pid"])
        print(list_pid)
        return list_pid
        
    def program_gw_download_uuid_get(self, dic_value):
        ## Get uuid in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_uuid = []
        for i in range(len(json_file["data"])):
            list_uuid.append(json_file["data"][i]["uuid"])
        print(list_uuid)
        return list_uuid
        
    def program_gw_download_fw_sku_get(self, dic_value):
        ## Get uuid in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_fw_sku = []
        for i in range(len(json_file["data"])):
            list_fw_sku.append(json_file["data"][i]["firmwareSku"])
        print(list_fw_sku)
        return list_fw_sku
    
    def program_gw_download_createDt_get(self, dic_value):
        ## Get createDt in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_create_time = []
        for i in range(len(json_file["data"])):
            list_create_time.append(json_file["data"][i]["createDt"])
        print(list_create_time)
        return list_create_time
        
    def program_gw_download_syncDt_get(self, dic_value):
        ## Get syncDt in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_sync_time = []
        for i in range(len(json_file["data"])):
            list_sync_time.append(json_file["data"][i]["syncDt"])
        print(list_sync_time)
        return list_sync_time    
        
    def program_gw_download_free_get(self, dic_value):
        ## Get free in response body and store in list
        ## project - EIS
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_free = []
        for i in range(len(json_file["data"])):
            list_free.append(json_file["data"][i]["free"])
        print(list_free)
        return list_free 