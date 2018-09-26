'''
Created on 2010/12/15

@author: panda.huang
'''
from selenium import webdriver

class Browser(object):
    '''
    classdocs
    '''

    def __init__(self,url,browser):

        if browser  == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")   #chrom browser maximization
            #options.add_argument("-incognito")  #open in incognito mode
            #enable multiple download
            #multi_dl_prefs = {}
            #multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
            #options.add_experimental_option("prefs", multi_dl_prefs)                
            self.browser = webdriver.Chrome(chrome_options=options)
            self.browser.get(url)

        if browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.privatebrowsing.autostart", True)
            self.browser = webdriver.Firefox(firefox_profile=profile)
            self.browser.maximize_window()   
            self.browser.get(url)

        if browser == "ie":
            self.browser = webdriver.Browser()
            self.browser.maximize_window()            
            #print self.driver.get_window_size()
            self.browser.get(url)

        '''
        Constructor
        '''
        
    def getie(self):
        return self.browser

    def delie(self):
        self.browser.quit()