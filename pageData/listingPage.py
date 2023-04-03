from selenium.webdriver.common.by import By


class listingClass:
    
    def __init__(self,driver):
        self.driver = driver
        
    paginationLastSelector = (By.XPATH,"(//button[@aria-current='page'])[last()]")
    paginationsFirstSelector = (By.XPATH,"(//button[@aria-current='page'])[1]")
    hmocardSelector = (By.XPATH,"(//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3'])/div")
    
    
    
    def PaginationLast(self):
        return self.driver.find_element(*listingClass.paginationLastSelector)
    
    def PaginationFirst(self):
        return self.driver.find_elements(*listingClass.paginationsFirstSelector)
    
    def procardCount(self):
        return self.driver.find_elements(*listingClass.hmocardSelector)