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
import pytest
from pageData.thankyouPage import ThankyouClass


class Test_book_now_existing_user(Invokation):
    def test_bookNowForm_existing_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        HomePage = Homepageclass(self.driver)
        DetailPage = detailpageClass(self.driver)
        Form = FormClass(self.driver)
        loginPopUP = loginpopupClass(self.driver)
        ThankyouPage = ThankyouClass(self.driver)
        propertyFlag = False

        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass

        HomePage.newsLetterEmail().send_keys("hs5686584@gmail.com")
        HomePage.newsLetterSubscribe().click()
        HomePage.closeBtnSubscribe().click()

        time.sleep(3)

        # need to create assertions for the contact us form.
