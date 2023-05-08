from selenium.webdriver.common.by import By

class FormClass:
    def __init__(self,driver):
        self.driver = driver
        
    firstnameSelector = (By.ID,"firstName")
    lastnameSelector = (By.ID,"lastName")
    emailSelector = (By.ID,"email")
    phonenumberSelector = (By.ID,"contactNumber")
    visastatusSelector = (By.NAME,"visaStatus")
    universityID1Selector = (By.ID,":r1:")
    universityID2Selector = (By.ID,":r2:")
    universityID3Selector = (By.ID,":r3:")
    universityID4Selector = (By.ID,":r4:")
    univeristyID5Selector = (By.ID,":r5:")
    uniItemSelector = (By.ID,"university-search-item-0")
    platformSelector = (By.NAME,"platformToReach")
    platformInfoselector = (By.NAME,"platformInfo")
    messageSelector = (By.ID,"message")
    submitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    BookNowSubmitBtnSelector = (By.XPATH,"(//div[text()='Book Now'])[last()]")
    genderRadioSelector = (By.XPATH,"//span[text()='Male']")
    homeAddressSelector = (By.ID,"g_address")
    countrySelector = (By.NAME,"country")
    stateSelector = (By.ID,"state")
    citySelector = (By.ID,"city")
    postalSelector = (By.ID,"postalCode")
    nationalitySelector = (By.NAME,"nationality")
    nextBtnSelector = (By.XPATH,"//div[text()='Next']")
    courseSelector = (By.NAME,"courseName")
    yearOfstudySelector = (By.NAME,"yearOfStudy")
    startdateSelector = (By.NAME,"startDate")
    startdateMonthSelector = (By.XPATH,"//div[text()='Dec']")
    enddateSelector = (By.NAME,"endDate")
    enddateMonthSelector = (By.XPATH,"//div[text()='Dec']")
    guardianFnameSelector = (By.ID,"name")
    guardianEmailSelector = (By.NAME,"email")
    guardianNumberSelector = (By.ID,"contactNo")
    relationshipSelector = (By.ID,"relationship")
    messageSelector = (By.NAME,"message")
    guardianDOBselector = (By.ID,"dob")
    guardianDOBdateSelector = (By.XPATH,"(//td[text()=30])[2]")
    sourceSelector = (By.NAME,"source")
    sourceNameSelector = (By.ID,"sourceName")
    guardiansubmitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    universityEmailSelector = (By.ID,"email")
    dateofBirthselector = (By.ID,"dateOfBirth")
    dateONEofDOBselector = (By.XPATH,"(//td[text()='1'])[2]")
    studentIDselctor = (By.ID,"studentId")
    coursenameselctor = (By.ID, "courseName")
    OKbtnSelector = (By.XPATH,"//div[text()='OK']")
    pastAttendSelector = (By.NAME,"previousUniversity")
    pastCourseSelector = (By.NAME,"previousCourseName")
    
    def firstName(self):
        return self.driver.find_element(*FormClass.firstnameSelector)
    
    def lastName(self):
        return self.driver.find_element(*FormClass.lastnameSelector)
    
    def email(self):
        return self.driver.find_element(*FormClass.emailSelector)
    
    def phoneNumber(self):
        return self.driver.find_element(*FormClass.phonenumberSelector)
    
    def visaStatus(self):
        return self.driver.find_element(*FormClass.visastatusSelector)
    
    def uniIDone(self):
        return self.driver.find_element(*FormClass.universityID1Selector)
    
    def uniIDtwo(self):
        return self.driver.find_element(*FormClass.universityID2Selector)
    
    def uniIDthree(self):
        return self.driver.find_element(*FormClass.universityID3Selector)
    
    def uniIDfour(self):
        return self.driver.find_element(*FormClass.universityID4Selector)
    
    def uniIDfive(self):
        return self.driver.find_element(*FormClass.univeristyID5Selector)
    
    def uniItem(self):
        return self.driver.find_element(*FormClass.uniItemSelector)
    
    def platform(self):
        return self.driver.find_element(*FormClass.platformSelector)
    
    def platformInfo(self):
        return self.driver.find_element(*FormClass.platformInfoselector)

    def message(self):
        return self.driver.find_element(*FormClass.messageSelector) 
    
    def submitBtnEnquire(self):
        return self.driver.find_element(*FormClass.submitBtnSelector)   
    
    def bookNowBtn(self):
        return self.driver.find_element(*FormClass.BookNowSubmitBtnSelector)
    
    def genderBtn(self):
        return self.driver.find_element(*FormClass.genderRadioSelector)
    
    def homeField(self):
        return self.driver.find_element(*FormClass.homeAddressSelector)

    def countryDrop(self):
        return self.driver.find_element(*FormClass.countrySelector)

    def stateField(self):
        return self.driver.find_element(*FormClass.stateSelector)

    def cityField(self):
        return self.driver.find_element(*FormClass.citySelector)
    
    def postalField(self):
        return self.driver.find_element(*FormClass.postalSelector)
    
    def nationalityDrop(self):
        return self.driver.find_element(*FormClass.nationalitySelector)

    def nextBtn(self):
        return self.driver.find_element(*FormClass.nextBtnSelector)
    
    def courseField(self):
        return self.driver.find_element(*FormClass.courseSelector)
    
    def yearofstudyField(self):
        return self.driver.find_element(*FormClass.yearOfstudySelector)
    
    def startDateField(self):
        return self.driver.find_element(*FormClass.startdateSelector)

    def endDateField(self):
        return self.driver.find_element(*FormClass.enddateSelector)
    
    def startdateMonth(self):
        return self.driver.find_element(*FormClass.startdateMonthSelector)
    
    def enddateMonth(self):
        return self.driver.find_element(*FormClass.enddateMonthSelector)
    
    def guardianFullname(self):
        return self.driver.find_element(*FormClass.guardianFnameSelector)
    
    def guardianEmail(self):
        return self.driver.find_element(*FormClass.guardianEmailSelector)
    
    def guardianContact(self):
        return self.driver.find_element(*FormClass.guardianNumberSelector)
    
    def guardianRelationship(self):
        return self.driver.find_element(*FormClass.relationshipSelector)
    
    def message(self):
        return self.driver.find_element(*FormClass.messageSelector)
    
    def guardianDOB(self):
        return self.driver.find_element(*FormClass.guardianDOBselector)
    
    def guardianDOBDate(self):
        return self.driver.find_element(*FormClass.guardianDOBdateSelector)
    
    def source(self):
        return self.driver.find_element(*FormClass.sourceSelector)
    
    def sourceName(self):
        return self.driver.find_element(*FormClass.sourceNameSelector)
    
    def guardianSubmitBtn(self):
        return self.driver.find_element(*FormClass.guardiansubmitBtnSelector)
    
    def universityemail(self):
        return self.driver.find_element(*FormClass.universityEmailSelector)
    
    def dateofbirth(self):
        return self.driver.find_element(*FormClass.dateofBirthselector)
    
    def date1ofDOB(self):
        return self.driver.find_element(*FormClass.dateONEofDOBselector)
    
    def studentID(self):
        return self.driver.find_element(*FormClass.studentIDselctor)
    
    def courseName(self):
        return self.driver.find_element(*FormClass.coursenameselctor)
    
    def OKbtnThankyou(self):
        return self.driver.find_element(*FormClass.OKbtnSelector)
    
    def pastAttend(self):
        return self.driver.find_element(*FormClass.pastAttendSelector)
    
    def pastCourse(self):
        return self.driver.find_element(*FormClass.pastCourseSelector)