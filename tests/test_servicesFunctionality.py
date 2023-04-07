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
from pageData.roomReplacement import roomreplacementclass
import pytest

@pytest.mark.skip()
class Test_BookNowForms(Invokation):
    
    def test_servicesFunctionality(self):
        
        homepageObj = Homepageclass(self.driver)
        roomreplacementObj = roomreplacementclass(self.driver)
        
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        
        servicesOnheader = homepageObj.headerServices()
        
        action = ActionChains(self.driver)
        action.move_to_element(servicesOnheader).perform()
        time.sleep(5)
        homepageObj.roomReplacement().click()
        
        roomreplacementObj.firstname().send_keys("test")
        roomreplacementObj.lastname().send_keys("test")
        roomreplacementObj.contactNumber().send_keys("8505813979")
        roomreplacementObj.email().send_keys("harsh.sachan@univeristyliving.com")
        roomreplacementObj.currentPrice().send_keys("100")
        roomreplacementObj.UniverisityName().send_keys("test uni")
        roomreplacementObj.currentProperty().sned_keys("scape swanston")
        roomreplacementObj.tenacyStart().click()
        roomreplacementObj.tenacyCalendarStartDate().click()
        roomreplacementObj.tenacyEnd().click()
        roomreplacementObj.tenacycalendarEndDate().click()
        roomreplacementObj.message().send_keys("test message")
        roomreplacementObj.needProperty().click()
        roomreplacementObj.Propertyname().send_keys("new property")
        roomreplacementObj.propertyLocation().send_keys("test location")
        roomreplacementObj.zipcode().send_keys("201301")
        roomreplacementObj.submitButton().click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\services\\RoomReplacement.png")
        