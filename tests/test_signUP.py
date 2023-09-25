from pytest import mark
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
import string
import random

N = 7


class Test_SignupE2e(Invokation):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = "".join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res + ".university@yopmail.com"

    def test_E2eLogin(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        homepageObject = Homepageclass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass

        homepageObject.loginBtn().click()
        loginPopUPObj.emailfield().send_keys(Test_SignupE2e.newEmail.lower())
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.firstName().send_keys("test")
        loginPopUPObj.lastName().send_keys("test")
        loginPopUPObj.phoneNumber().send_keys(Test_SignupE2e.phone_number)
        loginPopUPObj.signUpBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()
        loginPopUPObj.profileIcon().click()
        dashboard_email = self.driver.find_element(
            By.CSS_SELECTOR, ".text-base.text-theme-gray-text.truncate"
        ).text
        if dashboard_email == Test_SignupE2e.newEmail.lower():
            log.info("Sign up id matched with dashboard id")
        else:
            log.warning("email is not matched")
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\homepage&dashboard\\signUP-dashboard.png"
        )
        homepageObject.headerLogo().click()
        log.info("dashboard emai -->" + dashboard_email)
        log.info("sign up email -->" + Test_SignupE2e.newEmail.lower())
        log.info("used contact number for sign up -->" + Test_SignupE2e.phone_number)
