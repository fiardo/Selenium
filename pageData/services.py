from selenium.webdriver.common.by import By

class Servicesclass:
    
    def __init__(self,driver):
        self.driver = driver
        
        
    roomReplacementselector = (By.XPATH,"//a[@href='/services/room-replacement']")
    
    def roomreplacement(self):
        return self.driver.find_element(*Servicesclass.roomReplacementselector)