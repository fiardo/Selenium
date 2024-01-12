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


class Test_New_Bank_Account(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/bank-account"

    def test_New_Bank_Account(self):
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
        assert self.driver.current_url == Test_New_Bank_Account.page_url

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("Ireland")

        bank.openAccountBtn().click()

        login.emailfield().send_keys(Test_New_Bank_Account.new_email.lower())
        log.info("used new email in bank account ->" + Test_New_Bank_Account.new_email)
        login.loginBtn().click()
        login.firstName().send_keys("test")
        login.lastName().send_keys("test")
        login.phoneNumber().send_keys(Test_New_Bank_Account.new_phoneNumber)
        log.info(
            "used new phone number in bank account ->"
            + Test_New_Bank_Account.new_phoneNumber
        )
        login.signUpBtn().click()
        login.otpFirst().send_keys("1")
        login.otpsecond().send_keys("2")
        login.otpthird().send_keys("3")
        login.otpfourth().send_keys("4")
        login.otpfifth().send_keys("5")
        login.continueBtn().click()
        log.info("used new email for bank account ->" + Test_New_Bank_Account.new_email)
        log.info(
            "used new phone number for bank account ->"
            + Test_New_Bank_Account.new_phoneNumber
        )
        bank.openAccountBtn().click()
        Form.uniPlaceholderValue().click()
        Form.uniItem().click()
        bank.formSubmitBtn().click()
        time.sleep(2)

        time.sleep(2)
        self.driver.refresh()

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
