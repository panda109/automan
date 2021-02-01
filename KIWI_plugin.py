'''
Created on 2021年1月29日

@author: automan
'''
from tcms_api import TCMS
#arguments, author, author_id, case_run, case_status, case_status_id, category, category_id, component, create_date, default_tester, default_tester_id, email_settings, extra_link, id, is_automated, notes, plan, priority, priority_id, requirement, reviewer, reviewer_id, script, summary, tag, testcasecomponent, testcaseplan, testcasetag, text">
if __name__ == '__main__':
    rpc_client = TCMS()
    
    for case in rpc_client.exec.TestRun.get_cases(60):
        print(case)    
        if case['is_automated'] == True:
            case['status'] = "PASSED"
            case.update()
            rpc_client.exec.TestExecution.update(case['execution_id'],{'status':4})
        
        #default_tester
        #print(test_case.update(3013))