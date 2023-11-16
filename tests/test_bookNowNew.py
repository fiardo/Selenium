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
import string
import random

N = 10


class Test_book_now_new_user(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    bookNow_url_one = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you"
    bookNow_url_two = "https://www.universityliving.com/united-kingdom/london/iq-hoxton/book-now/thank-you"
    bookNow_url_three = "https://www.universityliving.com/australia/melbourne/scape-berkeley-2/book-now/thank-you"
    testing_key = "test"
    properties_name = ["chapter ealing", "iQ Hoxton", "scape berkeley 2"]
    Thankyou_urls = [bookNow_url_one, bookNow_url_two, bookNow_url_three]

    @mark.testomatio("@Tf916d5fc")
    def test_bookNowForm_new_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        formObj = FormClass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass
        assert homepageObj.searchbar().is_displayed()
        homepageObj.searchbar().send_keys("chapter ealing")
        time.sleep(2)
        homepageObj.searchbar().send_keys(Keys.RETURN)
        detailpageObj.booknowButton().click()
        loginPopUPObj.emailfield().send_keys(Test_book_now_new_user.new_email)
        log.info("email id -->" + Test_book_now_new_user.new_email)
        loginPopUPObj.loginBtn().click()
        time.sleep(3)
        loginPopUPObj.firstName().send_keys("test")
        loginPopUPObj.lastName().send_keys("test")
        loginPopUPObj.phoneNumber().send_keys(Test_book_now_new_user.new_phoneNumber)
        log.info("phone number -->" + Test_book_now_new_user.new_phoneNumber)
        loginPopUPObj.signUpBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()
        visastatusDropdown = Select(formObj.visaStatus())
        visastatusDropdown.select_by_index(2)
        bestPlatformDropdown = Select(formObj.platform())
        bestPlatformDropdown.select_by_index(10)
        formObj.platformInfo().send_keys("Discord-test")
        formObj.dateofbirth().click()
        formObj.date1ofDOB().click()
        try:
            formObj.uniIDone().click()
        except Exception:
            try:
                formObj.uniIDtwo().click()
            except Exception:
                try:
                    formObj.uniIDthree().click()
                except:
                    try:
                        formObj.uniIDfour().click()
                    except Exception:
                        try:
                            formObj.uniIDfive().click()
                        except Exception:
                            log.warning("ID is not interactable")
        formObj.uniItem().click()
        formObj.bookNowBtn().click()
        formObj.genderBtn().click()
        formObj.homeField().send_keys("test Home")
        country = Select(formObj.countryDrop())
        country.select_by_index(2)
        formObj.stateField().send_keys("test")
        formObj.cityField().send_keys("test")
        formObj.postalField().send_keys("test")
        nationality = Select(formObj.nationalityDrop())
        nationality.select_by_index(2)
        formObj.nextBtn().click()
        formObj.courseField().send_keys("test course")
        yearofStudy = Select(formObj.yearofstudyField())
        yearofStudy.select_by_index(2)
        formObj.startDateField().click()
        formObj.startdateMonth().click()
        formObj.endDateField().click()
        formObj.enddateMonth().click()
        # formObj.pastAttend().send_keys('test')
        # formObj.pastCourse().send_keys('test')
        formObj.nextBtn().click()
        formObj.guardianFullname().send_keys("test")
        formObj.guardianEmail().send_keys("test@yopmail.com")
        formObj.guardianContact().send_keys("8100223348")
        formObj.guardianRelationship().send_keys("testrelation")
        formObj.message().send_keys("testing Message")
        try:
            formObj.guardianDOB().click()
            formObj.guardianDOBDate().click()
        except Exception:
            pass
        sourceDrop = Select(formObj.source())
        sourceDrop.select_by_index(3)
        formObj.sourceName().send_keys("Mr Test")
        formObj.guardianSubmitBtn().click()
        time.sleep(5)
