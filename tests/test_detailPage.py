import time
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.listingPage import listingClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
import random
import string


class Test_Detail_page_class(Invokation):
    
    def test_detail_page_validations(self):
        
        log = self.getLogger()
        
        Homepage = Homepageclass(self.driver)
        Listingpage = listingClass(self.driver)
        Detailpage = detailpageClass(self.driver)
        formObj = FormClass(self.driver)
        
        self.driver.implicitly_wait(5)
        
        propertyName = "madrid getafe"
        Homepage.searchbar().send_keys(propertyName)
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
                log.info("Price is present-->" + a)
            else:
                log.warning("price is missing")
        except Exception:
            log.warning("Price is not available")
            
            
            
#----------------------------------Room Type Click-------------------------------------------------


#------------------------ All Room Type------------------------------
        try:
            if Detailpage.allRoomTypeBtn().is_displayed():
                log.info("All catagory is present")
                Detailpage.allRoomTypeBtn().click()
            else:
                log.warning("All category is not available plz check")
        except Exception:
            log.warning("All category is not interactable plz check")

#---------------------------Studio Room Type ---------------------------

        try:
            if Detailpage.studioRoomTypeBtn().is_displayed():
                log.info("Studio catagory is present")
                Detailpage.studioRoomTypeBtn().click()
            else:
                log.warning("Studio category is not available plz check")
        except Exception:
            log.warning("Studio category is not interactable plz check")

# ---------------------------- Apartments Room Type --------------------------
            
        try:
            if Detailpage.apartmentRoomTypeBtn().is_displayed():
                log.info("Apartments catagory is present")
                Detailpage.apartmentRoomTypeBtn().click()
            else:
                log.warning("Apartments category is not available plz check")
        except Exception:
            log.warning("Apartments category is not interactable plz check")
            
#-----------------------------------Ensuite Room Type ---------------------------
        
        try:
            if Detailpage.ensuiteRoomTypeBtn().is_displayed():
                log.info("Ensuite catagory is present")
                Detailpage.ensuiteRoomTypeBtn().click()
            else:
                log.warning("Ensuite category is not available plz check")
        except Exception:
            log.warning("Ensuite category is not interactable plz check")
            
        time.sleep(3)
            
#------------------------------------- Others -------------------------------------
            
        try:
            if Detailpage.othersRoomTypeBtn().is_displayed():
                log.info("All catagory is present")
                Detailpage.othersRoomTypeBtn().click()
            else:
                log.warning("Other category is not available plz check")
        except Exception:
            log.warning("Other category is not interactable plz check")    
            
# ------------------------------------ similar properties validations --------------------------

        try:
            if Detailpage.viewAllPropertiesBtn().is_displayed():
                log.info("More than 3 properties are available in the similar cities section")
                Detailpage.viewAllPropertiesBtn().click()
                a = Detailpage.similarPropertyNames()
                for ele in a:
                    prop_name = ele.text
                    log.info(prop_name)
                
                
        except Exception:
            log.warning("multiple exceptions occured in similar properties module plz check")
            
# --------------------------------------- Total Rooms in property ----------------------------------
        Detailpage.roomtypeLink().click()
        time.sleep(3)
        Detailpage.allRoomTypeBtn().click()
        time.sleep(3)
        try:
            rooms = Detailpage.roomNames()
            print(type(rooms))
            for roomNames in rooms:
                names = roomNames.text
                log.info(names)
        except Exception:
            log.warning("Error in similar property module -- plz check")
            
# -------------------------------------- No visa no pay & no uni no pay -------------------------------

        try:
            if Detailpage.noVisaNoPay().is_displayed() and Detailpage.noUniNoPay().is_displayed():
                log.info("property contains no visa no pay module")
            else:
                log.warning("property does not have no vis no pay module")            
                
        except Exception:
            log.warning("property does not have no vis no pay module")
        
# ----------------------------------------- select university ----------------------------------------

        try:
            formObj.uniIDone().click()
        except Exception:
            try:
                formObj.uniIDtwo().click()
            except Exception:
                try:
                    formObj.uniIDthree().click()
                except:
                    try:
                        formObj.uniIDfour().click()
                    except Exception:
                        try:
                            formObj.uniIDfive().click()
                        except Exception:
                            log.warning("ID is not interactable")
                            
        universities_in_select_university = Detailpage.universityCount()
        log.info("total university -->" + str(len(universities_in_select_university)))
        
# -------------------------------------------Book Now count -------------------------------

        try:
            if Detailpage.booknowButton().is_displayed():
                bookNowCount = Detailpage.BookNowCount()
                log.info("total book now count " + str(len(bookNowCount)))
            else:
                log.warning("No Book Now property is Available")
            
        except Exception:
            log.warning("No Book Now property is Available")
            
#------------------------------------------- join waitlist --------------------------


        try:
            if Detailpage.joinwaitlistBtn().is_displayed():
                bookNowCount = Detailpage.joinWaitlistCount()
                log.info("total Join waitlist count " + str(len(bookNowCount)))
            else:
                log.warning("No Join waitlist room is Available")
            
        except Exception:
            log.warning("No Join waitlist room is Available")