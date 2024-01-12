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
from pageData.bankAccount import BankAccountClass
import pytest
import string
import random

N = 10


class Test_Existing_Bank_Account(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/bank-account"

    def test_Existing_Bank_Account(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        bank = BankAccountClass(self.driver)
        Form = FormClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Student Bank Account']").click()
        time.sleep(2)
        self.driver.refresh()
        assert self.driver.current_url == Test_Existing_Bank_Account.page_url

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("Ireland")

        bank.openAccountBtn().click()
        login.loginMethod()
        log.info("used existing email -> harsh.sachan@universityliving.com")
        bank.openAccountBtn().click()

        # try:
        #     Form.univ().click()
        # except Exception:
        #     try:
        #         Form.uniIDtwo().click()
        #     except Exception:
        #         try:
        #             Form.uniIDthree().click()
        #         except:
        #             try:
        #                 Form.uniIDfour().click()
        #             except Exception:
        #                 try:
        #                     Form.uniIDfive().click()
        #                 except Exception:
        #                     log.warning("ID is not interactable")

        Form.uniPlaceholderValue().click()
        Form.uniItem().click()
        bank.formSubmitBtn().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\selenium_things\\selenium_framework\\screenshots\\services\\bank_Account\\irelandBankAccount.png"
        )

        time.sleep(2)
        bank.okBtn().click()

        # ------------------------------ check for canada -----------------------

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("Canada")

        bank.openAccountBtn().click()
        bank.formSubmitBtn().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\selenium_things\\selenium_framework\\screenshots\\services\\bank_Account\\candaBankAccount.png"
        )

        log.info("student bank account - canada -->" + self.driver.current_url)
        self.driver.back()
        time.sleep(2)
