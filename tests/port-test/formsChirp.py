import pytest
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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
import logging
import inspect

N = 10
s = Service("C:/Users/TUL/Desktop/cd/cd19.exe")
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8093")
driver = webdriver.Chrome(service=s, options=opt)
driver.implicitly_wait(15)

count = 0


def enqForm():
    i = "".join([str(random.randint(0, 9)) for i in range(2)])
    print(i)
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    print(new_phoneNumber)
    new_email = "c" + i + "@sharklasers.com"
    print(new_email)
    driver.find_element(By.XPATH, "//div[text()='Enquire']").click()
    for i in range(31):
        driver.find_element(By.ID, "email").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.ID, "email").send_keys(new_email)
    for i in range(10):
        driver.find_element(By.ID, "contactNumber").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.ID, "contactNumber").send_keys(new_phoneNumber)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(3)
    driver.back()


enqForm()
