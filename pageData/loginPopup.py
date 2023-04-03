from selenium.webdriver.common.by import By

class loginpopupClass:
    def __init__(self,driver):
        self.driver = driver
        
        
    emailfieldSelector = (By.ID,"email")
    loginBtnSelector = (By.XPATH,"//div[text()='Login']")
    otp1Selector = (By.NAME,"otp0")
    otp2Selector = (By.NAME,"otp1")
    otp3Selector = (By.NAME,"otp2")
    otp4Selector = (By.NAME,"otp3")
    otp5Selector = (By.NAME,"otp4")
    continueBtnSelector = (By.XPATH,"//div[text()='Continue']")
    profileiconSelector = (By.XPATH,"//a[@href='/dashboard?tab=booking']")
    dashboardemailSelector = (By.XPATH,"(//p[text()='harsh.sachan@universityliving.com'])")
    profilesectionSelector = (By.XPATH,"(//img[@alt='Profile'])")
    profileemailSelector = (By.XPATH,"(//p[text()='harsh.sachan@universityliving.com'])[2]")
    
    
    def emailfield(self):
        return self.driver.find_element(*loginpopupClass.emailfieldSelector)
    
    def loginBtn(self):
        return self.driver.find_element(*loginpopupClass.loginBtnSelector)
    
    def otpFirst(self):
        return self.driver.find_element(*loginpopupClass.otp1Selector)
    
    def otpsecond(self):
        return self.driver.find_element(*loginpopupClass.otp2Selector)
    
    def otpthird(self):
        return self.driver.find_element(*loginpopupClass.otp3Selector)
    
    def otpfourth(self):
        return self.driver.find_element(*loginpopupClass.otp4Selector)
    
    def otpfifth(self):
        return self.driver.find_element(*loginpopupClass.otp5Selector)
    
    def continueBtn(self):
        return self.driver.find_element(*loginpopupClass.continueBtnSelector)
    
    def profileIcon(self):
        return self.driver.find_element(*loginpopupClass.profileiconSelector)
    
    def dashboardEmail(self):
        return self.driver.find_element(*loginpopupClass.dashboardemailSelector)
    
    def profileSection(self):
        return self.driver.find_element(*loginpopupClass.profilesectionSelector)
    
    def profileEmail(self):
        return self.driver.find_element(*loginpopupClass.profileemailSelector)

        
        
    