from selenium.webdriver.common.by import By

class Headerclass:
    
    def __init__(self,driver):
        self.driver = driver
#---------------------Header elements -------------------------------
   
    logo_selector = (By.XPATH,"//img[@alt='University Living']")
    download_app_selector = (By.XPATH,"//div[text()='Download App']")
    about_selector = (By.XPATH,"//div[text()='About']")
    blog_selector = (By.XPATH,"//div[text()='Blog']")
    careers_selector = (By.XPATH,"//div[text()='Careers']")
    refer_and_earn_selector = (By.XPATH,"//div[text()='Refer & Earn']")    
    find_my_kinda_room_selector = (By.XPATH,"//a[text()='Find My Kinda Room']")
    compare_selector = (By.XPATH,"//a[text()='Compare']")
    services_selector = (By.XPATH,"//a[text()='Services']")
    scholarship_selector = (By.XPATH,"//a[text()='Scholarship']")
    loginbtnSelector = (By.XPATH,"//span[text()='Login / SignUp']")

#------------------------------download app elements ------------------------------
    
    app_store_selector = (By.XPATH,"//img[@alt='IOS App']")
    google_play_selector = (By.XPATH,"//img[@alt='Android App']")
    qr_selector = (By.XPATH,"//img[@alt='QR code']")
    mobile_img_selector = (By.XPATH,"//img[@alt='University Living Mobile App']")
    download_app_close_btn_selector = (By.XPATH,"//button[@class='z-[2] p-1.5 absolute rounded-full border leading-none outline-none focus:outline-none transition-colors -top-2 -right-2 md:-top-3 md:-right-3 bg-white border-gray-300 hover:bg-gray-100']")
    
    
# -----------------------------header elements methods-------------------------------    
    def logo(self):
        return self.driver.find_element(*Headerclass.logo_selector)
    
    def download_app(self):
        return self.driver.find_element(*Headerclass.download_app_selector)
    
    def about(self):
        return self.driver.find_element(*Headerclass.about_selector)
    
    def blog(self):
        return self.driver.find_element(*Headerclass.blog_selector)
    
    def careers(self):
        return self.driver.find_element(*Headerclass.careers_selector)
    
    def refer_and_earn(self):
        return self.driver.find_element(*Headerclass.refer_and_earn_selector)
    
    def find_my_kinda(self):
        return self.driver.find_element(*Headerclass.find_my_kinda_room_selector)
    
    def compare(self):
        return self.driver.find_element(*Headerclass.compare_selector)
    
    def services(self):
        return self.driver.find_element(*Headerclass.services_selector)
    
    def scholarship(self):
        return self.driver.find_element(*Headerclass.scholarship_selector)
    
    def loginBtn(self):
        return self.driver.find_element(*Headerclass.loginbtnSelector)
    
#-------------------------------- download app methods ---------------------------

    def app_store(self):
        return self.driver.find_element(*Headerclass.app_store_selector)
    
    def google_play(self):
        return self.driver.find_element(*Headerclass.google_play_selector)
    
    def qr(self):
        return self.driver.find_element(*Headerclass.qr_selector)
    
    def mobile_img(self):
        return self.driver.find_element(*Headerclass.mobile_img_selector)
    
    def download_app_close_btn(self):
        return self.driver.find_element(*Headerclass.download_app_close_btn_selector)
    