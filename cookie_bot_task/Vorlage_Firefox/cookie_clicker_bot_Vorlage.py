from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service  
import os
from time import sleep
"""
ToDo: Welche Bibliotheken müssen eingebunden werden?
Lesen Sie hierzu IB-Selenium Webdriver

"""


class cookieBot():

    def __init__(self):

        s = Service('./geckodriver') #Linux und Mac
        self.browser = webdriver.Firefox(service=s) 
    
        # Kopieren Sie den Source Code für CookieClicker aus dem Moodle-Kurs in dieses Verzeichnis
        directory = os.path.realpath(os.path.dirname(__file__)) # diese OS-Methode gibt Dateipfad zurück
        path = 'file://'+ directory + '/CookieClickerSource/index.html' #Dateipfad zum Spiel auf Ihrem PC
        self.browser.get(path)

        """
        -- Ab hier ist die Webseite geladen --
        ToDo: Legen Sie geeignete Variablen an
        """
    def clickCookie(self):
        success = False
        element = self.browser.find_element(By.ID,'bigCookie') 
        element.click()
        success = True
        
        return success
   
bot = cookieBot()
sleep(1)

while(True):
    bot.clickCookie()
