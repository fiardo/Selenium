import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.common.exceptions import NoSuchElementException
import pytest
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
import pytest


class Test_BookNowForms(Invokation):
    
    bookNow_url = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you"
    
    def test_bookNowForm(self):
        
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        formObj = FormClass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        
        

        log.info("using iq hoxton property for enquire form")
        homepageObj.searchbar().send_keys("chapter ealing")
        self.driver.find_element(By.XPATH,"//div[text()='Chapter Ealing']").click()                

        detailpageObj.booknowButton().click()
        
        loginPopUPObj.emailfield().send_keys("pravin.garg@universityliving.com")
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()
        
        
        # enquireformObj.firstName().send_keys("test")
        # enquireformObj.lastName().send_keys("test")
        # enquireformObj.email().send_keys("harsh.sachan@universityliving.com")
        # enquireformObj.phoneNumber().send_keys("8505813979")
        # enquireformObj.message().send_keys("this is test message :)")
        
        
        visastatusDropdown = Select(formObj.visaStatus())
        visastatusDropdown.select_by_index(3)
        bestPlatformDropdown = Select(formObj.platform())
        bestPlatformDropdown.select_by_index(10)
        formObj.platformInfo().send_keys("Discord-ID-Test-1234")
        
        try:
            formObj.uniIDone().click()
        except Exception:
            try:
                formObj.uniIDtwo().click()
            except Exception:
                try:
                    formObj.uniIDthree().click()
                except:
                    try:
                        formObj.uniIDfour().click()
                    except Exception:
                        print('id is not available for the univerisity select field')
           
        formObj.uniItem().click()
        # enquireformObj.submitBtn().click() 
        # time.sleep(5)
        # currenturl = self.driver.current_url
        
        # if Test_EnquireForms.enquireNowUrl == currenturl:
        #     print("test success")
        # else:
        #     print("test failed")

        # print(currenturl)
        
        formObj.bookNowBtn().click()
        formObj.genderBtn().click()
        formObj.homeField().send_keys("test Home")
        country = Select(formObj.countryDrop())
        country.select_by_index(2)
        formObj.stateField().send_keys("test") 
        formObj.cityField().send_keys("test")
        formObj.postalField().send_keys("test")
        nationality = Select(formObj.nationalityDrop())
        nationality.select_by_index(2)
        formObj.nextBtn().click()               
        formObj.courseField().send_keys("test course")
        yearofStudy = Select(formObj.yearofstudyField())
        yearofStudy.select_by_index(2)
        formObj.startDateField().click()        
        formObj.startdateMonth().click()
        formObj.endDateField().click()
        formObj.enddateMonth().click()
        formObj.nextBtn().click()
        formObj.guardianFullname().send_keys("test")
        formObj.guardianEmail().send_keys("test@yopmail.com")
        formObj.guardianContact().send_keys("8100223348")
        formObj.guardianRelationship().send_keys("testrelation")
        formObj.message().send_keys("testing Message")
        formObj.guardianDOB().click()
        formObj.guardianDOBDate().click()
        sourceDrop = Select(formObj.source())
        sourceDrop.select_by_index(3)
        formObj.sourceName().send_keys("Mr Test")
        formObj.guardianSubmitBtn().click()
        time.sleep(10)
        self.driver.get_screenshot_as_file("Book_Now.png")
        
        assert Test_BookNowForms.bookNow_url == self.driver.current_url