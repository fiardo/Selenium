from selenium.webdriver.common.by import By

class detailpageClass:
    
    def __init__(self,driver):
        self.driver = driver
        
    enquireBtnSelector = (By.XPATH,"//div[text()='Enquire']")
    booknowBtnSelector = (By.XPATH,"//div[text()='Book Now']")    
    viewMoreRoomSelector = (By.XPATH,"//div[text()='View More Room Types']")
    joinwaitlistBtnSelector = (By.XPATH,"//div[text()='Join Waitlist']")
    joinwaitlistlastBtnSelector = (By.XPATH,"(//div[text()='Join Waitlist'])[last()]")
    
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