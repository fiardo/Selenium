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
opt.add_experimental_option("debuggerAddress", "localhost:8093")
driver = webdriver.Chrome(service=s, options=opt)
driver.implicitly_wait(15)


driver.find_element(By.ID, "contactNumber").send_keys("888888888888888")
driver.find_element(By.XPATH, "//div[text()='Submit']").click()
# driver.find_element(By.XPATH, "//div[@class='flag in']").click()
# lst = []
# codeLIst = driver.find_elements(By.XPATH, "//span[@class='country-name']")
# for item in codeLIst:
#     lst.append(item.text)


# print(lst)
# print(len(codeLIst))
# driver.find_element(By.XPATH, "//div[@class='flag in']").click()

# k = 0
# while k == 235:
# driver.find_element(By.XPATH, "//div[@class='flag in']").click()
# time.sleep(5)
# lstTwo = driver.find_elements(By.XPATH, "//span[@class='country-name']")
# lstTwo[k].click()
# k = k + 1
# driver.find_element(By.XPATH, "//div[@class='flag in']").click()
# lstTwo = driver.find_elements(By.XPATH, "//span[@class='country-name']")
# driver.find_element(By.XPATH, "//div[@class='flag in']").click()

# for item in range(0, len(lstTwo)):
#     driver.find_element(By.XPATH, "//div[@class='flag in']").click()
#     lst = driver.find_elements(By.XPATH, "//span[@class='country-name']")
#     time.sleep(2)
#     lst[item].click()

driver.find_element(By.XPATH, "//div[@class='flag-dropdown ']").click()
lst = driver.find_elements(By.XPATH, "//span[@class='country-name']")
names = []
for item in lst:
    names.append(item.text)
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='arrow up']").click()


for i in range(0, len(lst)):
    driver.find_element(By.XPATH, "//div[@class='flag-dropdown ']").click()
    ltwo = driver.find_elements(By.XPATH, "//span[@class='country-name']")
    time.sleep(1)
    if ltwo[i].text != "Caribbean Netherlandsq":
        ltwo[i].click()
    else:
        continue

    print(
        names[i]
        + " error --> "
        + driver.find_element(By.XPATH, "(//p[@class='text-xs text-red-400'])[4]").text
    )
