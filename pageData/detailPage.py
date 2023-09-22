from selenium.webdriver.common.by import By

class detailpageClass:
    
    def __init__(self,driver):
        self.driver = driver
        
    enquireBtnSelector = (By.XPATH,"//div[text()='Enquire']")
    booknowBtnSelector = (By.XPATH,"//div[text()='Book Now']")    
    viewMoreRoomSelector = (By.XPATH,"//div[text()='View More Room Types']")
    joinwaitlistBtnSelector = (By.XPATH,"//div[text()='Join Waitlist']")
    joinwaitlistlastBtnSelector = (By.XPATH,"(//div[text()='Join Waitlist'])[last()]")
    firstnameSelector = (By.NAME, "firstName")
    lastnameSelector = (By.NAME, "lastName")
    phoneNumberSelector = (By.ID,"contactNumber")
    emailSelector = (By.NAME,"email")
    universityDropDown = (By.XPATH,"(//input[@placeholder = 'Select University'])[2]")
    uniItemSelector = (By.ID,"university-search-item-0")    
    messageSelector = (By.NAME,"userMessage")
    submitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    okBtnSelector = (By.XPATH,"//div[text()='OK']")
    noVisaNoPay_Selector = (By.XPATH,"(//div[text()='No Visa No Pay'])[1]")
    noUniNoPay_Selector = (By.XPATH,"(//div[text()='No University No Pay'])[1]")
    chooseYourRoom_Selector = (By.XPATH,"//div[text()='Choose Your Room']")
    fromPrice_selector = (By.XPATH,"//abbr/span")
    viewOffer_selector = (By.XPATH,"//u[text()='View Offer Details']")
    termsAndconditions_selector = (By.XPATH,"//span[text()='*T & C applied.']")
    viewOnMap_selctor = (By.XPATH,"//p[text()='View on Map']")
    allRoomType_selector = (By.XPATH,"//div[text()='All']")
    studioRoomType_selector = (By.XPATH,"//div[text()='Studio']")
    apartmentsRoomType_selector = (By.XPATH,"//div[text()='Apartments']")
    ensuiteRoomType_selector = (By.XPATH,"//div[text()='Ensuite']")
    othersRoomType_selector = (By.XPATH,"//div[text()='Others']")
    overview_selector = (By.XPATH,"//li[text()='Overview']")
    roomtype_selector = (By.XPATH,"//li[text()='Room Types']")
    PaymentInfo_selector = (By.XPATH,"//li[text()='Payment Info']")
    Reviews_selector = (By.XPATH,"//li[text()='Reviews']")
    similarProperties_selector = (By.XPATH,"//li[text()='Similar Properties']")
    wishlist_selector = (By.XPATH,"//p[text()='Wishlist']")
    share_selector = (By.XPATH,"//p[text()='Share']")
    addTocompare_selector = (By.XPATH,"//span[text()='Add to Compare']")
    paymentInfoSection_selector = (By.XPATH,"//h3[text()='Payment Info']")
    cancellationPolicySection_selector = (By.XPATH,"//h3[text()='Cancellation Policy']")
    whatWeLoveSection_selector = (By.XPATH,"//h3[text()='What We Love']")
    similarCards_selector = (By.XPATH,"//div[@class='relative h-52']")
    similarPropertyNames_selector = (By.XPATH,"//div[@class='flex mb-2 justify-between items-center']")
    viewAllProperitesBtn_selector = (By.XPATH,"//div[text()='View All Properties']")
    roomName_selector = (By.XPATH,"//div[@class='text-lg font-bold mb-4 text-gray-800']")
    uniCount_selector = (By.XPATH,"//img[@alt='university-cap']")
    BookNowCount_selector = (By.XPATH,"//div[text()='Book Now']")
    joinWaitlistCount_selector = (By.XPATH,"//div[text()='Join Waitlist']")
    propertyNameInSummaryCard_selector = (By.XPATH,"//h3[text()='Chapter Ealing']")
    
