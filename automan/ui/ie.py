'''
Created on 2010/12/15

@author: panda.huang
'''
from selenium import webdriver

class Ie(object):
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
            self.ie = webdriver.Chrome(chrome_options=options)
            self.ie.get(url)

        if browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.privatebrowsing.autostart", True)
            self.ie = webdriver.Firefox(firefox_profile=profile)
            #self.ie = webdriver.Firefox()
            self.ie.maximize_window()   
            self.ie.get(url)

        if browser == "ie":
            self.ie = webdriver.Ie()
            self.ie.maximize_window()            
            #print self.driver.get_window_size()
            self.ie.get(url)

        '''
        Constructor
        '''
        
    def getie(self):
        return self.ie

    def delie(self):
        self.ie.quit()