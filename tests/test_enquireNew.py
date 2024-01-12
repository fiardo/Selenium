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
from selenium.common.exceptions import NoSuchElementException
import pytest
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
import string
import random

N = 7


class Test_Enquire_new_user(Invokation):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = "".join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res + "@yopmail.com"
    iq_hoxton_thankYou_url = "https://www.universityliving.com/united-kingdom/london/iq-hoxton/enquire-now/thank-you"
    chapter_ealing_thankYou_url = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/enquire-now/thank-you"
    scape_melbourne_central_thankyou_url = "https://www.universityliving.com/australia/melbourne/scape-melbourne-central/enquire-now/thank-you"

    @mark.testomatio("@Tb5d15cfb")
    def test_enquire_new_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        enquireformObj = FormClass(self.driver)

        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass
        assert homepageObj.searchbar().is_displayed()
        homepageObj.searchbar().send_keys("chapter ealing")
        time.sleep(3)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        try:
            detailpageObj.enquireButton().click()
            log.info("IQ hoxton - Enquire Now")
        except Exception:
            homepageObj.headerSearch().send_keys("chapter ealing")
            time.sleep(2)
            homepageObj.headerSearch().send_keys(Keys.ENTER)
            try:
                detailpageObj.enquireButton().click()
                log.info("chapter ealing - Enquire now")
            except Exception:
                homepageObj.headerSearch().send_keys("scape melbourne central")
                time.sleep(2)
                homepageObj.headerSearch().send_keys(Keys.ENTER)
                detailpageObj.enquireButton().click()
                log.info("scape melbourne central - Enquire Now")
        enquireformObj.firstName().send_keys("test")
        enquireformObj.lastName().send_keys("test")
        enquireformObj.email().send_keys(Test_Enquire_new_user.newEmail)
        enquireformObj.phoneNumber().send_keys(Test_Enquire_new_user.phone_number)
        enquireformObj.message().send_keys("this is test message :)")
        bestPlatformDropdown = Select(enquireformObj.platform())
        bestPlatformDropdown.select_by_index(10)
        enquireformObj.platformInfo().send_keys("Discord1234")
        try:
            enquireformObj.uniIDone().click()
        except Exception:
            try:
                enquireformObj.uniIDtwo().click()
            except Exception:
                try:
                    enquireformObj.uniIDthree().click()
                except:
                    try:
                        enquireformObj.uniIDfour().click()
                    except Exception:
                        try:
                            enquireformObj.uniIDfive().click()
                        except Exception:
                            log.warning(
                                "id is not available for the univerisity select field"
                            )
        enquireformObj.uniItem().click()
        nationalityDropDown = Select(enquireformObj.nationalityDrop())
        nationalityDropDown.select_by_index(3)
        enquireformObj.submitBtnEnquire().click()
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\NewUserEnquireNow.png"
        )
        currenturl = self.driver.current_url
        assert (
            currenturl == Test_Enquire_new_user.iq_hoxton_thankYou_url
            or currenturl == Test_Enquire_new_user.chapter_ealing_thankYou_url
            or currenturl == Test_Enquire_new_user.scape_melbourne_central_thankyou_url
        )
        print(currenturl)
        print(Test_Enquire_new_user.newEmail)
        log.info("new email id is " + Test_Enquire_new_user.newEmail)
        log.info("new phone number is " + Test_Enquire_new_user.phone_number)
