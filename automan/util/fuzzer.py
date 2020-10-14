'''
Created on 2020/4/16

@author: helmut liu

'''
#from saker.fuzzers.fuzzer import Fuzzer
from saker.brute.brute  import Brute
#from saker.brute.basicAuth import BasicAuth
from saker.handler.headerHandler import HeaderHandler
import os
import pycurl
import base64
import json
from urllib.parse import urlencode
from urllib.parse import quote
from automan.tool.parse_file import Parse_file
#import automan.tool.error as error
from io import BytesIO

class fuzzer(object):
    
    def __init__(self):
        '''
        Get fuzz db path for enumerating the funzzing payload files
        '''
        
        self.FuzzCategoryList=[]
        self.systemini = Parse_file().get_ini('system.ini')
        self.currentlyini = Parse_file().get_ini('fuzzer.ini')
        #print (os.path.join(os.getcwd(), 'ini','API','golden_sample.json'))
        self.body_json = json.load(open(os.path.join(os.getcwd() , 'ini','API','golden_sample.json'))) 
        self.rootFuzzDB = self.systemini['fuzzdbroot']
        
        for dirname, dirnames, filenames in os.walk(self.rootFuzzDB):  
                #add fuzz category name from fuzzdb directory structure under attack folder
                #print(dirnames)
                if len(dirnames) > 0: 
                    self.FuzzCategoryList.append(dirnames)                   
        #print (self.FuzzCategoryList[0])

        
    def uri_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        
        for url like ndplay.nextdrive.io/nextdriveapi?xxx=yyy&zzz=<payload>, 
        add the desired parameter at last of uri as fuzzed key/value
        for url with path parameter /v1/gateways/%s/state , a replacement of %s within uri from qa file 

        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #urikey#: key name of uri parameter 
        #urivalue#: normal value of urikey
        #attack#: fuzz attack category
        '''
        uri = dicParm['uri']
        scheme = dicParm['method']
        kUri = dicParm['urikey']
        vUri = dicParm['urivalue']
        cfuzz = dicParm['attack']
        #load payload data
        fPayload = self.get_payload(cfuzz.lower())
        
        #first normal auth request 
        token = self.request_auth()
        
        #triage different url parameter usage
        if '/%s/' in uri:
            uReq = uri % vUri
        elif '?' in uri: 
            uReq = uri.strip() + '&' + kUri + '=' + vUri
        else:
            uReq = uri.strip() + '?' + kUri + '=' + vUri 

        print(uReq)
        hHdlr = HeaderHandler()
        hHdlr.set('Authorization', 'Bearer ' + token)
        hHdlr.set('Content-Type', 'application/json')
        #first normal request
        body_sample=json.dumps(self.body_json['data_retrieval'], indent=2, ensure_ascii=False)
        res = self.request_sent(uReq ,scheme, hHdlr.headers, body_sample)
        
        #status = res['code']
        #time = res['total time']
        rep = res['response']
        print(rep)

        for payload in fPayload:
            
            fzReq = uReq.replace(vUri, payload)
            print(fzReq)
            try:
               res = self.request_sent(fzReq ,scheme, hHdlr.headers, body_sample)
               
            except:
                 print('failed to sent fuzzing requests')
            if res['code'] == 200:
                 #status = res['code']
                 #rep = res['response']
                 print(payload)


    def header_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        for modified http request headers

        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #header_data#: normal header data
        #header_key# : the value of key to be fuzzed
        #attack#: fuzz attack category
        '''
        uri = dicParm['uri']
        scheme = dicParm['method']
        kHeader = dicParm['hdrkey']
        vHeader = dicParm['hdrvalue']
        cfuzz = dicParm['attack']

        #a list of fuzzed payload
        fPayload = self.get_payload(cfuzz.lower())
        
        #first normal request 
        token = self.request_auth()

        hHdlr = HeaderHandler()
        hHdlr.set('Authorization', 'Bearer ' + token)
        hHdlr.set('Content-Type', 'application/json')
        hHdlr.set(kHeader, vHeader)
        #print(hHdlr.headers['Content-Type'])
        body_sample=json.dumps(self.body_json['data_retrieval'], indent=2, ensure_ascii=False)
        res = self.request_sent(uri ,scheme, hHdlr.headers, body_sample)
        
        status = res['code']
        time = res['total time']
        rep = res['response']
        print(status)
        #print(json.loads(rep))
        #print(hHdlr.headers)
        #followed fuzz requests
        for payload in fPayload:
            hHdlr.set(kHeader,payload)
            #print(hHdlr.headers)
            try:
               res = self.request_sent(uri ,scheme, hHdlr.headers, body_sample)
               
            except:
                 print('failed to sent fuzzing requests')
            if res['code'] == 200:
                 status = res['code']
                 rep = res['response']
                 print(payload)

    def jsonbody_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        for modified http request body key value pairs, support json 

        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #body_data#: sample body data
        #body_key# : key name of request body
        #attack#: fuzz attack category
        '''
        #uri = dicParm['uri']
        #scheme = dicParm['method']
        json_file = dicParm['jsonfile']
        json_body = dicParm['bodycommand']
        #kBody = dicParm['bodykey']
        #vBody = dicParm['bodyvalue']
        #cfuzz = dicParm['attack']

        fJson = json.load(open(os.path.join(os.getcwd() , 'ini','API',json_file)))
        body_sample=json.dumps(fJson[json_body], indent=2, ensure_ascii=False)
        dicParm['bodysample']= body_sample
        #a list of fuzzed payload
        #first normal request 
        #token = self.request_auth()

        #hHdlr = HeaderHandler()
        #hHdlr.set('Authorization', 'Bearer ' + token)
        #hHdlr.set('Content-Type', 'application/json')
        #hHdlr.set(kHeader, vHeader)
        #print(hHdlr.headers['Content-Type'])
        
        
        #res = self.request_sent(uri ,scheme, hHdlr.headers, body_sample)
        print(body_sample)
        print(fJson[json_body]['target'][0]['pid'])
        #print(self.body_json['data_retrieval']['query'][0]['pid'])
        #tBody = body_sample.replace(self.body_json['data_retrieval']['query'][0]['pid'], vBody)
        #self.body_fuzzing_run(self,dicParm[])
    

    def body_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        for modified http request body key value pairs, support json 

        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #body_data#: sample body data
        #body_key# : key name of request body
        #attack#: fuzz attack category
        '''
        uri = dicParm['uri']
        scheme = dicParm['method']
        kBody = dicParm['bodykey']
        vBody = dicParm['bodyvalue']
        cfuzz = dicParm['attack']
        #json_file = dicParm['jsonfile']
        json_body = dicParm['bodycommand']
        
        if  'jsonfile' in dicParm :
            fJson = json.load(open(os.path.join(os.getcwd() , 'ini','API', dicParm['jsonfile'])))
            print(fJson)
            body_sample = json.dumps(fJson[json_body], indent=2, ensure_ascii=False)
            body_value = fJson[json_body][kBody]
            
        else :
            body_sample = json.dumps(self.body_json['data_retrieval'], indent=2, ensure_ascii=False)
            body_value = self.body_json['data_retrieval']['query'][0]['pid']

        print(body_sample)
        print(body_value)
        #a l ist of fuzzed payload
        fPayload = self.get_payload(cfuzz.lower())
        
        #first normal request 
        token = self.request_auth()

        hHdlr = HeaderHandler()
        hHdlr.set('Authorization', 'Bearer ' + token)
        hHdlr.set('Content-Type', 'application/json')
        #hHdlr.set(kHeader, vHeader)
        #print(hHdlr.headers['Content-Type'])
        
        
        res = self.request_sent(uri ,scheme, hHdlr.headers, body_sample)
        
        tBody = body_sample.replace(body_value, vBody)

        status = res['code']
        time = res['total time']
        rep = res['response']
        
        #print(tBody)
        #print(hHdlr.headers)
        #followed fuzz requests
        for payload in fPayload:
            fBody = tBody.replace(vBody, payload)
            #print(hHdlr.headers)
            try:
               res = self.request_sent(uri ,scheme, hHdlr.headers, fBody)
               
            except:
                 print('failed to sent fuzzing requests')
            if res['code'] == 200:
                 status = res['code']
                 rep = res['response']
                 print(rep)
                 

    def scan_api(self,cfuzz='xss'):
        '''
        Specific fuzz category to load payload files beneath defined category
        '''
        
        print(self.rootFuzzDB)
        self.get_payload(cfuzz.lower())
        
        

    def input_mutator(self):
        
        '''
        '''  
    def request_auth(self):
        '''
        Retrieve access token from oauth2
        Update url, user id , secret in fuzzer.ini for different user/application/project
        '''
        uri = self.currentlyini['nd_oauth2_uri']
        id = self.currentlyini['iij_key_id']
        secret = self.currentlyini['iij_key_secret']
        enc_auth = (id +':'+ secret).encode('utf-8')
        b64_auth = base64.b64encode(enc_auth)
        print(b64_auth.decode('utf-8'))
        hHdlr = HeaderHandler()
        hHdlr.set('Authorization', 'Basic ' + str(b64_auth.decode('utf-8')))
        hHdlr.set('Content-Type', 'application/x-www-form-urlencoded')
        
        body_auth = {}
        body_auth['grant_type']= self.currentlyini['grant_type']
        body_auth['client_id']=self.currentlyini['client_id']

        res = self.request_sent( uri,'POST', hHdlr.headers, body_auth)
        token = json.loads(res['response'])['access_token']
        #print(json.loads(res)['access_token'])
        return token

    def get_payload(self,cfuzz):
        payload=[]
        for dirname, dirnames, filenames in os.walk(os.path.join(self.rootFuzzDB, cfuzz)):   
            print(filenames)              
            
            for filename in filenames:
               if '.txt' in str(filename):
                   lines = dirname + os.sep + filename
                   print(lines)
                   try:
                       for line in open(lines):
                           #print(line)
                           payload.append(line.strip())
                   except:
                        pass
            
        if len(payload) == 0 :
            print ("can't find " + cfuzz)
            #raise error.notfindfile()
        else:
            
            return payload

    def request_sent(self,plUri='' ,plScheme='GET', plHead=[], plBody=[]):
        import certifi
        
        dataBuf = BytesIO()
        req = pycurl.Curl()
        #hList = ''
        #headers=['content-type:application/x-www-form-urlencoded','cache-control: no-cache']
        if 'json' in str(plHead['Content-Type']):
            enc_body = plBody
        elif 'urlencoded' in str(plHead['Content-Type']):
            enc_body = urlencode(plBody)
        
        if plScheme == 'POST' :
            #print(enc_body)
            #enc_body= quote(plBody)
            req.setopt(req.POSTFIELDS, enc_body)
        elif plScheme == 'PUT':
            req.setopt(req.UPLOAD, 1)
        else :
            req.setopt(req.HTTPGET,1)
            
        req.setopt(req.URL, plUri)
        req.setopt(req.CAINFO, certifi.where())
        #print(plHead)
        #for i in range(len(plHead.split(','))):
        #      header.append(plHead.split(',')[i])
        #headers.append(plHead)
        if len(plHead) > 0 :
            req.setopt(req.HTTPHEADER, [k+':'+v for k,v in plHead.items()])
        
        req.setopt(req.WRITEDATA, dataBuf)
        #req.setopt(req.VERBOSE,1)
        try:
          req.perform()
        except:
          print("Fail to send request")
             
        print ("Response:{} Time taken: {}".format(req.getinfo(req.RESPONSE_CODE),req.getinfo(req.TOTAL_TIME)))
        #print ("Time taken: ",req.getinfo(req.PRIMARY_IP))
        ret = {}
        ret['code'] = req.getinfo(req.RESPONSE_CODE)
        ret['total time']= req.getinfo(req.TOTAL_TIME)
        ret['response']= dataBuf.getvalue()
        dataBuf.close()
        req.close()

        return ret
        