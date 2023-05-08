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
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.listingPage import listingClass
from pageData.roomReplacement import roomreplacementclass
from pageData.services import Servicesclass
import pytest
import string
import random
N = 7

# @pytest.mark.skip()
class Test_unihallClass(Invokation):
          
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = ''.join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res+".university@yopmail.com"
    
    def test_unihallcase(self):
        
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        
        thankyouURL = 'https://www.universityliving.com/thankyou'
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        lisitngObj = listingClass(self.driver)
        formobj = FormClass(self.driver)
        
        
        homepageObj.searchbar().send_keys("London")
        time.sleep(2)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        try:
            lisitngObj.unihallcategory().click()
        except Exception:
            log.info("unihall not available or category is not available")
        
        time.sleep(3)
        try:
            lisitngObj.firstPropertyOnList().click()
        except Exception:
            log.info("no property is available on unihall listing")
        
        time.sleep(3)
         
        detailpageTab = self.driver.window_handles[1]   
        self.driver.switch_to.window(detailpageTab)
        detailpageURL = self.driver.current_url
        log.info(detailpageURL)
        detailpageObj.enquireButton().click()
        
        formobj.firstName().send_keys("test")
        formobj.lastName().send_keys("test")
        formobj.universityemail().send_keys(Test_unihallClass.newEmail)
        formobj.phoneNumber().send_keys(Test_unihallClass.phone_number)
        visa = Select(formobj.visaStatus())
        visa.select_by_index(2)
        
        try:
            formobj.uniIDone().click()
        except Exception:
            try:
                
                formobj.uniIDtwo().click()
            except Exception:
                try:
                    formobj.uniIDthree().click()
                except:
                    try:
                        formobj.uniIDfour().click()
                    except Exception:
                        try:
                            formobj.uniIDfive().click()
                        except Exception:
                            print('id is not available for the univerisity select field')
        
        formobj.uniItem().click()
        formobj.dateofbirth().click()
        formobj.date1ofDOB().click()
        formobj.studentID().send_keys("ID-TEST_007")
        formobj.courseName().send_keys("test course")
        yearofSTUDY = Select(formobj.yearofstudyField())
        yearofSTUDY.select_by_index(2)
        bestPlatform = Select(formobj.platform())
        bestPlatform.select_by_index(10)
        formobj.platformInfo().send_keys("DISCORD-TEST_00")        
        formobj.message().send_keys("test message")
        formobj.submitBtnEnquire().click()
        time.sleep(3)
        
        assert thankyouURL == self.driver.current_url
        
        self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\forms\\unihallThakyou.png")
        
        if thankyouURL == self.driver.current_url:
            log.info("Thank you url page of unihall is Woring fine")
        else:
            log.critical("Thank you url of unihall is not correct , Plz check")
        
        
        
        
        formobj.OKbtnThankyou().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\forms\\afterOKbuttonINunihall.png")
        assert detailpageURL == self.driver.current_url
        
        if detailpageURL == self.driver.current_url:
            log.info("Detail page is working fine after clicking on OK from thank you page")
        else:
            log.critical("The page is broken after clicking on OK from thank you page")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        