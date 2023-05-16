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
from pageData.contactusPage import contactusClass
import pytest
import string
import random
N = 7

class Test_contact_us_form(Invokation):
    
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = ''.join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res+"@yopmail.com"
    
    def test_contact_us_form(self):
        
        log = self.getLogger()
        
        contactpageUrl = "https://www.universityliving.com/contact"
        thankyouURL = "https://www.universityliving.com/thankyou?page=contact"
        
        self.driver.implicitly_wait(5)
        
        homepage = Homepageclass(self.driver)
        contactpage = contactusClass(self.driver)
        
        
        homepage.contactus().click()
        contactpage.fullName().send_keys("test test")
        contactpage.email().send_keys(Test_contact_us_form.newEmail)
        contactpage.phoneNumber().send_keys(Test_contact_us_form.phone_number)
        contactpage.travellingCountry().click()
        contactpage.selectCountry().click()
        contactpage.comment().send_keys("this is test msg :)")
        contactpage.submitBtn().click()
        time.sleep(3)
        
        if self.driver.current_url == thankyouURL:
            log.info("Thank You Url is working fine")
        else:
            log.critical("Thank you URL is not correct plz check")
        self.driver.save_screenshot("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\forms\\contact_us.png")
        contactpage.okBtn().click()
        
        self.driver.save_screenshot("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\forms\\After_contact_us.png")
        
        if self.driver.current_url == contactpageUrl:
            log.info("contact page url is working fine")
        else:
            log.critical("contact page url is not correct plz check")