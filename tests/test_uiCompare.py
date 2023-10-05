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
from PIL import Image, ImageChops, ImageStat


@pytest.mark.skip()
class Test_homeUI_check(Invokation):
    bookNow_url = 'https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you'

    @mark.testomatio('@T347886fd')
    def test_homeUI_check_cache(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        formObj = FormClass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        element = self.driver.find_element(By.XPATH, '//body')
        screenshot1 = element.screenshot_as_png
        screenshot1_file = 'ss1.png'
        with open(screenshot1_file, 'wb') as file:
            file.write(screenshot1)
        ref_file = 'ss2.png'
        ref_image = Image.open(ref_file)
        screenshot_image = Image.open(screenshot1_file)
        diff = ImageChops.difference(ref_image, screenshot_image)
        diff.show()
        stat = ImageStat.Stat(diff)
        rms = stat.rms[0]
        threshold = 10
        if rms < threshold:
            log.info('images are similar')
        else:
            log.warning('images are different')
