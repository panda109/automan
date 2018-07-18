import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_web(object):
   '''
   classdocs
   '''
   def __init__(self):
       '''
       Constructor
       '''

   if __name__ == '__main__':        
       driver = webdriver.Chrome()
       driver.get('http://172.16.0.222:8080')
       time.sleep(2)
       driver.find_element_by_id("username").send_keys("admin")
       time.sleep(1)
       elem = driver.find_element_by_id('password').send_keys("admin")
       time.sleep(1)
       elem = driver.find_element_by_id("signin-submit").click()     #signin-submit button
       time.sleep(2)
       #driver.find_element_by_xpath("//div[2]/div/div[2]/div").click()   #refresh button
       driver.find_element_by_xpath("//div[@id='navbar-collapse-main']/ul[2]/li[4]/a").click()
       time.sleep(2)
       driver.find_element_by_id("Sign out").click()
       time.sleep(2)
#         elem = driver.find_element_by_link_text("Hosts") # Hosts button
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_css_selector("div.btn-group.main-group-btn > button.btn")  #create host button
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_id("name")
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_id("ip")
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_id("site")
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_xpath("(//button[@type='button'])[15]")    #cancel button
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_css_selector("div.btn-group.main-group-btn > button.btn")  #create host button
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#         elem = driver.find_element_by_xpath("(//button[@id=''])[4]")     #submit button
#         elem.send_keys(Keys.RETURN)
#         time.sleep(2)
#        driver.find_element_by_css_selector("span.ng-binding").click()   #Cluster View and Physical View switch button
#        time.sleep(2)
#        elem = driver.find_element_by_link_text("Cluster View").click()  # Cluster View button
#        time.sleep(2)
#        path = "//*[@id='sidebar-menu']/li/a/span/i/td[contains(text(),'{0}')]"
#        driver.find_element_by_link_text("hh-server2").click()
#        time.sleep(2)
#        driver.find_element_by_css_selector("span.ng-binding").click()
#        time.sleep(2)    
#        elem = driver.find_element_by_link_text("Physical View").click() #Physical View button
#        time.sleep(2)
#        driver.find_element_by_xpath("//ul[@id='sidebar-menu']/li[4]/ul/li/a/span").click()  #select a instance
#        time.sleep(1)       
#        driver.find_element_by_css_selector("a.dropdown-toggle.component-menu > span").click()   #component-menu dropdown
#        time.sleep(1)
#        driver.find_element_by_link_text("Instances").click()    #Instances button
#        time.sleep(1)
#        driver.find_element_by_xpath("//tr[@id='c1c95e8a-4974-476a-902c-94b25af4978c']/td[6]").click() #select a instance
#        time.sleep(1)       
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()   #instance dropdown-menu
#        time.sleep(1)
#        driver.find_element_by_link_text("Soft Reboot").click()  #instance soft reboot button
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Hard Reboot").click()  #instance hard reboot button
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Stop").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Pause").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Suspend").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()       
#        time.sleep(1)
#        driver.find_element_by_link_text("Lock").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Rescue").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Rebuild").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Resize").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[30]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Migrate").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[60]").click()       
#        time.sleep(1)
#        driver.find_element_by_link_text("Associate Fixed IP").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[46]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Disassociate Fixed IP").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[49]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Associate Floating IP").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[40]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Disassociate Floating IP").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[43]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Update Security Group").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[36]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Backup").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[52]").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
#        time.sleep(1)
#        driver.find_element_by_link_text("Console Log").click()
#        time.sleep(1)
#        driver.find_element_by_xpath("(//button[@type='button'])[57]").click()
#        time.sleep(1)




       
       driver.close() 
