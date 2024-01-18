from selenium.webdriver.common.by import By

class Servicelistingclass :
    def __init__(self,driver):
        self.driver = driver
    exploreallserviceselector = (By.XPATH, "//div[text()='Explore All Services']")
    accommodationselector = (By.XPATH, "(//p[text()='Accommodation'])[2]")
    studentflightticketsselector = (By.XPATH, "(//p[text()='Student Flight Tickets'])[2]")
    guarantorselector = (By.XPATH, "(//p[text()='Guarantor'])[2]")
    internationalmoneytransferselector = (By.XPATH, "(//p[text()='International Money Transfer'])[2]")
    studentbankaccountselector = (By.XPATH, "(//p[text()='Student Bank Account'])[2]")
    getvisaselector = (By.XPATH, "(//p[text()='Get Visa'])[2]")
    studentfinancingselector = (By.XPATH, "(//p[text()='Student Financing'])[2]")
    roomessentialsselector = (By.XPATH, "(//p[text()='Room Essentials'])[2]")
    airportpickupselector = (By.XPATH, "(//p[text()='Airport Pickup'])[2]")
    roomreplacementselector = (By.XPATH, "(//p[text()='Room Replacement'])[2]")
    internationalsimselector = (By.XPATH, "(//p[text()='International SIM'])[2]")
    travelinsuranceselector = (By.XPATH, "(//p[text()='Travel Insurance'])[2]")
    healthinsuranceOSHCselector = (By.XPATH, "(//p[text()='Health Insurance - OSHC'])[2]")
    luggagestorageselector = (By.XPATH, "(//p[text()='Luggage Storage'])[2]")
    Forexselector = (By.XPATH, "(//p[text()='Forex'])[2]")
    jobsearchselector = (By.XPATH, "(//p[text()='Job Search'])[2]")
    studentinternshipsselector = (By.XPATH, "(//p[text()='Student Internships'])[2]")
    freeonlinecoursesselector = (By.XPATH, "(//p[text()='Free Online Courses'])[2]")
    Servicenamesselector = (By.XPATH, "//div[@class='my-auto pr-4']/p[1]")
    Servicedetailsselector = (By.XPATH, "//div[@class='my-auto pr-4']/p[2]")


    # ------------------------ Methods ------------------------------------------

    def exploreallservices(self):
        return self.driver.find_element(*Servicelistingclass.exploreallserviceselector)

    def accommodation(self):
        return self.driver.find_element(*Servicelistingclass.accommodationselector)

    def guarantor(self):
        return self.driver.find_element(*Servicelistingclass.guarantorselector)

    def internationalmoneytransfer(self):
        return self.driver.find_element(*Servicelistingclass.internationalmoneytransferselector)
    
    def studentbankaccount(self):
        return self.driver.find_element(*Servicelistingclass.studentbankaccountselector)
    
    def roomessentials(self):
        return self.driver.find_element(*Servicelistingclass.roomessentialsselector)
    
    def airportpickup(self):
        return self.driver.find_element(*Servicelistingclass.airportpickupselector)
    
    def internationalsim(self):
        return self.driver.find_element(*Servicelistingclass.internationalsimselector)
    
    def travelinsurance(self):
        return self.driver.find_element(*Servicelistingclass.travelinsuranceselector)
    
    def healthinsuranceOSHC(self):
        return self.driver.find_element(*Servicelistingclass.healthinsuranceOSHCselector)
    
    def luggagestorage(self):
        return self.driver.find_element(*Servicelistingclass.luggagestorageselector) 
       
    def Forex(self):
        return self.driver.find_element(*Servicelistingclass.Forexselector)
    
    def jobsearch(self):
        return self.driver.find_element(*Servicelistingclass.jobsearchselector)
    
    def studentinternship(self):
        return self.driver.find_element(*Servicelistingclass.studentinternshipsselector)
    
    def freeonlinecourse(self):
        return self.driver.find_element(*Servicelistingclass.freeonlinecoursesselector)
    
    def Servicenames(self):
        return self.driver.find_elements(*Servicelistingclass.Servicenamesselector)

    def Servicedetails(self):
        return self.driver.find_elements(*Servicelistingclass.Servicedetailsselector)











