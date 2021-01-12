'''
Created on Aug 21, 2020

@author: tim
'''

'''
https://{API_SEVER}/api/v1/subset/{subset}/projects/{projectName}/approval/{buildNumber}
{
  "qaComments": the_comments,    
  "qaApproval": "approved"             // {"approved" | "rejected"} 
}
'''
import sys,time,requests
from junitparser import JUnitXml

if __name__ == '__main__':
    argv = sys.argv[1:]
    project = argv[0]
    buildnumber = argv[1]
    subset = argv[2]
    logfile = argv[3]
    xml = JUnitXml.fromfile(logfile)
    time.sleep(1)
    res = "approved"
    for suite in xml:
        if (str(suite).find('pass') == -1):
            res = "rejected"
    qa_std = "https://frs.nextdrive.io/api/v1/subset/"+subset+"/projects/"+project+"/approval/"+buildnumber
    print(qa_std)
    json_data = {
            "qaComments": "QA auto test result",    
            "qaApproval": res
            }
    #{"approved" | "rejected"} 
    r = requests.post(qa_std, data = json_data )
    print(r)