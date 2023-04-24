import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.common.exceptions import NoSuchElementException
import pytest
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
import pytest


@pytest.mark.skip()
# @pytest.mark.usefixtures("setup")  # test in conftest
class Test_NVclass(Invokation):        # test class
    def test_NV(self):            # complete test will be written here
        
        log = self.getLogger()
        
        self.driver.get("https://www.universityliving.com/united-kingdom/london/property/mannequin-house")
        self.driver.implicitly_wait(10)
        url_bar = self.driver.find_element(By.XPATH,"//div[@class='toolbar']/input[@type='text']")
        actions = ActionChains(self.driver)
        actions.move_to_element(url_bar).perform()
        
        time.sleep(10)
        