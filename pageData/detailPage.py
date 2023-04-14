from selenium.webdriver.common.by import By

class detailpageClass:
    
    def __init__(self,driver):
        self.driver = driver
        
    enquireBtnSelector = (By.XPATH,"//div[text()='Enquire']")
    booknowBtnSelector = (By.XPATH,"//div[text()='Book Now']")    
    viewMoreRoomSelector = (By.XPATH,"//div[text()='View More Room Types']")
    joinwaitlistBtnSelector = (By.XPATH,"//div[text()='Join Waitlist']")
    joinwaitlistlastBtnSelector = (By.XPATH,"(//div[text()='Join Waitlist'])[last()]")
    firstnameSelector = (By.NAME, "firstName")
    lastnameSelector = (By.NAME, "lastName")
    phoneNumberSelector = (By.ID,"contactNumber")
    emailSelector = (By.NAME,"email")
    universityDropDown = (By.XPATH,"(//input[@placeholder = 'Select University'])[2]")
    uniItemSelector = (By.ID,"university-search-item-0")    
    messageSelector = (By.NAME,"userMessage")
    submitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    okBtnSelector = (By.XPATH,"//div[text()='OK']")
    
    
    def enquireButton(self):
        return self.driver.find_element(*detailpageClass.enquireBtnSelector)
    
    def booknowButton(self):
        return self.driver.find_element(*detailpageClass.booknowBtnSelector)
    
    def viewMoreRoomBtn(self):
        return self.driver.find_element(*detailpageClass.viewMoreRoomSelector)
    
    def joinwaitlistBtn(self):
        return self.driver.find_element(*detailpageClass.joinwaitlistBtnSelector)
    
    def joinwaitlistLastBtn(self):
        return self.driver.find_element(*detailpageClass.joinwaitlistlastBtnSelector)
    
    def firstname(self):
        return self.driver.find_element(*detailpageClass.firstnameSelector)
    
    def lastname(self):
        return self.driver.find_element(*detailpageClass.lastnameSelector)
    
    def phoneNumber(self):
        return self.driver.find_element(*detailpageClass.phoneNumberSelector)
    
    def email(self):
        return self.driver.find_element(*detailpageClass.emailSelector)
    
    def universityDrop(self):
        return self.driver.find_element(*detailpageClass.universityDropDown)
    
    def universityDROPItem(self):
        return self.driver.find_element(*detailpageClass.uniItemSelector)
    
    def message(self):
        return self.driver.find_element(*detailpageClass.messageSelector)
    
    def submitBtn(self):
        return self.driver.find_element(*detailpageClass.submitBtnSelector)
    
    def okBtn(self):
        return self.driver.find_element(*detailpageClass.okBtnSelector)
    
    
    
    