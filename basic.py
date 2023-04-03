import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty()) 
from pyfiglet import figlet_format
from selenium.common.exceptions import NoSuchElementException



ascii_art = pyfiglet.figlet_format("START", font="starwars")
print(ascii_art)
s = Service("C:/Users/TUL/Desktop/cd/cd3.exe")

driver = webdriver.Chrome(service=s)
driver.get('https://www.universityliving.com/')
wait = 1
driver.maximize_window()
driver.implicitly_wait(4)

loginEmail = 'harsh.sachan@universityliving.com'
    
driver.find_element(By.XPATH,"//span[text()='Login / SignUp']").click()
driver.find_element(By.ID,"email").send_keys(loginEmail)
driver.find_element(By.XPATH,"//div[text()='Login']").click()
driver.find_element(By.NAME,"otp0").send_keys("1")
driver.find_element(By.NAME,"otp1").send_keys("2")
driver.find_element(By.NAME,"otp2").send_keys("3")
driver.find_element(By.NAME,"otp3").send_keys("4")
driver.find_element(By.NAME,"otp4").send_keys("5")
driver.find_element(By.XPATH,"//div[text()='Continue']").click()
driver.find_element(By.XPATH,"(//a[@href='/dashboard?tab=booking'])").click()
    
emailDashboard = driver.find_element(By.XPATH,"(//p[text()='harsh.sachan@universityliving.com'])").text
driver.find_element(By.XPATH,"(//img[@alt='Profile'])").click()
emailProfile = driver.find_element(By.XPATH,"(//p[text()='harsh.sachan@universityliving.com'])[2]").text 
    
if (loginEmail == emailDashboard and loginEmail == emailProfile):
    print("Loggin successful")
else:
    print("there is an error in loggin")

print("Login email is -->", loginEmail)
print("Dashboard email is -->", emailDashboard)
print("profile email is -->", emailProfile)