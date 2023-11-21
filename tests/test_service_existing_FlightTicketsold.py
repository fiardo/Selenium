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
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.FlightTickets import FlightTicketClass
import pytest
import string
import random

N = 10


class Test_Existing_Student_Flight_Tickets(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/students-flight-ticket"

    def test_bookNowForm_new_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        flt = FlightTicketClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(
            By.XPATH, "//p[text()='Student Flight Tickets']"
        ).click()
        time.sleep(2)
        self.driver.refresh()

        assert self.driver.current_url == Test_Existing_Student_Flight_Tickets.page_url

        flt.toDestination().click()
        flt.toCitySearchDublin().click()
        flt.returnDate().click()
        flt.lastDate().click()
        flt.travellerAndClass().click()
        flt.searchFlightsBtn().click()

        login.emailfield().send_keys(Test_Existing_Student_Flight_Tickets.email.lower())
        login.loginBtn().click()
        login.otpFirst().send_keys("1")
        login.otpsecond().send_keys("2")
        login.otpthird().send_keys("3")
        login.otpfourth().send_keys("4")
        login.otpfifth().send_keys("5")
        login.continueBtn().click()

        flt.searchFlightsBtn().click()
        flt.submitBtn().click()
        self.driver.get

        time.sleep(3)
        self.driver.back()

        # ------------------------- checking for one way --------------------------

        flt.oneWay().click()
        flt.toDestination().click()
        flt.toCitySearchDublin().click()
        flt.travellerAndClass().click()
        flt.searchFlightsBtn().click()
        flt.submitBtn().click()
        self.driver.back()

        time.sleep(3)
