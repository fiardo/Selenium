from selenium.webdriver.common.by import By


class listingClass:
    def __init__(self, driver):
        self.driver = driver

    # breadcrum section selectros

    breadCrum_selector = (By.XPATH, "//nav/ol/li/a")
    breadCrumCity_selector = (By.XPATH, "(//nav/ol/li/span)[3]")

    # accommodation title selector
    accTitle_selector = (By.XPATH, "//h1")

    # select university selector
    selectUni_selector = (
        By.XPATH,
        "//input[@class='flex truncate items-center content-font w-full h-11 placeholder:text-gray-400 text-gray-700 px-3 rounded border border-gray-200 box-border pl-11 te-uselect']",
    )

    # pbsa and hmo category button

    pbsaBtn_selector = (By.XPATH, "//label[text()='Student Housing']")
    hmoBtn_selector = (By.XPATH, "//label[text()='Private Apartment']")

    # filter by selector

    filterBtn_selector = (By.XPATH, "//div[text()='Filter By ']")

    # city description title
    cityDescReadMore_selector = (By.XPATH, "//label[@for='read-more-controller']")
    cityDescOne_selector = (By.XPATH, "(//h2[1])[1]")
    cityDescTwo_selector = (By.XPATH, "(//h2[2])[1]")
    cityDescThree_selector = (By.XPATH, "(//h2[3])[1]")
    cityDescFour_selector = (By.XPATH, "(//h2[4])[1]")

    # let us find your perfect home section

    perfectHomeTitle_selector = (
        By.XPATH,
        "//div[text()='Let us find your perfect home!']",
    )

    searchCompareRelaxTitle_selector = (
        By.XPATH,
        "//p[text()='Search - Compare - Relax']",
    )

    paraOne_selector = (
        By.XPATH,
        "//p[text()='Choose from 1.5 Mn 100% verified student rooms near the university & compare between the best options.']",
    )

    easyPeasyTitle_selector = (By.XPATH, "//p[text()='Easy Peasy']")

    paraTwo_selector = (
        By.XPATH,
        "//p[text()='Instantly book the room in a matter of minutes. Save your time for more important things (Netflix).']",
    )

    priceMatchGuarantee_selector = (By.XPATH, "//p[text()='Price Match Guarantee']")

    paraThree_selector = (
        By.XPATH,
        "//p[text()='We keep our promises. Grab the best offers along with the lowest price promise.']",
    )

    # FAQ section selectors

    allFaqs_selector = (
        By.XPATH,
        "//div[@class='Listing_listingFaq__YCUTi']/details/summary",
    )

    # help center selector -  FAQ

    helpCenterFaq_selector = (By.XPATH, "(//a[@href='/faq'])[1]")

    # total property cards on page
    totalPropCards_selector = (
        By.XPATH,
        "//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3']/div",
    )
    totalPropCardsBtm_selector = (
        By.XPATH,
        "//div[@class='grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3']/div/div/div[2]",
    )

    # last pagiantion selector

    lastPage_selector = (By.XPATH, "(//nav[@aria-label='Pagination'])/button[last()-1]")
    firstPage_selector = (By.XPATH, "(//nav[@aria-label='Pagination'])/button[2]")

    # property card bottom description

    propertyNames_selector = (
        By.XPATH,
        "(//div[@class='w-full bg-white rounded-b-md p-3'])/div/a/p",
    )
    propertyDistance_selector = (
        By.XPATH,
        "(//div[@class='w-full bg-white rounded-b-md p-3'])/div[1]/div",
    )
    propertyType_selector = (
        By.XPATH,
        "(//div[@class='w-full bg-white rounded-b-md p-3'])/div[2]/div[1]",
    )
    propertyCity_selector = (
        By.XPATH,
        "(//div[@class='w-full bg-white rounded-b-md p-3'])/div[3]/div/span",
    )
    propertyPrice_selector = (
        By.XPATH,
        "(//div[@class='w-full bg-white rounded-b-md p-3'])/div[3]/div[2]",
    )

    # ----------------------------- filter btn selector ----------------------------
    filtetBtn_selector = (By.XPATH, "//div[text()='Filter By ']")

    # ---------------------------- select university bar -------------------------------
    selectUniversityBar_selector = (
        By.XPATH,
        "//input[@placeholder='Select University']",
    )
    universityNameContainer_selector = (By.ID, "university-search")
    universityNameList_selector = (By.XPATH, "//div[@id='university-search']/a")
    universityFirst_selector = (By.ID, "university-search-item-0")

    # ------------------------------------ filter pills selectors ---------------------

    filterPillKey_selctor = (By.XPATH, "//li[@class='shrink-0']/p/span[1]")
    filterPillValue_selector = (By.XPATH, "//li[@class='shrink-0']/p/span[2]")
    filterPillClose_selector = (By.XPATH, "//li[@class='shrink-0']/p/span[3]")

    # ------------------------------------- compare selectors ------------------------

    addToCompare_selector = (By.XPATH, "//span[text()='Add to Compare']")
    removeFromCompare_selector = (By.XPATH, "//span[text()='Remove from Compare']")
    fillingFastTag_selector = (By.XPATH, "//span[text()='Filling Fast']")
    compareWidgetBtn_selector = (By.ID, "compare_widget")
    compareWidget_count = (
        By.XPATH,
        "//div[@class='w-5 h-5 bg-theme-orange p-1 absolute -right-1 -top-1.5 rounded-full flex justify-center items-center text-white text-xs']",
    )
    compareWidgetClearAll_selector = (By.XPATH, "//p[text()='Clear All']")
    compareWidgetDeleteIcon_selector = (By.XPATH, "//img[@alt='Delete Icon']")
    compareWidgetCompareBtn_selector = (By.XPATH, "//div[text()='COMPARE']")
    compareWidgetBtnCount_selector = (
        By.XPATH,
        "//div[@class='bg-white text-theme-orange w-5 h-5 rounded-full flex justify-center items-center text-base']",
    )
    compareProperties_selector = (
        By.XPATH,
        "//p[@class='w-full truncate font-semibold']",
    )

    goToCompareBtn_selector = (By.XPATH, "//div[text()='GO TO COMPARE']")
    propertiesNamesInWidget_selector = (
        By.XPATH,
        "//p[@class='w-full truncate font-semibold']",
    )

    compareWidgetPropPrices_selector = (
        By.XPATH,
        "//span[@class='text-theme-orange font-medium']",
    )

    # -------------------------------- place stay count selector --------------------------

    placeToStayCount_selector = (
        By.XPATH,
        "//div[@class='flex text-xs items-center text-theme-blue font-semibold']",
    )

    # ------------------------------------ add to favorite icon ----------------------

    addToFavIcon_selector = (By.XPATH, "(//div[@class='absolute top-2 right-2'])[1]")
    addFavToaster_selector = (By.XPATH, "//div[@role='alert']")

    # ------------------------------ filter selectors ------------------------------------
    clearAllBtn_selector = (By.XPATH, "//div[text()='Clear All']")
    showResultBtn_selector = (By.XPATH, "//div[text()='Show Results']")
    distanceRadioBtn_selector = (By.ID, "sort-distance")
    mostPopularRadioBtn_selector = (By.ID, "sort-mostPopular")
    priceLowToHighRadioBtn_selector = (By.ID, "sort-price")
    priceHighToLowRadioBtn_selector = (By.ID, "sort--price")
    bestOfferRadioBtn_selector = (By.ID, "sort-offer")
    offerUptoValue_selector = (
        By.XPATH,
        "//span[@class='text-theme-orange font-semibold']",
    )
    fillingFastYes_selector = (By.ID, "fillingFast-yes")
    fillingFastNo_selector = (By.ID, "fillingFast-no")

    # -------------------------------------- chat box selector ---------------------------------
    chatMinBtn_selector = (By.ID, "min_window")
    contactWidget_selector = (
        By.XPATH,
        "//div[@class='shadow-xl peer rounded-full bg-theme-orange relative p-2.5 w-14 h-14 flex items-center justify-center']",
    )

    chatWidget_selector = (By.XPATH, "//div[@class='relative'][2]")

    # -------------------------------------- methods -------------------------------------------

    # Bredcrum section

    def breadCrumStart(self):
        return self.driver.find_elements(*listingClass.breadCrum_selector)

    def breadCrumCity(self):
        return self.driver.find_element(*listingClass.breadCrumCity_selector)

    # accommodation title

    def accTitle(self):
        return self.driver.find_element(*listingClass.accTitle_selector)

    # select university

    def selectUni(self):
        return self.driver.find_element(*listingClass.selectUni_selector)

    # pbsa and hmo category button

    def pbsaBtn(self):
        return self.driver.find_element(*listingClass.pbsaBtn_selector)

    def hmoBtn(self):
        return self.driver.find_element(*listingClass.hmoBtn_selector)

    # city description

    def readMoreBtn(self):
        return self.driver.find_element(*listingClass.cityDescReadMore_selector)

    def headingOne(self):
        return self.driver.find_element(*listingClass.cityDescOne_selector)

    def headingTwo(self):
        return self.driver.find_element(*listingClass.cityDescTwo_selector)

    def headingThree(self):
        return self.driver.find_element(*listingClass.cityDescThree_selector)

    def headingFour(self):
        return self.driver.find_element(*listingClass.cityDescFour_selector)

    # title and description for let us find your perfect home section

    def perfectHomeTitle(self):
        return self.driver.find_element(*listingClass.perfectHomeTitle_selector)

    def searchCompareRelaxTitle(self):
        return self.driver.find_element(*listingClass.searchCompareRelaxTitle_selector)

    def paraOne(self):
        return self.driver.find_element(*listingClass.paraOne_selector)

    def easyPeasyTitle(self):
        return self.driver.find_element(*listingClass.easyPeasyTitle_selector)

    def paraTwo(self):
        return self.driver.find_element(*listingClass.paraTwo_selector)

    def priceMatchGuaranteeTitle(self):
        return self.driver.find_element(*listingClass.priceMatchGuarantee_selector)

    def paraThree(self):
        return self.driver.find_element(*listingClass.paraThree_selector)

    # last and first pagination method

    def lastPagination(self):
        return self.driver.find_element(*listingClass.lastPage_selector)

    def firstPagination(self):
        return self.driver.find_element(*listingClass.firstPage_selector)

    # total property cards on page

    def totalPropertyCardsOnPage(self):
        return self.driver.find_elements(*listingClass.totalPropCards_selector)

    def totalPropertyCardsBtmOnPage(self):
        return self.driver.find_elements(*listingClass.totalPropCardsBtm_selector)

    # propert card bottom description methods

    def propertyNames(self):
        return self.driver.find_elements(*listingClass.propertyNames_selector)

    def propertyDistances(self):
        return self.driver.find_elements(*listingClass.propertyDistance_selector)

    def propertytypes(self):
        return self.driver.find_elements(*listingClass.propertyType_selector)

    def propertyCities(self):
        return self.driver.find_elements(*listingClass.propertyCity_selector)

    def propertyPrices(self):
        return self.driver.find_elements(*listingClass.propertyPrice_selector)

    # fitler btn methods

    def filterByBtn(self):
        return self.driver.find_element(*listingClass.filterBtn_selector)

    # select university methods

    def selectUniversityBar(self):
        return self.driver.find_element(*listingClass.selectUniversityBar_selector)

    def universityNameContainer(self):
        return self.driver.find_element(*listingClass.universityNameContainer_selector)

    def universityNameList(self):
        return self.driver.find_elements(*listingClass.universityNameList_selector)

    def firstUniversity(self):
        return self.driver.find_element(*listingClass.universityFirst_selector)

    # Faw section Methods

    def allFAQs(self):
        return self.driver.find_elements(*listingClass.allFaqs_selector)

    def helpCenterLinkFAQ(self):
        return self.driver.find_element(*listingClass.helpCenterFaq_selector)

    # fitler pills on page methods

    def filterPillKey(self):
        return self.driver.find_elements(*listingClass.filterPillKey_selctor)

    def filterPillValue(self):
        return self.driver.find_elements(*listingClass.filterPillValue_selector)

    def filterPillClose(self):
        return self.driver.find_elements(*listingClass.filterPillClose_selector)

    # compare methods (widgets and listing compare elements)

    def addToCompareBtn(self):
        return self.driver.find_elements(*listingClass.addToCompare_selector)

    def removeFromCompareBtn(self):
        return self.driver.find_elements(*listingClass.removeFromCompare_selector)

    def compareWidgetBtn(self):
        return self.driver.find_element(*listingClass.compareWidgetBtn_selector)

    def compareWidgetCount(self):
        return self.driver.find_element(*listingClass.compareWidget_count)

    def compareWidgetClearAllBtn(self):
        return self.driver.find_element(*listingClass.compareWidgetClearAll_selector)

    def compareWidgetDeleteIcon(self):
        return self.driver.find_elements(*listingClass.compareWidgetDeleteIcon_selector)

    def compareWidgetCompareBtn(self):
        return self.driver.find_element(*listingClass.compareWidgetCompareBtn_selector)

    def compareWidgetBtnCount(self):
        return self.driver.find_element(*listingClass.compareWidgetBtnCount_selector)

    def compareWidgetPropertiesName(self):
        return self.driver.find_elements(*listingClass.compareProperties_selector)

    def goToCompareBtn(self):
        return self.driver.find_element(*listingClass.goToCompareBtn_selector)

    def propertiesNameInWidget(self):
        return self.driver.find_elements(*listingClass.propertiesNamesInWidget_selector)

    def propertiesPricesInWidget(self):
        return self.driver.find_elements(*listingClass.compareWidgetPropPrices_selector)

    def fillingFastTags(self):
        return self.driver.find_elements(*listingClass.fillingFastTag_selector)

    # ----------------------------------- place to stay count ----------------------------

    def placesToStayCount(self):
        return self.driver.find_element(*listingClass.placeToStayCount_selector)

    # ------------------------------- add to fav icon method ------------------------------

    def addToFavIcon(self):
        return self.driver.find_element(*listingClass.addToFavIcon_selector)

    def addFavToaster(self):
        return self.driver.find_element(*listingClass.addFavToaster_selector)

    # --------------------------------- filter methods -----------------------------------

    def filterClearAllBtn(self):
        return self.driver.find_element(*listingClass.clearAllBtn_selector)

    def filterShowResultBtn(self):
        return self.driver.find_element(*listingClass.showResultBtn_selector)

    def filterDistanceBtn(self):
        return self.driver.find_element(*listingClass.distanceRadioBtn_selector)

    def filterMostPopularBtn(self):
        return self.driver.find_element(*listingClass.mostPopularRadioBtn_selector)

    def filterPriceLowToHighBtn(self):
        return self.driver.find_element(*listingClass.priceLowToHighRadioBtn_selector)

    def filterPriceHighToLowBtn(self):
        return self.driver.find_element(*listingClass.priceHighToLowRadioBtn_selector)

    def filterBestOfferBtn(self):
        return self.driver.find_element(*listingClass.bestOfferRadioBtn_selector)

    def offerUptoValue(self):
        return self.driver.find_elements(*listingClass.offerUptoValue_selector)

    # -------------------------------------- chat pop up methods -------------------------------

    def chatMinimizedBtn(self):
        return self.driver.find_element(*listingClass.chatMinBtn_selector)

    def contactWidget(self):
        return self.driver.find_element(*listingClass.contactWidget_selector)

    def chatWidget(self):
        return self.driver.find_element(*listingClass.chatWidget_selector)
