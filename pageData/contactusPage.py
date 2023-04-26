from selenium.webdriver.common.by import By

class contactusClass:
    
    def __init__(self,driver):
        self.driver = driver
        
        
    fullNameSelector = (By.ID,"fullName")
    emailSelector = (By.ID,"Email")
    phoneNumberSelector = (By.ID,"contactNumber")
    travellingCountrySelector = (By.XPATH,"//input[@placeholder='Travelling Country']")
    selectCountrySelector = (By.ID,"-item-0")
    commentsSelector = (By.NAME,"userMessage")
    submitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    okBtnSelector = (By.XPATH,"//div[text()='OK']")
    
    
    def fullName(self):
        return self.driver.find_element(*contactusClass.fullNameSelector)
    
    def email(self):
        return self.driver.find_element(*contactusClass.emailSelector)
    
    def phoneNumber(self):
        return self.driver.find_element(*contactusClass.phoneNumberSelector)
    
    def travellingCountry(self):
        return self.driver.find_element(*contactusClass.travellingCountrySelector)
    
    def selectCountry(self):
        return self.driver.find_element(*contactusClass.selectCountrySelector)
    
    def comment(self):
        return self.driver.find_element(*contactusClass.commentsSelector)

    def submitBtn(self):
        return self.driver.find_element(*contactusClass.submitBtnSelector)
    
    def okBtn(self):
        return self.driver.find_element(*contactusClass.okBtnSelector)