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
from pageData.studentFinancing import StudentFinancingClass
import pytest
import string
import random
from pageData.servicelisting import Servicelistingclass

class Test_servicelistingpage(Invokation):
    
    def test_servicelistingpage(self):
        log = self.getLogger()
        homepageObject = Homepageclass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        servicepage = Servicelistingclass(self.driver)
        loginEmail = "harsh.sachan@universityliving.com"
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        homepageObject.services().click()

        serviceNamesList = []
        
        serviceNameElement = servicepage.Servicenames()
        for items in serviceNameElement:
            serviceNamesList.append(items.text)
        print(serviceNamesList)

        servicedetailList = []
        
        servicedetailElement = servicepage.Servicedetails()
        for items in servicedetailElement:
            servicedetailList.append(items.text)
        print(servicedetailList)   



        ServiceNames =  ['Accommodation', 'Student Flight Tickets', 'Guarantor', 'International Money Transfer', 'Student Bank Account', 'Get Visa', 'Student Financing', 'Room Essentials', 'Airport Pickup', 'Room Replacement', 'International SIM', 'Travel Insurance', 'Health Insurance - OSHC', 'Luggage Storage', 'Forex', 'Job Search', 'Student Internships', 'Free Online Courses']
        Servicedetails = ['Find the perfect home, close to university and close to life', 'Jet off to your dream destination in style with special student fares', 'Verified guarantors for the ultimate safety net', 'Transfer funds for tuition & accommodation with utter ease', 'Local bank account for seamless payments & transactions', 'Seamless end-to-end Visa Solutions for your study abroad journey', 'No need to hold back on your dream of education abroad', 'Pack Light! Explore a range of room essentials for an effortless move-in', 'Book a safe & comfy ride to and from the airport', 'One-of-a-kind solution to help you find a next perfect room', 'Stay connected anywhere, anytime across 180+ countries', "Emergencies don't come knocking, better to be safe than sorry", 'In sickness and in health, we’ve got you covered', 'Safe & Secure extra storage space at convenient locations', 'Purchase, sell, and transfer international currency from anywhere', 'Explore from over 10m jobs across different industry verticals', 'Kickstart your career with real-world industry experience', 'Unlock your potential and take your skills to next level with these courses']

        if (serviceNamesList == ServiceNames and servicedetailList == Servicedetails):
            log.info(" Order of the listed services Names and Description in service listing page is matched ")
        else:
            log.critical( " Order of the listed services Names and Description in service listing page is Not matched")


