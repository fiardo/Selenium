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
from pageData.listingPage import listingClass
import pytest
import string
import random

N = 10


class Test_propertyDetailClass(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])

    def test_property_Details_Verification(self):
        log = self.getLogger()
        login = loginpopupClass(self.driver)
        Homepage = Homepageclass(self.driver)
        listing = listingClass(self.driver)
        Detail = detailpageClass(self.driver)
        Form = FormClass(self.driver)
        self.driver.implicitly_wait(5)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass

        Homepage.searchbar().send_keys("chapter ealing")
        time.sleep(2)
        Homepage.searchbar().send_keys(Keys.RETURN)
        # Detail.booknowButton().click()
        log.info(Detail.stayDurationText().text)
        log.info(Detail.moveText().text)
        log.info(Detail.occupancyText().text)
        log.info(Detail.priceText().text)
        log.info(Detail.totalText().text)

        Detail.booknowButton().click()
        login.emailfield().send_keys(Test_propertyDetailClass.new_email)
        login.loginBtn().click()
        time.sleep(2)
        login.firstName().send_keys("test")
        login.lastName().send_keys("test")
        login.phoneNumber().send_keys(Test_propertyDetailClass.new_phoneNumber)
        login.signUpBtn().click()
        login.otpFirst().send_keys("1")
        login.otpsecond().send_keys("2")
        login.otpthird().send_keys("3")
        login.otpfourth().send_keys("4")
        login.otpfifth().send_keys("5")
        login.continueBtn().click()

        log.info(
            "--------xx--------------------xx------------------xx---------------xx----------------xx----------------xx---------"
        )
        log.info(Detail.formPrice().text)
        log.info(Detail.formRoomName().text)
        log.info(Detail.formDuration().text)
        log.info(Detail.formMoveIn().text)
        log.info(Detail.formMoveOut().text)
        log.info(Detail.formPrice().text)
        log.info(Detail.formTotalPrice().text)
        log.info(Detail.formRoomName().text)

        assert Detail.totalText().text == Detail.formTotalPrice().text
        assert Detail.priceText().text == Detail.formPrice().text
        assert Detail.priceText().text == Detail.formPrice().text
        assert Detail.moveText().text == (
            Detail.formMoveIn().text + " - " + Detail.formMoveOut().text
        )

        visastatusDropdown = Select(Form.visaStatus())
        visastatusDropdown.select_by_index(4)

        try:
            Form.uniIDone().click()
        except Exception:
            try:
                Form.uniIDtwo().click()
            except Exception:
                try:
                    Form.uniIDthree().click()
                except:
                    try:
                        Form.uniIDfour().click()
                    except Exception:
                        try:
                            Form.uniIDfive().click()
                        except Exception:
                            log.warning("ID is not interactable")
        Form.uniItem().click()
        bestPlatformDropdown = Select(Form.platform())
        bestPlatformDropdown.select_by_index(10)
        Form.platformInfo().send_keys("Discord-test")
        Form.dateofbirth().click()
        Form.date1ofDOB().click()
        Form.bookNowBtn().click()

        time.sleep(5)
