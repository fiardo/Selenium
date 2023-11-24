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

# driver.find_element(By.ID, "BookingAvailabilityForm_Residence").click()
# propertyDropDown = Select(
#     driver.find_element(By.ID, "BookingAvailabilityForm_Residence")
# )
# propertyDropDown.select_by_index(1)

# driver.find_element(By.ID, "BookingAvailabilityForm_BookingPeriod").click()
# dateDropDown = Select(
#     driver.find_element(By.ID, "BookingAvailabilityForm_BookingPeriod")
# )
# dateDropDown.select_by_index(1)
# driver.find_element(By.ID, "BookingAvailabilityForm_BookingPeriod").click()
driver.find_element(By.XPATH, "(//span[text()='Apply'])[1]").click()
floorPlanKey = driver.find_element(By.XPATH, "//td[text()='Floor plan:']").text
floorPlanValue = driver.find_element(
    By.XPATH, "(//td[@class='building-contect-value'])[2]"
).text
bedBathKey = driver.find_element(By.XPATH, "//td[text()='Bed/Bath:']").text
bedBathValue = driver.find_element(
    By.XPATH, "(//td[@class='building-contect-value'])[3]"
).text
leaseTermKey = driver.find_element(By.XPATH, "//td[text()='Lease Term:']").text
leaseTermnValue = driver.find_element(
    By.XPATH, "(//td[@class='building-contect-value'])[4]"
).text

print(floorPlanKey + "-->" + floorPlanValue)
print(bedBathKey + "-->" + bedBathValue)
print(leaseTermKey + "-->" + leaseTermnValue)


driver.find_element(By.ID, "applicant_first_name").send_keys("test")
driver.find_element(By.ID, "applicant_last_name").send_keys("test")
driver.find_element(By.NAME, "masked-phone_numbers[0][phone_number]-country").clear()
driver.find_element(By.NAME, "masked-phone_numbers[0][phone_number]-country").send_keys(
    "+44"
)
driver.find_element(By.ID, "phone_numbers[0][phone_number]-base").send_keys(
    "8505813979"
)
driver.find_element(By.ID, "applicant_username").send_keys("test@yopmail.com")
driver.find_element(By.ID, "applicant_password").send_keys("test@12345")
driver.find_element(By.ID, "applicant_password_confirm").send_keys("test@12345")
driver.find_element(By.ID, "agrees_to_terms").click()
driver.find_element(By.ID, "create-app-btn").click()
driver.find_element(By.XPATH, "//a[text()='I agree to the terms']").click()
