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


class Test_Enquire_exisitng_user(Invokation):
    iq_hoxton_thankYou_url = 'https://www.universityliving.com/united-kingdom/london/iq-hoxton/enquire-now/thank-you'
    chapter_ealing_thankYou_url = 'https://www.universityliving.com/united-kingdom/london/chapter-ealing/enquire-now/thank-you'
    scape_melbourne_central_thankyou_url = 'https://www.universityliving.com/australia/melbourne/scape-melbourne-central/enquire-now/thank-you'

    @mark.testomatio('@Tb184fb29')
    def test_enquire_form_existing_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        enquireformObj = FormClass(self.driver)
        homepageObj.searchbar().send_keys('iq hoxton')
        time.sleep(2)
        homepageObj.searchbar().send_keys(Keys.RETURN)
        try:
            detailpageObj.enquireButton().click()
            log.info('IQ hoxton - Enquire Now')
        except Exception:
            homepageObj.headerSearch().send_keys('chapter ealing')
            time.sleep(2)
            homepageObj.headerSearch().send_keys(Keys.ENTER)
            try:
                detailpageObj.enquireButton().click()
                log.info('chapter ealing - Enquire now')
            except Exception:
                homepageObj.headerSearch().send_keys('scape melbourne central')
                time.sleep(2)
                homepageObj.headerSearch().send_keys(Keys.ENTER)
                detailpageObj.enquireButton().click()
                log.info('scape melbourne central - Enquire Now')
        enquireformObj.firstName().clear()
        enquireformObj.firstName().send_keys('test')
        enquireformObj.lastName().clear()
        enquireformObj.lastName().send_keys('test')
        enquireformObj.email().clear()
        enquireformObj.email().send_keys('ha.sachan@universityliving.com')
        for i in range(10):
            enquireformObj.phoneNumber().send_keys(Keys.BACKSPACE)
        enquireformObj.phoneNumber().send_keys('8505813979')
        enquireformObj.message().clear()
        enquireformObj.message().send_keys('this is test message :)')
        visastatusDropdown = Select(enquireformObj.visaStatus())
        visastatusDropdown.select_by_index(3)
        bestPlatformDropdown = Select(enquireformObj.platform())
        bestPlatformDropdown.select_by_index(10)
        enquireformObj.platformInfo().send_keys('Discord-ID')
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
                                'id is not available for the univerisity select field')
        enquireformObj.uniItem().click()
        enquireformObj.submitBtnEnquire().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            'C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\enquireNow.png')
        currenturl = self.driver.current_url
        if currenturl == Test_Enquire_exisitng_user.iq_hoxton_thankYou_url or currenturl == Test_Enquire_exisitng_user.chapter_ealing_thankYou_url or currenturl == Test_Enquire_exisitng_user.scape_melbourne_central_thankyou_url:
            log.info('Thankyou URL is working Fine')
        else:
            log.warning('Thankyou URL is not working PlZ check')
        homepageObj.headerLogo().click()
