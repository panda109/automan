'''
Created on 2020/4/16

@author: helmut liu

'''
from saker.fuzzers.fuzzer import Fuzzer
from saker.brute.brute  import Brute
from saker.brute.basicAuth import BasicAuth
from saker.handler.headerHandler import HeaderHandler
import os
import pycurl
import base64
import json
from urllib.parse import urlencode
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
        self.rootFuzzDB = self.systemini['fuzzdbroot']
        
        #if str(qa_filename).find('.txt') > 0:
        for dirname, dirnames, filenames in os.walk(self.rootFuzzDB):  
                #add fuzz category name from fuzzdb directory structure
                #print(dirnames)
                if len(dirnames) > 0: 
                    self.FuzzCategoryList.append(dirnames)                   
                   
        #elif str(qa_filename).find('.qa') > 0:
        #    qa_list.append(self.get_qa_file(qa_filename))
        #take first level directory name as category
        #print (self.FuzzCategoryList[0])

        
    def uri_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #uri_key#: key name of uri parameter or name of header
        #attack#: fuzz attack category
        '''
    def header_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #header_data#: normal header data
        #header_key# : the value of key to be fuzzed
        #attack#: fuzz attack category
        '''
        uri = dicParm['uri']
        scheme = dicParm['method']
        header_data = dicParm['header_data']
        fuzzkey = dicParm['header_key']
        cfuzz = dicParm['attack']
        #a list of fuzzed payload
        fPayload = self.get_payload(cfuzz.lower())
        
        #first normal request 
        token = request_auth()
        request_sent(token, uri,scheme, header_data, '')
        #followed fuzz requests
        for payload in fPayload:
            
            header_data= fuzzkey+':'+ payload
            rep= request_sent(token, uri,scheme, header_data, '')




    def body_fuzzing_run(self, value_dict):
        dicParm = dict(value_dict)
         
        '''
        Take param from qa file for testing url, parameter to be fuzzed and fuzz attack category
        #method# : GET,POST,PUT
        #uri# : tested web site url/api 
        #body_data#: key name of uri parameter or name of header
        #body_key
        #attack#: fuzz attack category
        '''
    def scan_api(self,cfuzz='xss'):
        '''
        Specific fuzz category to load payload files beneath defined category
        '''
        
        print(self.rootFuzzDB)
        self.get_payload(cfuzz.lower())
        
        

    def input_mutator(self):
        
        '''
        '''  
    
    def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    # On Python 3, decoding step is required.
        header_line = header_line.decode('iso-8859-1')
         
        if ':' not in header_line:
            return

        name, value = header_line.split(':', 1)
        name = name.strip().lower()
        value = value.strip()

        headers[name] = value

    def request_auth(self):
        '''
        Retrieve access token from oauth 
        '''
        uri = self.currentlyini['nd_oauth2_uri']
        id = self.currentlyini['iij_key_id']
        secret = self.currentlyini['iij_key_secret']
        enc_auth = (id +':'+ secret).encode('utf-8')
        b64_auth = base64.b64encode(enc_auth)
        print(b64_auth.decode('utf-8'))
        head_auth = "Authorization : Basic " + str(b64_auth.decode('utf-8'))
        body_auth = []
        body_auth.append('grant_type='+self.currentlyini['grant_type'])
        body_auth.append('client_id='+self.currentlyini['client_id'])

        res = self.request_sent('', uri,'POST', head_auth, body_auth)
        print(json.loads(res))
        #return json.loads(res)['access_token']

    def get_payload(self,cfuzz):
        payload=[]
        for dirname, dirnames, filenames in os.walk(os.path.join(self.rootFuzzDB, cfuzz)):   
            print(filenames)              
            
            for filename in filenames:
               if str(filename).find('.txt'):
                   lines = dirname + os.sep + filename
                   print(lines)
                   try:
                       for line in open(lines):
                           print(line)
                           payload.append(line.strip())
                   except:
                        pass
            
        if len(payload) == 0 :
            print ("can't find " + cfuzz)
            #raise error.notfindfile()
        else:
            
            return payload

    def request_sent(self,token='', plUri='' ,plScheme='GET', plHead='', plBody=''):
        import certifi
        
        dataBuf = BytesIO()
        req = pycurl.Curl()
        hList = ''
        headers=['content-type:application/x-www-form-urlencoded','cache-control: no-cache']
        
        if plScheme == 'POST' :
            print(plBody)
            enc_body= urlencode(plBody)
            req.setopt(req.POSTFIELDS, enc_body)
        elif plScheme == 'PUT':
            req.setopt(req.UPLOAD, 1)
        else :
            req.setopt(req.HTTPGET,1)
            
        req.setopt(req.URL, plUri)
        req.setopt(req.CAINFO, certifi.where())
        
        #for i in range(len(plHead.split(','))):
        #      header.append(plHead.split(',')[i])
        headers.append(plHead)
        req.setopt(req.HTTPHEADER, headers)
        if len(token) > 0:
            req.setopt(req.XOAUTH2_BEARER,token)
        req.setopt(req.WRITEDATA, dataBuf)
        print(req.POSTFIELDS)
        
        try:
          req.perform()
        except:
          print("Fail to send request")
        
        '''     
        encoding = None
        if 'content-type' in headers:
            content_type = headers['content-type'].lower()
            match = re.search('charset=(\S+)', content_type)
            if match:
                encoding = match.group(1)
                print('Decoding using %s' % encoding)
        if encoding is None:
        # Default encoding for HTML is iso-8859-1.
        # Other content types may have different default encoding,
        # or in case of binary data, may have no encoding at all.
            encoding = 'iso-8859-1'
            print('Assuming encoding is %s' % encoding)

        body = buffer.getvalue()
        # Decode using the encoding we figured out.
        print(body.decode(encoding))        
        '''

        print ("Response: ",req.getinfo(req.RESPONSE_CODE))
        print ("Time taken: ",req.getinfo(req.TOTAL_TIME))
        return dataBuf.getvalue()
        
        req.close()
