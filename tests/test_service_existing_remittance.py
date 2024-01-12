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
from pageData.Remittance import RemittanceClass
import pytest
import string
import random

N = 10


class Test_Existing_Remittance(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/remittance"

    def test_Existing_Remittance(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        remittance = RemittanceClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(
            By.XPATH, "//p[text()='International Money Transfer']"
        ).click()
        time.sleep(2)
        self.driver.refresh()
        assert self.driver.current_url == Test_Existing_Remittance.page_url

        time.sleep(3)
        remittance.recipientInput().clear()
        time.sleep(3)
        remittance.recipientInput().send_keys("200")
        time.sleep(2)
        log.info("sending amount ->" + "200")
        log.info(
            "selected recipients coutnry -> " + remittance.recipientCountryText().text
        )
        log.info("selected Sender amount -> " + remittance.youSendInput().text)
        log.info("selected Sender coutnry -> " + remittance.youSendCountryText().text)
        remittance.sendNowBtn().click()
        login.loginMethodUsingPlaceholder()
        time.sleep(2)
        remittance.sendNowBtn().click()
        remittance.wireTransfer().click()
        remittance.selectProperty().click()
        remittance.firstProperty().click()
        # --------------- detail validations --------------------------------------

        receivingAmount_wt = remittance.receivingAmount().text
        amountNeedToPay_wt = remittance.amountNeedToPay().text
        fxRate_wt = remittance.fxRate().text

        log.info("Receiving amount ->" + receivingAmount_wt)
        log.info("Amount need to pay->" + amountNeedToPay_wt)
        log.info("FX rate wire transfer ->" + fxRate_wt)

        # --------------------------- Redirection Wire transfer ---------------------------------------
        remittance.continueBtn().click()
        time.sleep(3)
        wireTransferRedirectionUrl = self.driver.current_url
        log.info("wire transfer redirection url -> " + wireTransferRedirectionUrl)
        self.driver.back()

        # ---------------------- Agent Assisted --------------------------------

        remittance.agentAssisted().click()
        time.sleep(3)
        remittance.selectProperty().click()
        remittance.firstProperty().click()

        # ------------------------------ detail validation agent assisted --------

        receivingAmount_aa = remittance.receivingAmount().text
        amountNeedToPay_aa = remittance.amountNeedToPay().text
        fxRate_aa = remittance.fxRate().text

        log.info("Receiving amount ->" + receivingAmount_aa)
        log.info("Amount need to pay->" + amountNeedToPay_aa)
        log.info("FX rate of agent assisted->" + fxRate_aa)

        # -------------------------- Redirection agent assisted --------------------

        remittance.continueBtn().click()
        time.sleep(3)
        wireTransferRedirectionUrl = self.driver.current_url
        log.info("Agent assisted redirection url -> " + wireTransferRedirectionUrl)
        self.driver.back()
