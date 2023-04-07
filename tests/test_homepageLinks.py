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

@pytest.mark.skip()
class Test_BookNowForms(Invokation):
    
    bookNow_url = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/book-now/thank-you"
    
    def test_bookNowForm(self):
        
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        links = self.driver.find_elements(By.TAG_NAME,"a")
        for link in links:
            href = link.get_attribute("href")
            # log.info(href)
        