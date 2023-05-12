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
import string
import random

N = 7
# @pytest.mark.skip()
class Test_DropUsALineclass(Invokation):
    
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = ''.join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res+"@yopmail.com"
        
    propertyUrl = "https://www.universityliving.com/united-kingdom/london/property/iq-hoxton"
    
    def test_dropusaline(self):
        
        log = self.getLogger()
        
        self.driver.implicitly_wait(5)
        
        homepage = Homepageclass(self.driver)
        detailpage = detailpageClass(self.driver)
        
        homepage.searchbar().send_keys("iq hoxton")
        time.sleep(2)
        homepage.searchbar().send_keys(Keys.ENTER)
        detailpage.firstname().send_keys("test")
        detailpage.lastname().send_keys("test")
        detailpage.phoneNumber().send_keys(Test_DropUsALineclass.phone_number)
        detailpage.email().send_keys(Test_DropUsALineclass.newEmail)
        detailpage.universityDrop().click()
        detailpage.universityDROPItem().click()
        detailpage.message().send_keys("test message")
        detailpage.submitBtn().click()
        
        time.sleep(3)
        self.driver.save_screenshot("C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\Drop_Us_A_Line.png")
        
        detailpage.okBtn().click()
        time.sleep(2)
        assert Test_DropUsALineclass.propertyUrl == self.driver.current_url
        
        if Test_DropUsALineclass.propertyUrl == self.driver.current_url:
            log.info("page is working fine")
        else:
            log.critical("URL issue plz check")
        self.driver.save_screenshot("C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\After_Drop_Us_A_Line.png")