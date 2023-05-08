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
from pageData.listingPage import listingClass
from pageData.Forms import FormClass
import pytest

# @pytest.mark.skip()
class Test_BookNowForms(Invokation):
    
    bookNow_url = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you"
    
    def test_SeoCampusDescription(self):
        
        log = self.getLogger()       
        self.driver.implicitly_wait(5)
        
        homepageObj = Homepageclass(self.driver)
        listingObj = listingClass(self.driver)
        
        homepageObj.searchbar().send_keys('London')
        self.driver.find_element(By.XPATH,"//div[text()='London']").click()
        eleDescription = listingObj.cityDescription()
        self.driver.execute_script("arguments[0].scrollIntoView();",eleDescription)
        a = listingObj.cityDescription().text
        print(a)
        self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\listing\\listingDescription.png")
        log.info("Description city -->" + a)
        eleTop = listingObj.homeBreadcrum()
        
        
        self.driver.execute_script("arguments[0].scrollIntoView();",eleTop)
        time.sleep(2)
        listingObj.selectUniversity().click()
        listingObj.universityItem().click()
        time.sleep(3)
        uniDescription = listingObj.uniDesc()
        self.driver.execute_script("arguments[0].scrollIntoView();",uniDescription)
        uniDescTitile = listingObj.uniDesc().text
        print(uniDescTitile)
        self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\listing\\UniversityDescription.png")
        log.info("Description university -->" + uniDescTitile)
        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        
        
        listingObj.campusPill().click()
        scrollToPagetextOfPagination = listingObj.pageTextPagination()
        self.driver.execute_script("arguments[0].scrollIntoView();",scrollToPagetextOfPagination)
        
        try:
            readmore = listingObj.readMoreDesc()
            print(readmore.text)
            log.warning("read more is present in campus description. pl check")
            self.driver.get_screenshot_as_file("campusDescription.png")
            
            
        except Exception:
            log.info("No descrioption is available on campus page")
            print("No descrioption is available on campus page")
            self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\listing\\campusDescription.png")

        
        
        