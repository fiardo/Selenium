from selenium.webdriver.common.by import By



class roomreplacementclass:
    
    def __init__(self,driver):
        self.driver = driver
        
        
    firstnameSelector = (By.ID,"firstName")
    lastnameSelector = (By.ID,"lastName")
    contactNoSelector = (By.XPATH, "//input[@placeholder = 'Contact Number']")
    emailSelector = (By.ID, "email")
    currentPriceSelector = (By.ID,"accommodationPrice")
    universityNameSelector = (By.XPATH,"//input[@placeholder = 'Type University Name']")
    currentPropertySelector = (By.ID,"currentAccommodation")
    tenacyStartSelector = (By.ID, "tenancyStartDateRoomReplacement")
    tenacyCalendarStartDateSelector = (By.XPATH, "(//td[text()='1'])[2]")
    tenacyEndSelector = (By.ID,"tenancyEndDateRoomReplacement")
    tenacycalendarEndDateSelector = (By.XPATH,"(//td[text()='30'])[2]")
    messageSelector = (By.ID,"message")
    needPropertySelector = (By.XPATH,"//label[text()='Yes']")
    propertyNameSelector = (By.ID,"propertyName")
    propertyLocationSelector = (By.ID, "propertyLocation")
    zipcodeSelector = (By.ID,"zipcode")
    submitBtnSelector = (By.CLASS_NAME, "submit_button")
    
    
    def firstname(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def lastname(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def contactNumber(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def email(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def currentPrice(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def UniverisityName(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def currentProperty(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def tenacyStart(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def tenacyCalendarStartDate(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def tenacyEnd(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def tenacycalendarEndDate(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def message(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def needProperty(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def Propertyname(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def propertyLocation(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def zipcode(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def submitButton(self):
        return self.driver.find_element(*roomreplacementclass.submitBtnSelector)
    
    
    
    
    
    
    
    
    
    

    