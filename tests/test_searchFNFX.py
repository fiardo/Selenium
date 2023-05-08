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

@pytest.mark.skip()  # test in conftest
class Test_SearchFunc(Invokation):        # test class 
    
    def test_seachbarFnFx(self):            # complete test will be written here
        
        log = self.getLogger()
        self.driver.implicitly_wait(10)
    
        homepage = Homepageclass(self.driver)
        
        keyword_list = ["London", "Birmingham","Manchester","Nottingham","Glasgow","Cardiff","King's College London (KCL)","Queen Mary University of London (QMUL)","University of Manchester","Birmingham City University (BCU)","Nottingham Trent University (NTU)","University of Glassgow"]
        item_len = len(keyword_list)
        
        for i in keyword_list:
            homepage.searchbar().send_keys(i)
            time.sleep(3)
            first_element_in_search = self.driver.find_element(By.XPATH,"((//div[@class='content-font'])/div)[1]").text
            if i == first_element_in_search:
                log.info("data matched--->" + i)
            homepage.headerLogo().click()           
        
        log.info("length -->" + item_len)       
        
        
 