#----------------------------------form details -----------------------------------------------
    
    totalPrice_selector = (By.XPATH,"//span[@automation_id='Total']")
    
    
    
    def enquireButton(self):
        return self.driver.find_element(*detailpageClass.enquireBtnSelector)
    
    def booknowButton(self):
        return self.driver.find_element(*detailpageClass.booknowBtnSelector)
    
    def viewMoreRoomBtn(self):
        return self.driver.find_element(*detailpageClass.viewMoreRoomSelector)
    
    def joinwaitlistBtn(self):
        return self.driver.find_element(*detailpageClass.joinwaitlistBtnSelector)
    
    def joinwaitlistLastBtn(self):
        return self.driver.find_element(*detailpageClass.joinwaitlistlastBtnSelector)
    
    def firstname(self):
        return self.driver.find_element(*detailpageClass.firstnameSelector)
    
    def lastname(self):
        return self.driver.find_element(*detailpageClass.lastnameSelector)
    
    def phoneNumber(self):
        return self.driver.find_element(*detailpageClass.phoneNumberSelector)
    
    def email(self):
        return self.driver.find_element(*detailpageClass.emailSelector)
    
    def universityDrop(self):
        return self.driver.find_element(*detailpageClass.universityDropDown)
    
    def universityDROPItem(self):
        return self.driver.find_element(*detailpageClass.uniItemSelector)
    
    def message(self):
        return self.driver.find_element(*detailpageClass.messageSelector)
    
    def submitBtn(self):
        return self.driver.find_element(*detailpageClass.submitBtnSelector)
    
    def okBtn(self):
        return self.driver.find_element(*detailpageClass.okBtnSelector)
    
    def noVisaNoPay(self):
        return self.driver.find_element(*detailpageClass.noVisaNoPay_Selector)
    
    def noUniNoPay(self):
        return self.driver.find_element(*detailpageClass.noUniNoPay_Selector)
    
    def chooseYourRoom(self):
        return self.driver.find_element(*detailpageClass.chooseYourRoom_Selector)
 
    def fromPrice(self):
        return self.driver.find_element(*detailpageClass.fromPrice_selector)
    
    def viewOffer(self):
        return self.driver.find_element(*detailpageClass.viewOffer_selector)
    
    def termsAndConditions(self):
        return self.driver.find_element(*detailpageClass.termsAndconditions_selector)

    def viewOnMap(self):
        return self.driver.find_element(*detailpageClass.viewOnMap_selctor)
    
    def allRoomTypeBtn(self):
        return self.driver.find_element(*detailpageClass.allRoomType_selector)   
    
    def studioRoomTypeBtn(self):
        return self.driver.find_element(*detailpageClass.studioRoomType_selector)
    
    def apartmentRoomTypeBtn(self):
        return self.driver.find_element(*detailpageClass.apartmentsRoomType_selector)
    
    def ensuiteRoomTypeBtn(self):
        return self.driver.find_element(*detailpageClass.ensuiteRoomType_selector)
    
    def othersRoomTypeBtn(self):
        return self.driver.find_element(*detailpageClass.othersRoomType_selector)
    
    def overveiwLink(self):
        return self.driver.find_element(*detailpageClass.overview_selector)
    
    def roomtypeLink(self):
        return self.driver.find_element(*detailpageClass.roomtype_selector)
    
    def paymentInfoLink(self):
        return self.driver.find_element(*detailpageClass.PaymentInfo_selector)
    
    def reviewsLink(self):
        return self.driver.find_element(*detailpageClass.Reviews_selector)
    
    def similarPropertyLink(self):
        return self.driver.find_element(*detailpageClass.similarProperties_selector)
    
    def wishlistLink(self):
        return self.driver.find_element(*detailpageClass.wishlist_selector)
    
    def shareLink(self):
        return self.driver.find_element(*detailpageClass.share_selector)
    
    def addTocompareBtn(self):
        return self.driver.find_element(*detailpageClass.addTocompare_selector)
    
    def paymentInfoSection(self):
        return self.driver.find_element(*detailpageClass.paymentInfoSection_selector)

    def cancellationPolicySection(self):
        return self.driver.find_element(*detailpageClass.cancellationPolicySection_selector)
    
    def whatWeLoveSection(self):
        return self.driver.find_element(*detailpageClass.whatWeLoveSection_selector)
    
    def similarCardsNames(self):
        return self.driver.find_elements(*detailpageClass.similarCards_selector)    
    
    def similarPropertyNames(self):
        return self.driver.find_elements(*detailpageClass.similarPropertyNames_selector)
    
    def viewAllPropertiesBtn(self):
        return self.driver.find_element(*detailpageClass.viewAllProperitesBtn_selector)
    
    def roomNames(self):
        return self.driver.find_elements(*detailpageClass.roomName_selector)
    
    def universityCount(self):
        return self.driver.find_elements(*detailpageClass.uniCount_selector)
    
    def BookNowCount(self):
        return self.driver.find_elements(*detailpageClass.BookNowCount_selector)
    
    def joinWaitlistCount(self):
        return self.driver.find_elements(*detailpageClass.joinWaitlistCount_selector)
    
    def propertyNameInSummaryCard(self):
        return self.driver.find_element(*detailpageClass.propertyNameInSummaryCard_selector)
    
    
    # ------------------------------------------- form methods -----------------------------------
    
    def totalPrice(self):
        return self.driver.find_element(*detailpageClass.totalPrice_selector)
    