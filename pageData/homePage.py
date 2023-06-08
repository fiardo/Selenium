from selenium.webdriver.common.by import By

class Homepageclass:
    
    def __init__(self,driver):
        self.driver = driver
        
    searchbarSelector = (By.XPATH,"//input[@placeholder='Search by City, University or Property']")
    loginbtnSelector = (By.XPATH,"//span[text()='Login / SignUp']")
    homepageImgSelector = (By.XPATH,"//img[@alt='University Living']")
    headerServicesSelector = (By.XPATH,"//a[text()='Services']")
    roomreplacementSelector = (By.XPATH,"//a[@href = '/services/room-replacement']")
    servicesSelector = (By.XPATH,"//a[text()='Services']")
    contactusSelector = (By.XPATH,"//a[text()='Contact Us']")
    headerSearchSelector = (By.XPATH,"//input[@placeholder='Search by City, University or Property']")
    chatIcon_Selector = (By.XPATH,"//img[@alt='Chat Icon']")
    
    
    
    def searchbar(self):
        return self.driver.find_element(*Homepageclass.searchbarSelector)
    
    def loginBtn(self):
        return self.driver.find_element(*Homepageclass.loginbtnSelector)
    
    def headerLogo(self):
        return self.driver.find_element(*Homepageclass.homepageImgSelector)
    
    def headerServices(self):
        return self.driver.find_element(*Homepageclass.headerServicesSelector)
    
    def roomReplacement(self):
        return self.driver.find_element(*Homepageclass.roomreplacementSelector)
    
    def services(self):
        return self.driver.find_element(*Homepageclass.servicesSelector)
    
    def contactus(self):
        return self.driver.find_element(*Homepageclass.contactusSelector)
    
    def headerSearch(self):
        return self.driver.find_element(*Homepageclass.headerSearchSelector)
    
    def chatIcon(self):
        return self.driver.find_element(*Homepageclass.chatIcon_Selector)
    
    