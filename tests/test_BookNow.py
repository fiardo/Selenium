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
    bookNow_url_one = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you"
    bookNow_url_two = "https://www.universityliving.com/united-kingdom/london/iq-hoxton/book-now/thank-you"
    bookNow_url_three = "https://www.universityliving.com/australia/melbourne/scape-berkeley-2/book-now/thank-you"
    testing_key = "test"
    existing_email_id = "pravin.garg@universityliving.com"
    properties_name = ["chapter ealing", "iQ Hoxton", "scape berkeley 2"]
    Thankyou_urls = [bookNow_url_one, bookNow_url_two, bookNow_url_three]

    def test_bookNowForm_existing_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
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

        assert HomePage.searchbar().is_displayed()
        HomePage.searchbar().send_keys(Test_book_now_existing_user.properties_name[0])
        time.sleep(3)
        HomePage.searchbar().send_keys(Keys.ENTER)
        DetailPage.booknowButton().click()
        # log.info("property name -->" + propertyName)
        assert loginPopUP.loginBtn().is_displayed()
        assert loginPopUP.emailfield().is_displayed()
        assert loginPopUP.loginBtn().is_displayed()
        loginPopUP.emailfield().send_keys(Test_book_now_existing_user.existing_email_id)
        log.info("Existing Email -> pravin.garg@universityliving.com")
        loginPopUP.loginBtn().click()
        loginPopUP.otpFirst().send_keys("1")
        loginPopUP.otpsecond().send_keys("2")
        loginPopUP.otpthird().send_keys("3")
        loginPopUP.otpfourth().send_keys("4")
        loginPopUP.otpfifth().send_keys("5")
        assert loginPopUP.continueBtn().is_displayed()
        loginPopUP.continueBtn().click()
        visastatusDropdown = Select(Form.visaStatus())
        visastatusDropdown.select_by_index(3)
        bestPlatformDropdown = Select(Form.platform())
        bestPlatformDropdown.select_by_index(10)
        Form.platformInfo().send_keys("Dis-test-1")
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
        Form.bookNowBtn().click()
        log.info("partial Book now journey -- success")
        assert Form.booknow_step1_validator().text == "Personal Info"
        if Form.booknow_step1_validator().text == "Personal Info":
            log.info("Partial booking -- completed")
        else:
            log.warning("personal info missing xx Plz check")
        Form.genderBtn().click()
        Form.homeField().send_keys("test Home")
        country = Select(Form.countryDrop())
        country.select_by_index(2)
        Form.stateField().send_keys("test")
        Form.cityField().send_keys("test")
        Form.postalField().send_keys("test")
        nationality = Select(Form.nationalityDrop())
        nationality.select_by_index(2)
        Form.nextBtn().click()
        assert Form.booknow_step2_validator().text == "University Info"
        if Form.booknow_step2_validator().text == "University Info":
            log.info("step 1/3 -- success")
        else:
            log.warning("University info missing nxxx Plz check")
        Form.courseField().send_keys("test course")
        yearofStudy = Select(Form.yearofstudyField())
        yearofStudy.select_by_index(2)
        Form.startDateField().click()
        Form.startdateMonth().click()
        Form.endDateField().click()
        Form.enddateMonth().click()
        Form.pastCourse().send_keys("test past course")
        Form.pastAttend().send_keys("test past university")
        Form.nextBtn().click()
        assert Form.booknow_step3_validator().text == "Guardian Info"
        if Form.booknow_step3_validator().text == "Guardian Info":
            log.info("step 2/3 -- success")
        else:
            log.warning("Guardian info missing xx Plz check")
        Form.guardianFullname().send_keys("test")
        Form.guardianEmail().send_keys("test@yopmail.com")
        Form.guardianContact().send_keys("8100223348")
        Form.guardianRelationship().send_keys("testrelation")
        Form.message().send_keys("testing Message")
        try:
            Form.guardianDOB().click()
            Form.guardianDOBDate().click()
        except Exception:
            log.info("no guardian DOB required")
        sourceDrop = Select(Form.source())
        sourceDrop.select_by_index(3)
        Form.sourceName().send_keys("Mr Test")
        Form.guardianSubmitBtn().click()
        if ThankyouPage.chat_Btn().is_displayed():
            log.info("step 3/3 -- success")
            time.sleep(3)
        else:
            log.warning("step failure")
        # self.driver.get_screenshot_as_file(
        #     "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\BookNowNow.png"
        # )
