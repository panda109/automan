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
import sys
import junitparser
from junitparser import JUnitXml
from junitparser import Element, Attr, TestSuite

if __name__ == '__main__':
    argv = sys.argv[1:]
    print(argv[0],argv[1],argv[2],argv[3])
    project = argv[0]
    buildnumber = argv[1]
    subset = argv[2]
    logfile = argv[3]
    xml = JUnitXml.fromfile(logfile)
    print(xml)
    for suite in xml:
    # handle suites
        print(suite)
        for case in suite:
        # handle cases
            print(case)
            print(case.index("pass"))
    #qa_std = "https://{API_SEVER}/api/v1/subset/{subset}/projects/{projectName}/approval/{buildNumber}"
    #headers = {'Content-Type': 'application/json' , 'nextdrive-uuid' : cube_uuid , 'nextdrive-session' : token}
    #r = requests.post(qa_std, data = json_data , headers = headers )