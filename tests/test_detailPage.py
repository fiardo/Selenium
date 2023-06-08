import time
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.listingPage import listingClass
from pageData.detailPage import detailpageClass
import random
import string

class Test_Detail_page_class(Invokation):
    
    def test_detail_page_validations(self):
        
        log = self.getLogger()
        
        Homepage = Homepageclass(self.driver)
        Listingpage = listingClass(self.driver)
        Detailpage = detailpageClass(self.driver)
        
        self.driver.implicitly_wait(5)
        
        Homepage.searchbar().send_keys("chapter ealing")
        time.sleep(2)
        Homepage.searchbar().send_keys(Keys.ENTER)
        
#---------------------------------------validating the overview link --------------------------------------

        try:
            if Detailpage.overveiwLink().is_displayed():
                log.info("Overview link is present")
            else:
                log.warning("overview is not present")
        except Exception:
            log.warning("overview link is not present")

#------------------------------------------ Room type link  ----------------------------------------            
        
        try:
            if Detailpage.roomtypeLink().is_displayed():
                log.info("Room type link in present")
            else:
                log.warning("Room link is not present")
                
        except Exception:
            log.warning("Room Type link is not present")

#-------------------------------------Payment Info link validations ------------------------------------------            
        try:
            if Detailpage.paymentInfoLink().is_displayed():
                log.info("Payment info link in present")
            else:
                log.warning("Payment info link is not present")
                
        except Exception:
            log.warning("Payment info link is not present")   
        
#------------------------------------------Reviews link validations ----------------------------------------

        try:
            if Detailpage.reviewsLink().is_displayed():
                log.info("Review link in present")
            else:
                log.warning("Review is not present")
                
        except Exception:
            log.warning("Review link is not present")

#------------------------------------------- similar properties ----------------------------------------

        try:
            if Detailpage.similarPropertyLink().is_displayed():
                log.info("Similar Properties link in present")
            else:
                log.warning("similar Properties link is not present")
                
        except Exception:
            log.warning("Similar Properties link is not present")
            
#------------------------------------ Property price check  --------------------------------------        

        try:
            a = Detailpage.fromPrice().text
            if Detailpage.fromPrice().is_displayed():
                log.info("Price -->" + a)
            else:
                log.warning("price is missing")
        except Exception:
            log.warning("Price is not available")
            
            
            
#----------------------------------logs seperator-------------------------------------------------


        log.info("--------------------------------------------------------------------------------------------------")

        
        
        