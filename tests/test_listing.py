import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.listingPage import listingClass
import pytest

@pytest.mark.skip()
class Test_lising(Invokation):
    
    def test_listing_e2e(self):
        
        log = self.getLogger()
        
        self.driver.implicitly_wait(5)
        
        homepageObj = Homepageclass(self.driver)
        listingObj = listingClass(self.driver)
        
        homepageObj.searchbar().send_keys("melbo")
        time.sleep(3)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        lastPage = listingObj.PaginationLast().text
        listingObj.PaginationLast().click()
        time.sleep(3)
        listOfPropertiesinlastpae = listingObj.procardCount()
        lastPagePropCount = len(listOfPropertiesinlastpae) -1 
        log.info("total element in last page"+ str(lastPage))
        
        # ------------------------------- properties count -------------------------------------------

        totalPropcount = ((int(lastPage) -1 )*12) + lastPagePropCount
        log.info(totalPropcount)