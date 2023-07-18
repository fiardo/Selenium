from selenium.webdriver.common.by import By

class DownloadAppclass:
    
    def __init__(self,driver):
        self.driver = driver
        
#---------------------------------------xxx--------------------------------xxx-------------------------------

    pageLink = "https://www.universityliving.com/about"
    title_selector = (By.XPATH,"//h3[text()='Book Accommodation Nearby ']")
    ios_link = "https://apps.apple.com/us/app/university-living/id1614605795?referrer=utm_source%3Dios%26utm_category%3Dheader%26utm_medium%3Ddesktop"
    googlePlay_link = "https://play.google.com/store/apps/details?id=com.universityliving&referrer=utm_source%3Dandroid%26utm_category%3Dheader%26utm_medium%3Ddesktop"
    iosButton_selector = (By.XPATH,"//img[@alt='IOS App']")
    playstore_selector = (By.XPATH,"//img[@alt='Android App']")
        
    def iosButton(self):
        return self.driver.find_element(*DownloadAppclass.iosButton_selector)
    
    def playstoreButton(self):
        return self.driver.find_element(*DownloadAppclass.playstore_selector)

    def title(self):
        return self.driver.find_element(*DownloadAppclass.title_selector)
        
        