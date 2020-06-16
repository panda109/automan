# -*- coding: utf-8 -*-
'''
Created on 2020/06/16

@author: Shawn Lin
'''
import automan.tool.error as error
import requests,base64,json

class apicalls(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass

    def accesstoken_get(self, value_dict):
        bolResult = True
        dicParm = dict(value_dict)
        #print("API dicParm",dicParm)
        try:
            strAutho = '%s:%s' % (dicParm['strID'],dicParm['strSecret'])
            byteAutho = strAutho.encode('utf-8')
            base64Autho = base64.b64encode(byteAutho)
            strFinalAutho = '%s %s' % (dicParm['strPrefixOfAutho'],base64Autho.decode('utf-8'))
            
            dicHeader = {dicParm['strHeaderAutho']:strFinalAutho, dicParm['strHeaderContentType']:dicParm['strHeaderConTypeValue']}
            dicBody = {dicParm['strBodyGrantType']:dicParm['strBodyGrantTypeValue'], dicParm['strBodyScope']:dicParm['strScopeRange']}
            objResponse = requests.post(dicParm['strURL'], data=dicBody, headers=dicHeader)
            dicResponse = objResponse.json()
    
            if objResponse.status_code != 200:
                raise error.equalerror()
            elif dicResponse["expires_in"] != 3600:
                raise error.equalerror()
            elif dicResponse["token_type"] != 'Bearer':
                raise error.equalerror()
            else:
                #print(dicResponse["access_token"])
                return dicResponse["access_token"]
        except:
            #raise error.notfind()
            raise error.equalerror()
        

    def gwstate_get(self, value_dict):
        bolResult = True
        dicParm = dict(value_dict)
        #print("API dicParm",dicParm)
        try:
            strGWM_URL = dicParm['strNDAPIServer'] + dicParm['strNDAPIServerPath'] % dicParm['strProductID']
            strGWM_Autho = '%s %s' % (dicParm['strAuthoType'],dicParm['AToken'])
            
            dicGWM_Header = {dicParm['strHeaderAutho']:strGWM_Autho}
            dicGWM_Params={dicParm['strParame_ProID']:dicParm['strProductID']}
            objGWMResponse = requests.get(strGWM_URL, params=dicGWM_Params, headers=dicGWM_Header)
            dicGWMResponse = objGWMResponse.json()
            #print("dicGWMResponse",dicGWMResponse)
            
            if objGWMResponse.status_code != 200:
                raise error.equalerror()
            elif dicGWMResponse["message"] != "success":
                raise error.equalerror()
            elif dicGWMResponse["data"]["state"] != dicParm['strGWState']:
                raise error.equalerror()
            #else:
            #    return bolResult
        except:
            raise error.equalerror()
        