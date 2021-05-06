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

class api_egplus_app(object):
    def __init__(self):  
        pass
    
    def notification_threshold_uuid_get(self, dic_value):
        ## Get uuid in response body and store in list
        ## Project - EG+
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        print("\n")
        print(dic_param["response_body"])
        print(type(dic_param["response_body"]))
        json_file = json.loads(dic_param["response_body"])
        list_uuid = []
        list_uuid.append(json_file["uuid"])
        print(list_uuid)
        return list_uuid
    
    def notification_threshold_name_get(self, dic_value):
        ## Get name in response body and store in list
        ## Project - EG+
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_name = []
        list_name.append(json_file["name"])
        print(list_name)
        return list_name
    
    def notification_threshold_model_get(self, dic_value):
        ## Get model in response body and store in list
        ## Project - EG+
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_model = []
        list_model.append(json_file["model"])
        print(list_model)
        return list_model
        
    def notification_threshold_status_get(self, dic_value):
        ## Get online status in response body and store in list
        ## Project - EG+
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_status = []
        list_status.append(json_file["onlineStatus"])
        print(list_status)
        return list_status

    def notification_threshold_mac_get(self, dic_value):
        ## Get MAC in response body and store in list
        ## Project - EG+
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_mac = []
        list_mac.append(json_file["attributes"]["macAddress"])
        print(list_mac)
        return list_mac    
    # 050621 not done
    def device_info_by_uuid_uuid_get(self, dic_value):
        ## Get uuid in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard API
        ## Parameters:
        ##      - response body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_uuid = []
        list_uuid.append(json_file["uuid"])
        print(list_uuid)
        return list_uuid
       
    def device_info_by_uuid_name_get(self, dic_value):
        ## Get name in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard API
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_name = []
        list_name.append(json_file["name"])
        print(list_name)
        return list_name
        
    def device_info_by_uuid_model_get(self, dic_value):
        ## Get model in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard API
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_model = []
        list_model.append(json_file["model"])
        print(list_model)
        return list_model
        
    def device_info_by_uuid_status_get(self, dic_value):
        ## Get status in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard API
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_status = []
        list_status.append(json_file["onlineStatus"])
        print(list_status)
        return list_status
      
    def device_info_by_uuid_battery_get(self, dic_value):
        ## Get battery % in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_battery = []
        list_battery.append(json_file["info"]["battery"])
        print(list_battery)
        return list_battery
    
    def device_info_by_uuid_motion_get(self, dic_value):
        ## Get motion info in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_motion = []
        list_motion.append(json_file["info"]["motion"])
        print(list_motion)
        return list_motion

    def device_info_by_uuid_generated_time_get(self, dic_value):
        ## Get generatedAt in response body and store in list
        ## For Get_device_info_by_UUID_for_dashboard
        ## Parameters:
        ##      - response_body: input response body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_generated = []
        list_generated.append(json_file["info"]["generatedAt"])
        print(list_generated)
        return list_generated
    
    
    
    
    
    
    
    
    
    