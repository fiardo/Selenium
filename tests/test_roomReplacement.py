from pytest import mark
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
from pageData.services import Servicesclass
import pytest


@pytest.mark.skip()
class Test_RoomReplacement(Invokation):
    @mark.testomatio("@T6f6f3725")
    def test_roomReplacemnet(self):
        roomReplacementURL = (
            "https://www.universityliving.com/services/room-replacement"
        )
        thankyouPageURl = (
            "https://www.universityliving.com/services/room-replacement/thank-you"
        )
        homepageObj = Homepageclass(self.driver)
        roomreplacementObj = roomreplacementclass(self.driver)
        serviceObj = Servicesclass(self.driver)
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass
        try:
            servicesOnheader = homepageObj.headerServices()
            action = ActionChains(self.driver)
            action.move_to_element(servicesOnheader).perform()
            time.sleep(2)
            homepageObj.roomReplacement().click()
            log.info("room replacement from header")
        except Exception:
            homepageObj.services().click()
            serviceObj.roomreplacement().click()
            log.info("room replacement from service page")
        roomreplacementObj.firstname().send_keys("test")
        roomreplacementObj.lastname().send_keys("test")
        roomreplacementObj.contactNumber().send_keys("8505813979")
        roomreplacementObj.email().send_keys("harsh.sachan@univeristyliving.com")
        roomreplacementObj.currentPrice().send_keys("100")
        roomreplacementObj.UniverisityName().send_keys("uni")
        roomreplacementObj.unidropdownItem().click()
        roomreplacementObj.currentProperty().send_keys("scape swanston")
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
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\services\\RoomReplacement.png"
        )
        assert thankyouPageURl == self.driver.current_url
        if thankyouPageURl == self.driver.current_url:
            log.info("page url is working")
        else:
            log.warning("page url is different plz check")
        roomreplacementObj.okButton().click()
        assert roomReplacementURL == self.driver.current_url
        if roomReplacementURL == self.driver.current_url:
            log.info("After submission page is fine")
        else:
            log.warning("Page break")
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\python\\FrameWorkDesign2\\logs&Repos\\services\\AfterClickOnOKButtonRoomReplacement.png"
        )
