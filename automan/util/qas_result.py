#coding=utf-8
'''
Created on 2021/02/09

@author: Dustin Lin
'''
import xml.etree.ElementTree as XET
import automan.tool.error as error  
import os
class qas_result(object):
    def __init__(self):
        '''
        '''
    def result_get(self, value_dict):
        ## get each qa file result in qas
        ##parameter:
        ##    testcase_name: qas testcase name
       
        try:
            dic_Param = dict(value_dict)
            ##Til API_Service qas folder
            folder_path = os.path.join(os.getcwd(), "log", dic_Param["testcase_name"])  
            list_all_file = os.listdir(folder_path)
            list_qa_result = []
            float_qa_runtime = 0
            #str_return_result = "API Service(3rd party) test finished: "
            str_return_title = dic_Param["title"]
            print(str_return_title)
            str_final_result = ""
            ##To get each testcase result, time 
            for i in range(len(list_all_file)):
                tree = XET.parse(folder_path + "\\{filename}\\{filename}.xml".format(filename = list_all_file[i]))
                root = tree.getroot()
                print(root.get("name"), root.get("time"), root.get("result"))
                float_qa_runtime = float_qa_runtime + float(root.get("time"))
                list_qa_result.append(root.get("result"))
            print(list_qa_result)
            print(float_qa_runtime)
            int_run_time_mins = int(int(float_qa_runtime) / 60)
            int_run_time_sec = int(int(float_qa_runtime) % 60)
            ##Verify qas result
            #print("=====")
            #print(str_final_result)
            str_final_result = str_return_title + "\n"
            #print(str_final_result)
            str_final_result = str_final_result + "Testing environment: " + dic_Param["environment"] + "\n"
            #print(str_final_result)
            str_final_result = str_final_result + "------------------------------\n"
            #print(str_final_result)
            str_final_result = str_final_result + "Final result: "
            #print(str_final_result)
            if "fail" in list_qa_result:
                str_final_result = str_final_result + "Fail\n"
            else:
                str_final_result = str_final_result + " Pass\n"
            str_final_result = str_final_result + "Total RunTime: "
            str_final_result = str_final_result + "{} mins: {} sec\n".format(int_run_time_mins, int_run_time_sec)
            #print("=+++++++++++++++++++++++++++++++++++++++++++")
            #print(str_final_result)
            return str_final_result
        except:
            raise error.notfind()
            
            
    def xxx_get(self, value_dict):
        ##test
        dic_param = dict(value_dict)
        print(dic_param["xxx"])
        
        
        
        
        
        
        
        
        
        
        
        
                    