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

N = 10


s = Service("C:/Users/TUL/Desktop/cd/cd19.exe")
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=s, options=opt)


driver.implicitly_wait(15)


def friendForm():
    # driver.find_element(
    #     By.XPATH, "//input[@data_automation_id='F0_FullName']"
    # ).send_keys("test test")
    # new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    # driver.find_element(
    #     By.XPATH, "//input[@data_automation_id='F0_PhoneNumber']"
    # ).send_keys(new_phoneNumber)
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + "@yopmail.com"
    # driver.find_element(By.XPATH, "//input[@data_automation_id='F0_Email']").send_keys(
    #     new_email
    # )
    # driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//div[text()='Done']").click()
    # time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys(new_email)
    driver.find_element(By.XPATH, "//div[text()='Send Email']").click()
    driver.find_element(By.XPATH, "//div[text()='OK']").click()


count = 0
while count < 35:
    friendForm()
    count = count + 1
