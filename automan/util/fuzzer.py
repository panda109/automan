'''
Created on 2020/4/16

@author: helmut liu

'''
from saker.fuzzers.fuzzer import Fuzzer
from saker.brute.brute  import Brute
from saker.brute.basicAuth import BasicAuth
from saker.handler.headerHandler import HeaderHandler
import pycurl
from io import BytesIO

class fuzzer(object):
    
    def __init__(self, param):
        '''
        Get fuzz db path for enumerating the funzzing payload files
        '''
        
    def uri_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #pfuzz#: key name of uri parameter or name of header
        #attack#: fuzz attack category
        '''
    def header_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #pfuzz#: key name of uri parameter or name of header
        #attack#: fuzz attack category
    def scan_api(self):
       '''
       Specific fuzz category to load payload files beneath defined category
       '''
    def input_mutator(self):
       '''
       '''  
    
    def request_auth(self)
       '''
       Retrieve access token from oauth 
       '''

    def request_sent(self,token, plUri,plScheme="GET", plHead,plBody=""):
        import certifi
        
        dataBuf = BytesIO()
        req = pycurl.Curl()
        hList = ""

        if plSheme="POST"
            req.setopt(req.HTTPPOST,1)

        req.setopt(req.URL, plUri)
        req.setopt(req.HTTPHEADER, plHead)
        req.setopt(req.XOAUTH2_BEARER,token)
        req.setopt(req.WRITEDATA, dataBuf)

        req.setopt(req.CAINFO, certifi.where())
        
        try:
          req.perform()
        except:
          print("Fail to send request")
            
        
        print ("Response: %n",req.getinfo(RESPONSE_CODE))
        print ("Time taken: %n",req.getinfo(TOTAL_TIME))
        return dataBuf.getvalue()
        req.close()
