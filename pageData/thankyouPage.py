from selenium.webdriver.common.by import By

class ThankyouClass:
    
    def __init__(self,driver):
        self.driver = driver
        
# ---------------------------- Selectors ---------------------------------

    chat_Btn_selector = (By.XPATH,"//span[text()='Chat with Student Expert']")
    explore_community_btn_selector = (By.XPATH,"//a[text()='Explore Community']")





# ----------------------------Methods -----------------------------------

    def chat_Btn(self):
        return self.driver.find_element(*ThankyouClass.chat_Btn_selector)
    
    def explore_community(self):
        return self.driver.find_element(*ThankyouClass.explore_community_btn_selector)
    
    
     