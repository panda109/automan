#coding=utf-8
"""
Created on 2021/05/07
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
    
    def user_detail_email_get(self, dic_value):
        ## Get email in response body and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body 
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_mail = []
        list_mail.append(json_file["email"])
        print("\n" + list_mail + "\n")
        return list_mail
        
    def user_detail_registeredAt_get(self, dic_value):
        ## Get user registered time and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_mail_registeredAt = []
        list_mail_registeredAt.append(json_file["registeredAt"])
        print("\n" + list_mail_registeredAt + "\n")
        return list_mail_registeredAt
        
    def user_detail_ios_version_get(self, dic_value):
        ## Get user ios version and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_ios_version = []
        for i in range(len(json_file["iosVersion"])):
            list_ios_version.append(json_file["iosVersion"][i]["version"])
        print("\n" + list_ios_version + "\n")
        return list_ios_version
        
    def user_detail_ios_version_activatedAt_get(self, dic_value):
        ## Get user ios version activatedAt and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.laods(dic_param["response_body"])
        list_ios_version_activatedAt = []
        for i in range(len(json_file["iosVersion"])):
            list_ios_version_activatedAt.append(json_file["iosVersion"][i]["activatedAt"])
        print("\n" + list_ios_version_activatedAt + "\n")
        return list_ios_version_activatedAt       
    
    def user_detail_android_version_get(self, dic_value):
        ## Get user android version and store in list
        ## For Get_User_Detail
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_android_version = []
        for i in range(len(json_file["androidVersions"])):
            list_android_version.append(json_file["androidVersions"][i]["version"])
        print("\n" + list_android_version + "\n")
        return list_android_version
        
    def user_detail_android_version_activatedAt_get(self, dic_value):
        ## Get user android version activatedAt and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_android_activatedAt = []
        for i in range(len(json_file["androidVersions"])):
            list_android_activatedAt.append(json_file["androidVersions"][i]["activatedAt"])
        print("\n" + list_android_activatedAt + "\n")
        return list_android_activatedAt
    
    def user_detail_gateways_model_get(self, dic_value):
        ## Get user GW model and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_model = []
        for i in range(len(json_file["gateways"])):
            list_gateways_model.append(json_file["gateways"][i]["model"])
        print("\n" + list_gateways_model + "\n")
        return list_gateways_model
        
    
    def user_detail_gateways_pid_get(self, dic_value):
        ## Get user GW pid and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_pid = []
        for i in range(len(json_file["gateways"])):
            list_gateways_pid.append(json_file["gateways"][i]["pid"])
        print("\n" + list_gateways_pid + "\n")
        return list_gateways_pid
        
    def user_detail_gateways_status_get(self, dic_value):
        ## Get user GW status and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_online_status = []
        for i in range(len(json_file["gateways"])):
            list_gateways_online_status.append(json_file["gateways"][i]["onlineStatus"]["status"])
        print("\n" + list_gateways_online_status + "\n")
        return list_gateways_online_status
        
    def user_detail_gateways_updatedAt_get(self, dic_value):
        ## Get user GW updatedAt and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_online_status_updatedAt = []
        for i in range(len(json_file["gateways"])):
            list_gateways_online_status_updatedAt.append(json_file["gateways"][i]["onlineStatus"]["updatedAt"])
        print("\n" + list_gateways_online_status_updatedAt + "\n")
        return list_gateways_online_status_updatedAt
        
    def user_detail_gateways_ip_get(self, dic_value):
        ## Get user GW ip and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_ip = []
        for i in range(len(json_file["gateways"])):
            list_gateways_ip.append(json_file["gateways"][i]["ip"])
        print("\n" + list_gateways_ip + "\n")
        return list_gateways_ip
        
    def user_detail_gateways_fw_vers_get(self, dic_value):
        ## Get user GW FW version and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_fw_version = []
        for i in range(len(json_file["gateways"])):
            list_gateways_fw_version.append(json_file["gateways"][i]["firmware"]["version"])
        print("\n" + list_gateways_fw_version + "\n")
        return list_gateways_fw_version
        
    def user_detail_gateways_fw_updatedAt_get(self, dic_value):
        ## Get user GW FW updatedAt and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_fw_updatedAt = []
        for i in range(len(json_file["gateways"])):
            list_gateways_fw_updatedAt.append(json_file["gateways"][i]["firmware"]["updatedAt"])
        print("\n" + list_gateways_fw_updatedAt + "\n")
        return list_gateways_fw_updatedAt
        
    def user_detail_gateways_location_get(self, dic_value):
        ## Get user GW location and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_gateways_location = []
        for i in range(len(json_file["gateways"])):
            for j in range(len(json_file["gateways"][i]["location"])):
                list_gateways_location.append(json_file["gateways"][i]["location"][j])
        print("\n" + list_gateways_location + "\n")
        return list_gateways_location
        
    def user_detail_gateways_device_model_get(self, dic_value):
        ## Get user GW device model and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_device_model = []
        for i in range(len(json_file["gateways"])):
            for j in range(len(json_file["gateways"][i]["devices"])):
                list_device_model.append(json_file["gateways"][i]["devices"][j]["model"])
        print("\n" + list_device_model + "\n")
        return list_device_model
        
    def user_detail_gateways_device_status_get(self, dic_value):
        ## Get user GW device status and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_device_status = []
        for i in range(len(json_file["gateways"])):
            for j in range(len(json_file["gateways"][i]["devices"])):
                list_device_status.append(json_file["gateways"][i]["devices"][j]["onlineStatus"]["status"])
        print("\n" + list_device_status + "\n")
        return list_device_status
        
    def user_detail_gateways_device_updatedAt_get(self, dic_value):
        ## Get user GW device updatedAt and store in list
        ## For Get_User_Detail API
        ## Parameters:
        ##      - response_body
        dic_param = dict(dic_value)
        json_file = json.loads(dic_param["response_body"])
        list_device_updatedAt = []
        for i in range(len(json_file["gateways"])):
            for j in range(len(json_file["gateways"][i]["devices"])):
                list_device_updatedAt.append(json_file["gateways"][i]["devices"][j]["onlineStatus"]["updatedAt"])
        print("\n" + list_device_updatedAt + "\n")
        return list_device_updatedAt

     