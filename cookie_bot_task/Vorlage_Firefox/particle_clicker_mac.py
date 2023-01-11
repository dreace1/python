from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service  
from time import sleep as schlafen_fuers_laden

class ParticleBot():
    def __init__(self, url, timeout):
        self.url = url
        s = Service('./geckodriver')
        self.browser = webdriver.Firefox(service=s) 
        self.browser.get(self.url) 
        self.browser.implicitly_wait(timeout)

    def click_element(self,element_id):
        success = False
        element = self.browser.find_element(By.ID,'detector-events') 
        element.click()
        success = True
        
        return success

bot = ParticleBot("https://particle-clicker.web.cern.ch/",2) 
schlafen_fuers_laden(1)
while(True): 
    bot.click_element('detector-events')