import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.contactusPage import contactusClass
import pytest
import string
import random
from bs4 import BeautifulSoup


s = Service("C:/Users/TUL/Desktop/cd/cd14.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.universityliving.com/')

driver.implicitly_wait(10)

page_source = driver.page_source
print(page_source)

with open('your_output_file.txt',"w",encoding='utf-8') as file:
    file.write(page_source)