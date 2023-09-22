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
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.roomReplacement import roomreplacementclass
from pageData.services import Servicesclass
import pytest
import string
import random
N = 7


class Test_join_Waitlist_new_user(Invokation):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = ''.join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res + '@yopmail.com'

    @mark.testomatio('@T0c934481')
    def test_join_Waitlist_new_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        thankyouURL = 'https://www.universityliving.com/australia/melbourne/scape-berkeley-2/wait-list/thank-you'
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        joinwaitlistObj = FormClass(self.driver)
        homepageObj.searchbar().send_keys('Scape Berkeley 2')
        time.sleep(2)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        detailpageObj.viewMoreRoomBtn().click()
        self.driver.execute_script('window.scrollTo(0, 500)')
        detailpageObj.joinwaitlistLastBtn().click()
        joinwaitlistObj.firstName().send_keys('test')
        joinwaitlistObj.lastName().send_keys('test')
        joinwaitlistObj.email().send_keys('pravin.garg@universityliving.com')
        joinwaitlistObj.phoneNumber().send_keys('8871555179')
        joinwaitlistObj.message().send_keys('this is test message :)')
        visastatusDropdown = Select(joinwaitlistObj.visaStatus())
        visastatusDropdown.select_by_index(3)
        bestPlatformDropdown = Select(joinwaitlistObj.platform())
        bestPlatformDropdown.select_by_index(10)
        joinwaitlistObj.platformInfo().send_keys('Dis-test-12')
        try:
            joinwaitlistObj.uniIDone().click()
        except Exception:
            try:
                joinwaitlistObj.uniIDtwo().click()
            except Exception:
                try:
                    joinwaitlistObj.uniIDthree().click()
                except:
                    try:
                        joinwaitlistObj.uniIDfour().click()
                    except Exception:
                        try:
                            joinwaitlistObj.uniIDfive().click()
                        except Exception:
                            log.info('University ID is different again')
        joinwaitlistObj.uniItem().click()
        joinwaitlistObj.submitBtnEnquire().click()
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            'C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\NewUserJoinwaitlist.png')
        currenturl = self.driver.current_url
        assert thankyouURL == currenturl
        log.info('new email id is ' + Test_join_Waitlist_new_user.newEmail)
        log.info('new phone number is' +
                 Test_join_Waitlist_new_user.phone_number)
