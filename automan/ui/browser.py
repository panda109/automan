#coding:utf-8
'''
Created on 2010/12/15

@author: panda.huang
'''
from selenium import webdriver
from appium import webdriver as appium
from automan.tool.parse_file import Parse_file

class Browser(object):
    '''
    classdocs
    '''

    def __init__(self,param,browser):
        if browser  == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")   #chrom browser maximization
            #options.add_argument("-incognito")  #open in incognito mode
            #enable multiple download
            #multi_dl_prefs = {}
            #multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
            #options.add_experimental_option("prefs", multi_dl_prefs)                
            self.browser = webdriver.Chrome(chrome_options=options)
            self.browser.get(param)

        if browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.privatebrowsing.autostart", True)
            self.browser = webdriver.Firefox(firefox_profile=profile)
            self.browser.maximize_window()   
            self.browser.get(param)

        if browser == "ie":
            self.browser = webdriver.Browser()
            self.browser.maximize_window()            
            #print self.driver.get_window_size()
            self.browser.get(param)

        if browser == "app":
            #read from url in to desired_capabilities
            app = []
            app = Parse_file().get_app(param)
            #dc = {}
            for line in list(app):
                print(line)
            
            #self.browser = appium.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities=dc)
            #self.browser.quit()
        '''
        Constructor
        '''
        
    def getie(self):
        return self.browser

    def delie(self):
        self.browser.quit()