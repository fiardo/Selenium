from selenium.webdriver.common.by import By

class Homepageclass:
    
    def __init__(self,driver):
        self.driver = driver
        
    searchbarSelector = (By.XPATH,"//input[@placeholder='Search by City, University or Property']")
    loginbtnSelector = (By.XPATH,"//span[text()='Login / SignUp']")
    homepageImgSelector = (By.XPATH,"//img[@alt='University Living']")
    headerServicesSelector = (By.XPATH,"//a[text()='Services']")
    roomreplacementSelector = (By.XPATH,"//a[@href = '/services/room-replacement']")
    servicesSelector = (By.XPATH,"//a[text()='Services']")
    contactusSelector = (By.XPATH,"//a[text()='Contact Us']")
    headerSearchSelector = (By.XPATH,"//input[@placeholder='Search by City, University or Property']")
    chatIcon_Selector = (By.XPATH,"//img[@alt='Chat Icon']")
    search_results_selector = (By.XPATH,"//div[@id='async-pagination-example']/div/a/div/div[1]")
    downloadApp_link_selector = (By.XPATH,"//div[text()='Download App']")
    flightTickets_link_selector = (By.XPATH,"//div[text()='Flight Tickets']")
    about_link_selector = (By.XPATH,"//div[text()='About']")
    blog_link_selector = (By.XPATH,"//div[text()='Blog']")
    careers_link_selector = (By.XPATH,"//div[text()='Careers']")
    referAndearn_link_selector = (By.XPATH,"//div[text()='Refer & Earn']")
    costOfliving_link_selector = (By.XPATH,"//a[text()='Cost of Living']")
    findMyKindaRoom_link_selector = (By.XPATH,"//a[text()='Find My Kinda Room']")
    services_link_selector = (By.XPATH,"//a[text()='Services']")
    scholarship_link_selector = (By.XPATH,"//a[text()='Scholarship']")
    hero_title_selector = (By.XPATH,"//p[text()='Safe home for every student']")
    hero_kinda_selector = (By.XPATH,"//p[text()='Find My Kinda Room']")
    hero_trust_pilot_selector = (By.XPATH,"(//img[@alt='Trustpilot'])[1]")
    hero_video_reviews_selector = (By.XPATH,"//button[text()='Video Reviews']")
    hero_kinda_desc_selector = (By.XPATH,"//p[text()='Curated recommendations from experts']")
    bedsCount_selector = (By.XPATH,"//p[text()='1.75 Mn+']")
    bedsText_selector = (By.XPATH,"//p[text()='Beds']")
    propertiesCount_selector = (By.XPATH,"//p[text()='35K+']")
    propertiesText_selector = (By.XPATH,"//p[text()='Properties']")
    studentAssistedCount_selector = (By.XPATH,"//p[text()='2 Mn']")
    studentAssistedText_selector = (By.XPATH,"//p[text()='students Assited']")
    globalCitiesCount_selector = (By.XPATH,"//p[text()='300+']")
    globalCitiestext_selector = (By.XPATH,"//p[text()='Global Cities']")
    
    #---------------------------Top citites selector -----------------------------------------------
    
    londonImage_selector = (By.XPATH,"//img[@alt='London']")
    nottinghamImage_selector = (By.XPATH,"//img[@alt='Nottingham']")
    leedsImage_selector = (By.XPATH,"//img[@alt='Leeds']")
    melbourneImage_selector = (By.XPATH,"//img[@alt='Melbourne']")
    birminghamImage_selector = (By.XPATH,"//img[@alt='Birmingham']")
    liverpoolImage_selector = (By.XPATH,"//img[@alt='Liverpool']")
    torontoImage_selector = (By.XPATH,"//img[@alt='Toronto']")
    newyorkImage_selector = (By.XPATH,"//img[@alt='New York']")
    
    # ----------------------- Top cities names -----------------------------
    
    cityNames_selector = (By.XPATH,"/html/body/div[1]/main/section[3]/div[2]/a/div/div/div/span[1]")
    
    bedsCount_selector = (By.XPATH,"/html/body/div[1]/main/section[3]/div[2]/a/div/div/div/span[2]")
    
    # -------------------------- perfect home section ------------------------------
    
    Title_selector = (By.XPATH,"//div[text()='Let us find your perfect home!']")
    descOne_selector = (By.XPATH,"//p[text()='Search - Compare - Relax']")
    descTwo_selector = (By.XPATH,"//p[text()='Easy Peasy']")
    descThree_selector = (By.XPATH,"//p[text()='Price Match Guarantee']")
    termsAndConditions_selector = (By.XPATH,"//a[text()='Terms & Conditions']")
    
    # ---------------------------popular Properties ---------------------------
    vertCityNames_selector = (By.XPATH,"//ul[@class='p-4 space-y-11']/li")
    uk_selector = (By.ID,"united-kingdom")
    australia_selector = (By.ID,"australia")
    ireland_selector = (By.ID,"ireland")
    canada_selector = (By.ID,"canada")
    us_selector = (By.ID,"united-states")
    popPropertiesNames_selector = (By.XPATH,"//div[@class='w-[85vw] md:w-[45vw] flex-shrink-0 lg:w-full flex flex-col text-theme-black-text']/a/p[1]")
    popPropertiesPrice_selector = (By.XPATH,"//div[@class='w-[85vw] md:w-[45vw] flex-shrink-0 lg:w-full flex flex-col text-theme-black-text']/a/p[2]")
    
    
    
    
    #------------------------------Methods ------------------------------
    def searchbar(self):
        return self.driver.find_element(*Homepageclass.searchbarSelector)
    
    def loginBtn(self):
        return self.driver.find_element(*Homepageclass.loginbtnSelector)
    
    def headerLogo(self):
        return self.driver.find_element(*Homepageclass.homepageImgSelector)
    
    def headerServices(self):
        return self.driver.find_element(*Homepageclass.headerServicesSelector)
    
    def roomReplacement(self):
        return self.driver.find_element(*Homepageclass.roomreplacementSelector)
    
    def services(self):
        return self.driver.find_element(*Homepageclass.servicesSelector)
    
    def contactus(self):
        return self.driver.find_element(*Homepageclass.contactusSelector)
    
    def headerSearch(self):
        return self.driver.find_element(*Homepageclass.headerSearchSelector)
    
    def chatIcon(self):
        return self.driver.find_element(*Homepageclass.chatIcon_Selector)
    
    def search_results(self):
        return self.driver.find_elements(*Homepageclass.search_results_selector)
    
    def download_app(self):
        return self.driver.find_element(*Homepageclass.downloadApp_link_selector)
    
    def About(self):
        return self.driver.find_element(*Homepageclass.about_link_selector)
    
    def Blog(self):
        return self.driver.find_element(*Homepageclass.blog_link_selector)
    
    def careers(self):
        return self.driver.find_element(*Homepageclass.careers_link_selector)
    
    def referAndearn(self):
        return self.driver.find_element(*Homepageclass.referAndearn_link_selector)
    
    def flight_tickets(self):
        return self.driver.find_element(*Homepageclass.flightTickets_link_selector)
    
    def cost_of_living(self):
        return self.driver.find_element(*Homepageclass.costOfliving_link_selector)
    
    def find_my_kinda_room(self):
        return self.driver.find_element(*Homepageclass.findMyKindaRoom_link_selector)
    
    def services(self):
        return self.driver.find_element(*Homepageclass.services_link_selector)
    
    def scholarship(self):
        return self.driver.find_element(*Homepageclass.scholarship_link_selector)
    
    def heroTitle(self):
        return self.driver.find_element(*Homepageclass.hero_title_selector)
    
    def heroKinda(self):
        return self.driver.find_element(*Homepageclass.hero_kinda_selector)
    
    def heroTrustPilot(self):
        return self.driver.find_element(*Homepageclass.hero_trust_pilot_selector)
    
    def heroVideoReview(self):
        return self.driver.find_element(*Homepageclass.hero_video_reviews_selector)
    
    def heroKindaDesc(self):
        return self.driver.find_element(*Homepageclass.hero_kinda_desc_selector)
    
    #----------------------------Top cities images --------------------------------------
    
    def londonImg(self):
        return self.driver.find_element(*Homepageclass.londonImage_selector)
    
    def nottinghamImg(self):
        return self.driver.find_element(*Homepageclass.nottinghamImage_selector)
    
    def leedsImg(self):
        return self.driver.find_element(*Homepageclass.leedsImage_selector)
    
    def melbourneImg(self):
        return self.driver.find_element(*Homepageclass.melbourneImage_selector)
    
    def birminghamImg(self):
        return self.driver.find_element(*Homepageclass.birminghamImage_selector)
    
    def liverpoolImg(self):
        return self.driver.find_element(*Homepageclass.liverpoolImage_selector)
    
    def torontoImg(self):
        return self.driver.find_element(*Homepageclass.torontoImage_selector)
    
    def newyorkImg(self):
        return self.driver.find_element(*Homepageclass.newyorkImage_selector)
    
    # -------------------- Top cities names -----------------------------------
    
    def topCityNames(self):
        return self.driver.find_elements(*Homepageclass.cityNames_selector)
    
    def bedsCount(self):
        return self.driver.find_elements(*Homepageclass.bedsCount_selector)  
    
    #--------------------------- perfect home section -------------------
    
    
    def title(self):
        return self.driver.find_element(*Homepageclass.Title_selector)
    
    def descOne(self):
        return self.driver.find_element(*Homepageclass.descOne_selector)
    
    def descTwo(self):
        return self.driver.find_element(*Homepageclass.descTwo_selector)
    
    def descThree(self):
        return self.driver.find_element(*Homepageclass.descThree_selector)
    
    def TandCperfecthome(self):
        return self.driver.find_element(*Homepageclass.termsAndConditions_selector)
    
    # ------------------------------ Popular Properties ----------------------------
    
    def popUK(self):
        return self.driver.find_element(*Homepageclass.uk_selector)
    
    def popAUS(self):
        return self.driver.find_element(*Homepageclass.australia_selector)
    
    def popIRE(self):
        return self.driver.find_element(*Homepageclass.ireland_selector)
    
    def popCAN(self):
        return self.driver.find_element(*Homepageclass.canada_selector)
    
    def popUS(self):
        return self.driver.find_element(*Homepageclass.us_selector)
    
    def vertCityNames(self):
        return self.driver.find_elements(*Homepageclass.vertCityNames_selector)
    
    def popularPropertiesNames(self):
        return self.driver.find_elements(*Homepageclass.popPropertiesNames_selector)
    
    def popularPropertiesPrice(self):
        return self.driver.find_elements(*Homepageclass.popPropertiesPrice_selector)