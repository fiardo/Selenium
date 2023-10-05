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


s = Service("C:/Users/TUL/Desktop/cd/cd16.exe")
chrome_options = Options()
# chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://www.universityliving.com/")

time.sleep(10)
