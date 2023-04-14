from selenium.webdriver.common.by import By


class listingClass:
    
    def __init__(self,driver):
        self.driver = driver
        
    paginationLastSelector = (By.XPATH,"(//button[@aria-current='page'])[last()]")
    paginationsFirstSelector = (By.XPATH,"(//button[@aria-current='page'])[1]")
    hmocardSelector = (By.XPATH,"(//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3'])/div")
    descriptionHeaderSelector = (By.XPATH,"//div[text()='Everything About Student Accommodation in London']")
    selectUniversitySelector = (By.XPATH,"//input[@placeholder = 'Select University']")
    universitydropitemselector = (By.ID,"university-search-item-0")
    homeBreadcrumSelector = (By.XPATH,"//a[text() = 'Home']")
    campusSelector = (By.XPATH,"//label[text() = 'Denmark Hill Campus']")
    pageTextSelector = (By.XPATH,"//span[text() = 'Page']")
    uniDescHeaderSelector = (By.XPATH,"//div[text()=\"Everything about student accommodation near King's College London\"]")
    readMoreDescSelector = (By.XPATH,"//label[@for = 'read-more-controller']")
    uniHallCategorySelector = (By.XPATH,"//label[text()='University Halls']")
    firstpropertiesSelector = (By.XPATH,"(//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3']/div)[1]")
    propertylistedSelector = (By.XPATH,"(//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3']/div)")
    
    
    
    def PaginationLast(self):
        return self.driver.find_element(*listingClass.paginationLastSelector)
    
    def PaginationFirst(self):
        return self.driver.find_elements(*listingClass.paginationsFirstSelector)
    
    def procardCount(self):
        return self.driver.find_elements(*listingClass.hmocardSelector)
    
    def cityDescription(self):
        return self.driver.find_element(*listingClass.descriptionHeaderSelector)
    
    def selectUniversity(self):
        return self.driver.find_element(*listingClass.selectUniversitySelector)
    
    def homeBreadcrum(self):
        return self.driver.find_element(*listingClass.homeBreadcrumSelector)
    
    def universityItem(self):
        return self.driver.find_element(*listingClass.universitydropitemselector)
    
    def campusPill(self):
        return self.driver.find_element(*listingClass.campusSelector)    
    
    def pageTextPagination(self):
        return self.driver.find_element(*listingClass.pageTextSelector)
    
    def uniDesc(self):
        return self.driver.find_element(*listingClass.uniDescHeaderSelector)
    
    def readMoreDesc(self):
        return self.driver.find_element(*listingClass.readMoreDescSelector)
    
    def unihallcategory(self):
        return self.driver.find_element(*listingClass.uniHallCategorySelector)
    
    def firstPropertyOnList(self):
        return self.driver.find_element(*listingClass.firstpropertiesSelector)