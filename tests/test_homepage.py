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
from pageData.downloadAppPage import DownloadAppclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
import pytest
import requests
import requests
import json
import pyautogui

# -------------------------Homepage Test Case ------------------------------------
class Test_Homepage_class(Invokation):
    
#--------------------------- Test Data ------------------------------------------

    homepage_url = "https://www.universityliving.com/"
    colc_url = "https://www.universityliving.com/cost-of-living-calculator"
    my_kinda_url = "https://www.universityliving.com/assist/journey/start"
    services_url = "https://www.universityliving.com/services"
    scholarship_url = "https://www.universityliving.com/scholarship"
    mmt_url = "https://www.universityliving.com/services/students-flight-ticket"
    about_url = "https://www.universityliving.com/about"
    blog_url = "https://www.universityliving.com/blog/"
    careers_url = "https://www.universityliving.com/careers"
    refer_url = "https://www.universityliving.com/refer-and-earn"
    topCitiesAndBedCountApi = "https://api-prod.universityliving.com/v1/cities/popular"
    
#------------------------------Actual Test case starts -------------------------------------------
    def test_homepageValidations(self):
        
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        
        Homepage = Homepageclass(self.driver)
        DownloadApp = DownloadAppclass(self.driver)
        
        #---------------------Header Checks ---------------------------------------------------
        
        assert Homepage.headerLogo().is_displayed()
        assert Homepage.download_app().is_displayed()
        assert Homepage.flight_tickets().is_displayed()
        assert Homepage.About().is_displayed()
        assert Homepage.Blog().is_displayed()
        assert Homepage.careers().is_displayed()
        assert Homepage.referAndearn().is_displayed()
        assert Homepage.cost_of_living().is_displayed()
        assert Homepage.find_my_kinda_room().is_displayed()
        assert Homepage.services().is_displayed()
        assert Homepage.scholarship().is_displayed()
        assert Homepage.loginBtn().is_displayed()
        
        # -------------------------------- URL Redirection Checks ---------------------------------------------
        
        assert self.driver.current_url == Test_Homepage_class.homepage_url
        
        if self.driver.current_url == Test_Homepage_class.homepage_url:
            log.info("homepage url - working")
        else:
            log.critical("homepage url - broken")

        #----------------------------------- COLC url check ---------------------------------------------------
        
        Homepage.cost_of_living().click()
        
        assert self.driver.current_url == Test_Homepage_class.colc_url
        
        if self.driver.current_url == Test_Homepage_class.colc_url:
            log.info("COLC url - working")
        else:
            log.critical("COLC url - broken")
            
        Homepage.headerLogo().click()
            
        #---------------------------------- Find My Kinda url check --------------------------------------------
        
        Homepage.find_my_kinda_room().click()
        
        assert self.driver.current_url == Test_Homepage_class.my_kinda_url
        
        if self.driver.current_url == Test_Homepage_class.my_kinda_url:
            log.info("My kinda url - working")
        else:
            log.critical("My kinda url - broken")
            
        Homepage.headerLogo().click()

        #---------------------------------- Services url check ----------------------------------------------
        
        Homepage.services().click()
        
        assert self.driver.current_url == Test_Homepage_class.services_url
        
        if self.driver.current_url == Test_Homepage_class.services_url:
            log.info("services url - working")
        else:
            log.critical("services url - broken")
            
        Homepage.headerLogo().click()
            
        # --------------------------------- scholarship url check -------------------------------------
        
        Homepage.scholarship().click()
        
        assert self.driver.current_url == Test_Homepage_class.scholarship_url
        
        if self.driver.current_url == Test_Homepage_class.scholarship_url:
            log.info("scholarship url - working")
        else:
            log.critical("scholarship url - broken")
            
        Homepage.headerLogo().click()
        
        #----------------------------------------------- About url check -------------------------------------
        Homepage.About().click()
        time.sleep(2)
        
        assert self.driver.current_url == Test_Homepage_class.about_url
        
        if self.driver.current_url == Test_Homepage_class.about_url:
            log.info("about url - working")
            
        else:
            log.critical("about url - broken")
            
        Homepage.headerLogo().click()
        
        # ------------------------------------------ career url check -----------------------------------
        
        Homepage.careers().click()
        time.sleep(2)
        
        assert self.driver.current_url == Test_Homepage_class.careers_url
        
        if self.driver.current_url == Test_Homepage_class.careers_url:
            log.info("careers url - working")
        
        else:
            log.critical("careers url - broken")
        
        Homepage.headerLogo().click()
        
        # ----------------------------------------- refer and earn -------------------------------------
        
        Homepage.referAndearn().click()
        time.sleep(2)
        
        assert self.driver.current_url == Test_Homepage_class.refer_url
        
        if self.driver.current_url == Test_Homepage_class.refer_url:
            log.info("refer url - working")
        
        else:
            log.critical("refer url - broken")
        
        Homepage.headerLogo().click()
        
        #-----------------Download app pop up------------------------------------------------
        
        Homepage.download_app().click()
        
        time.sleep(3)
        
        assert DownloadApp.title().is_displayed()
        assert DownloadApp.iosButton().is_displayed()
        assert DownloadApp.playstoreButton().is_displayed()
        time.sleep(3)
        
        if (DownloadApp.iosButton().is_displayed() and DownloadApp.playstoreButton().is_displayed()):
            log.info("The download buttons are present")
        else:
            log.critical("download buttons - not available")
            
        self.driver.refresh()
        
        # -------------------------------------- Blog url check -----------------------------------------------
        
        Homepage.Blog().click()
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        assert self.driver.current_url == Test_Homepage_class.blog_url
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        Homepage.headerLogo().click()
                
        # -------------------------------------Hero section --------------------------------------------
        
        assert Homepage.heroTitle().is_displayed()
        assert Homepage.searchbar().is_displayed()
        assert Homepage.heroKinda().is_displayed()
        assert Homepage.heroKindaDesc().is_displayed()
        assert Homepage.heroTrustPilot().is_displayed()
        assert Homepage.heroVideoReview().is_displayed()
        
        if Homepage.heroTitle().is_displayed():
            log.info('Hero Banner Title - present')
        else:
            log.critical("Hero Banner Title - Not available")
            
            
            
        if Homepage.searchbar().is_displayed():
            log.info('Hero Banner search bar - present')
        else:
            log.critical("Hero Banner search bar - Not available")
            
            
        if Homepage.heroKinda().is_displayed():
            log.info('Hero Banner kinda - present')
        else:
            log.critical("Hero Banner kinda - Not available")
            
            
        if Homepage.heroKindaDesc().is_displayed():
            log.info('Hero Banner kinda desc - present')
        else:
            log.critical("Hero Banner kinda desc - Not available")
            
            
            
        if Homepage.heroTrustPilot().is_displayed():
            log.info('Hero Banner trust pilot - present')
        else:
            log.critical("Hero Banner trust pilot - Not available")
            
        
        if Homepage.heroVideoReview().is_displayed():
            log.info('Hero Banner video review - present')
        else:
            log.critical("Hero Banner video review - Not available")
            
            
        # ----------------------Top city section -------------------------
        
        assert Homepage.londonImg().is_displayed
        assert Homepage.nottinghamImg().is_displayed
        assert Homepage.leedsImg().is_displayed
        assert Homepage.melbourneImg().is_displayed
        assert Homepage.birminghamImg().is_displayed
        assert Homepage.liverpoolImg().is_displayed
        assert Homepage.torontoImg().is_displayed
        assert Homepage.newyorkImg().is_displayed
        
        lstNames = []
        TopcityOrder = ["London","Nottingham","Leeds","Melbourne","Birmingham","Liverpool","Toronto","New York"]
        BedsCountSequence = {"London":"95436 Beds","Nottingham":"35444 Beds","Leeds":"22088 Beds","Melbourne":"59946 Beds","Birmingham":"29276 Beds","Liverpool":"29342 Beds","Toronto":"16706 Beds","New York":"25044 Beds"}
        
        topcitiesResponse = requests.get(Test_Homepage_class.topCitiesAndBedCountApi)
        log.info("Top cities api response ->" + str(topcitiesResponse.status_code))
        
        dataTopCities = topcitiesResponse.json()
        formattedDataTopCities = json.dumps(dataTopCities, indent=4)
        
        for i in range(0,len(dataTopCities)):
            apiCityNames = dataTopCities[i]['name']
            apiBedCount = dataTopCities[i]['numberOfBeds']
            if apiCityNames == TopcityOrder[i]:
                log.info(apiCityNames + ' pass' + " beds ->" + apiBedCount)
                print(apiCityNames + ' pass' + " beds ->" + apiBedCount)
            else:
                print(apiCityNames + ' fail' + " beds ->" + apiBedCount)
                
# -------------------------------Let us find your perfect home ---------

        assert Homepage.descOne().is_displayed()
        assert Homepage.descTwo().is_displayed()
        assert Homepage.descThree().is_displayed()
        assert Homepage.TandCperfecthome().is_displayed()
        
# -------------------------- Popular properties ----------------------

        assert Homepage.popUK().is_displayed()
        assert Homepage.popAUS().is_displayed()
        assert Homepage.popIRE().is_displayed()
        assert Homepage.popCAN().is_displayed()
        assert Homepage.popUS().is_displayed()
            
        
        
        

                
            




                
        
                
        
            
        
                 
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
