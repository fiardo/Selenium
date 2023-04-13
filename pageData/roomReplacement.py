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
    universityDropDownSelector = (By.XPATH,"//p[text()='AECC University College']")
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
    OKbuttonSelector = (By.XPATH, "//button[text()='OK']")
    
    
    
    def firstname(self):
        return self.driver.find_element(*roomreplacementclass.firstnameSelector)
    
    def lastname(self):
        return self.driver.find_element(*roomreplacementclass.lastnameSelector)
    
    def contactNumber(self):
        return self.driver.find_element(*roomreplacementclass.contactNoSelector)
    
    def email(self):
        return self.driver.find_element(*roomreplacementclass.emailSelector)
    
    def currentPrice(self):
        return self.driver.find_element(*roomreplacementclass.currentPriceSelector)
    
    def UniverisityName(self):
        return self.driver.find_element(*roomreplacementclass.universityNameSelector)
    
    def unidropdownItem(self):
        return self.driver.find_element(*roomreplacementclass.universityDropDownSelector)
    
    def currentProperty(self):
        return self.driver.find_element(*roomreplacementclass.currentPropertySelector)
    
    def tenacyStart(self):
        return self.driver.find_element(*roomreplacementclass.tenacyStartSelector)
    
    def tenacyCalendarStartDate(self):
        return self.driver.find_element(*roomreplacementclass.tenacyCalendarStartDateSelector)
    
    def tenacyEnd(self):
        return self.driver.find_element(*roomreplacementclass.tenacyEndSelector)
    
    def tenacycalendarEndDate(self):
        return self.driver.find_element(*roomreplacementclass.tenacycalendarEndDateSelector)
    
    def message(self):
        return self.driver.find_element(*roomreplacementclass.messageSelector)
    
    def needProperty(self):
        return self.driver.find_element(*roomreplacementclass.needPropertySelector)
    
    def Propertyname(self):
        return self.driver.find_element(*roomreplacementclass.propertyNameSelector)
    
    def propertyLocation(self):
        return self.driver.find_element(*roomreplacementclass.propertyLocationSelector)
    
    def zipcode(self):
        return self.driver.find_element(*roomreplacementclass.zipcodeSelector)
    
    def submitButton(self):
        return self.driver.find_element(*roomreplacementclass.submitBtnSelector)
    
    def okButton(self):
        return self.driver.find_element(*roomreplacementclass.OKbuttonSelector)
    
    
    
    
    
    
    
    

    