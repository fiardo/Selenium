import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as e
from pageData.header import Headerclass
import string
import random
import pytest

from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass


@pytest.mark.skip()
class Test_headerTest(Invokation):
    
    def test_header_e2e(self):
        log = self.getLogger()
        self.driver.implicityly_wait(5)
        headobj = Headerclass(self.driver)
        
# ----------------------checking the download app fn/fx -------------------
        
        headobj.download_app().click()
        
        
        
        
        
        