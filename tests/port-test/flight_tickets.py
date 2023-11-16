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


s = Service("C:/Users/TUL/Desktop/cd/cd18.exe")
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8093")
driver = webdriver.Chrome(service=s, options=opt)
# driver.get("https://universityliving.com")
driver.implicitly_wait(15)


# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--disable-notifications")
# chrome_options.add_experimental_option("debuggerAddress", "localhost:8093")
# driver = webdriver.Chrome(options=chrome_options)

# driver.find_element(By.XPATH, "//div[text()='Flight Tickets']").click()
# driver.find_element(By.XPATH, "//div[text()='Submit']").click()
# driver.back()


def mmtSelection():
    driver.find_element(
        By.XPATH,
        "//div[@class='relative hover:bg-[#f5e9ffbf] border sm:rounded-r-xl sm:rounded-bl-none rounded-b-xl p-3 text-theme-black-text animate-none']",
    ).click()
    driver.find_element(By.XPATH, "//p[text()='Dublin']").click()
    driver.find_element(
        By.XPATH, "//div[@class='border-l-2 p-3 hover:bg-[#f5e9ffbf] ']"
    ).click()
    driver.find_element(
        By.XPATH, "//div[@aria-label='Move forward to switch to the next month.']"
    ).click()
    driver.find_element(By.XPATH, "(//td[text()='30'])[2]").click()
    driver.find_element(By.XPATH, "//div[text()='Search Flights']").click()


def form_all_same():
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    driver.find_element(By.ID, "contactNo").click()
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_email_change_no_change():
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + "@yopmail.com"
    print("updated email 1 -->", new_email)
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(new_email)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_phoneNumber_change_no_change():
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    print("updated phone number 1 -->", new_phoneNumber)
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    driver.find_element(By.ID, "contactNo").click()
    for i in range(10):
        driver.find_element(By.ID, "contactNo").send_keys(Keys.BACK_SPACE)

    driver.find_element(By.ID, "contactNo").send_keys(new_phoneNumber)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_lastName_change_no_change():
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("testchange")
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_firstName_change_no_change():
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "firstName").send_keys("testchange")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_last_and_email_change_no_change():
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + "@yopmail.com"
    print("updated email 2 -->", new_email)
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("testchangeagain")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(new_email)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_last_and_number_change_no_change():
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    print("updated number 2 -->", new_phoneNumber)
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("testchange")
    driver.find_element(By.ID, "contactNo").click()
    for i in range(10):
        driver.find_element(By.ID, "contactNo").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.ID, "contactNo").send_keys(new_phoneNumber)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_first_and_last_change_no_change():
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "firstName").send_keys("testTestingtest")
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("testtestTesting")
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_first_and_number_no_change():
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "firstName").send_keys("testTestingtestTesting")
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    print("updated phone number 1 -->", new_phoneNumber)
    driver.find_element(By.ID, "contactNo").click()
    for i in range(10):
        driver.find_element(By.ID, "contactNo").send_keys(Keys.BACK_SPACE)

    driver.find_element(By.ID, "contactNo").send_keys(new_phoneNumber)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


def form_first_and_email_change_no_change():
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + "@yopmail.com"
    print("updated email 3 -->", new_email)
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "firstName").send_keys("test testing")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(new_email)
    driver.find_element(By.XPATH, "//div[text()='Submit']").click()
    time.sleep(5)
    driver.back()


mmtSelection()
form_all_same()
mmtSelection()
form_all_same()
mmtSelection()
form_email_change_no_change()
mmtSelection()
form_phoneNumber_change_no_change()
mmtSelection()
form_lastName_change_no_change()
mmtSelection()
form_firstName_change_no_change()
mmtSelection()
form_last_and_email_change_no_change()
mmtSelection()
form_last_and_number_change_no_change()
mmtSelection()
form_first_and_last_change_no_change()
mmtSelection()
form_firstName_change_no_change()
mmtSelection()
form_first_and_number_no_change()
mmtSelection()
form_first_and_email_change_no_change()
