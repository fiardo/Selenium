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
from pageData.getVisa import GetVisaClass
import pytest
import string
import random

N = 10


class Test_New_GetVisa(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/visa-assistance"

    def test_New_Remittance(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        visa = GetVisaClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Get Visa']").click()
        time.sleep(2)
        assert self.driver.current_url == Test_New_GetVisa.page_url
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\selenium_things\\selenium_framework\\screenshots\\services\\get_visa\\visaHomeNew.png"
        )
        time.sleep(1)
        visa.submitBtn().click()
        time.sleep(1)

        assert visa.firstNameError().is_displayed()
        assert visa.lastNameError().is_displayed()
        assert visa.emailError().is_displayed()
        assert visa.phoneNumberError().is_displayed()

        visa.firstName().send_keys("test")
        visa.lastName().send_keys("test")
        visa.email().send_keys("harsh.sachan@universityliving.com")
        visa.phoneNumber().send_keys("8505813979")
        visa.submitBtn().click()

        login.emailfield_using_placeholder().send_keys(Test_New_GetVisa.new_email)
        login.loginBtn().click()

        time.sleep(2)
        login.firstName().send_keys("test")
        login.lastName().send_keys("test")
        login.phoneNumber().send_keys(Test_New_GetVisa.new_phoneNumber)

        log.info("new email for get visa -> " + Test_New_GetVisa.new_email)
        log.info("new phone number for get visa -> " + Test_New_GetVisa.new_phoneNumber)

        login.signUpBtn().click()
        login.otpFirst().send_keys(1)
        login.otpsecond().send_keys(2)
        login.otpthird().send_keys(3)
        login.otpfourth().send_keys(4)
        login.otpfifth().send_keys(5)
        login.continueBtn().click()

        time.sleep(2)

        visa.submitBtn().click()
        time.sleep(3)
        redirection_url_new_user_getVisa = self.driver.current_url
        log.info("redirection url of get visa -> " + redirection_url_new_user_getVisa)

        visa.okBtn().click()
        time.sleep(2)
