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
from pageData.Guarnator import GuarantorClass
import pytest
import string
import random

N = 10


class Test_Existing_Guarantor(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/guarantor"

    def test_Existing_Guarantor(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        guarantor = GuarantorClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Guarantor']").click()
        time.sleep(2)
        self.driver.refresh()
        assert self.driver.current_url == Test_Existing_Guarantor.page_url

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("UK")
        guarantor.findGuarantorBtn().click()
        login.loginMethod()
        guarantor.findGuarantorBtn().click()
        guarantor.formSubmitBtn().click()

        time.sleep(3)
        redirectionUrl = self.driver.current_url
        log.info("UK - Redirection Url -> " + redirectionUrl)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        # ------------------------- for ireland --------------------------

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("Ireland")
        guarantor.findGuarantorBtn().click()
        guarantor.formSubmitBtn().click()

        time.sleep(3)
        redirectionUrl = self.driver.current_url
        log.info("Ireland - Redirection Url -> " + redirectionUrl)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        # ------------------------- for France -------------------------------

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("France")
        guarantor.findGuarantorBtn().click()
        guarantor.formSubmitBtn().click()

        time.sleep(3)
        redirectionUrl = self.driver.current_url
        log.info("France - Redirection Url -> " + redirectionUrl)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        # --------------------------- for USA ---------------------------------

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("USA")
        guarantor.findGuarantorBtn().click()
        guarantor.formSubmitBtn().click()

        time.sleep(3)
        redirectionUrl = self.driver.current_url
        log.info("USA - Redirection Url -> " + redirectionUrl)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
