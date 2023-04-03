import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.common.exceptions import NoSuchElementException
import pytest
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
import pytest



# @pytest.mark.usefixtures("setup")  # test in conftest
class Test_LoginE2e(Invokation):        # test class
    def test_E2eLogin(self):            # complete test will be written here
        
        log = self.getLogger()
    
        homepageObject = Homepageclass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        loginEmail = 'harsh.sachan@universityliving.com'
        
        self.driver.implicitly_wait(4)

        homepageObject.loginBtn().click()
        loginPopUPObj.emailfield().send_keys(loginEmail)
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")

        loginPopUPObj.continueBtn().click()
        loginPopUPObj.profileIcon().click()
    
        emailDashboard = loginPopUPObj.dashboardEmail().text
        loginPopUPObj.profileSection().click()
        emailProfile = loginPopUPObj.profileEmail().text 
    
        if (loginEmail == emailDashboard and loginEmail == emailProfile):
            print("Loggin successful")
        else:
            print("there is an error in loggin")

        print("Login email is -->", loginEmail)
        print("Dashboard email is -->", emailDashboard)
        print("profile email is -->", emailProfile)
        # self.driver.refresh()
    
    
# --------- dont forget to use -v and -s for getting the print statement in  pytest console ---------------------------

