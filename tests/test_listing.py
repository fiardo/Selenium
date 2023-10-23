from pytest import mark
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
from pageData.listingPage import listingClass
from pageData.header import Headerclass
import pytest
from selenium.webdriver.common.alert import Alert
import re
import random
import string

N = 7


class Test_lising(Invokation):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = "".join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res + ".university@yopmail.com"
    faqPageUrl = "https://www.universityliving.com/faq"

    @mark.testomatio("@T561e803d")
    def test_listing_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        listing = listingClass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        header = Headerclass(self.driver)
        loginEmail = "harsh.sachan@universityliving.com"
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass
        cityKey = "london"
        log.info("selected city for listing automation " + cityKey)
        homepageObj.searchbar().send_keys(cityKey)
        time.sleep(3)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        log.info("search bar is working fine")
        assert listing.selectUniversityBar().is_displayed()
        assert listing.filterByBtn().is_displayed()
        log.info("filters are available on the selected listing page")
        assert listing.accTitle().is_displayed()
        log.info("listing page description is available")
        assert listing.readMoreBtn().is_displayed()
        assert listing.perfectHomeTitle().is_displayed()
        assert listing.searchCompareRelaxTitle().is_displayed()
        assert listing.easyPeasyTitle().is_displayed()
        assert listing.priceMatchGuaranteeTitle().is_displayed()
        assert listing.helpCenterLinkFAQ().is_displayed()
        log.info("help centre FAQ link is present")
        assert listing.breadCrumCity().text == cityKey.capitalize()
        log.info("city name is correct in listing breadcrum")
        isCityDescription = listing.cityDescMainTitle().is_displayed()
        if isCityDescription:
            log.info(listing.cityDescMainTitle().text)
            assert (
                listing.cityDescMainTitle().text
                == "Best " + cityKey.capitalize() + " Accommodation For Students"
            )
        else:
            log.warning("city description is missing")
        listing.pbsaBtn().click()
        time.sleep(2)
        pbsaStayText = listing.placesToStayCount().text
        pbsaStayCount = int("".join(re.findall("\\d", pbsaStayText)))
        log.info("stay count on PBSA -->" + str(pbsaStayCount))
        listing.hmoBtn().click()
        time.sleep(2)
        hmoStayText = listing.placesToStayCount().text
        hmoStayCount = int("".join(re.findall("\\d", hmoStayText)))
        log.info("stay count on HMO -->" + str(hmoStayCount))
        totalStayCount = pbsaStayCount + hmoStayCount
        log.info("total stay count [ PBSA + HMO ] --> " + str(totalStayCount))
        listing.pbsaBtn().click()
        time.sleep(2)
        lastPaginationPbsa = int(listing.lastPagination().text)
        listing.lastPagination().click()
        time.sleep(2)
        lastPaginationPbsaPropCount = len(listing.totalPropertyCardsBtmOnPage())
        totalCardCountPbsa = (lastPaginationPbsa - 1) * 12 + lastPaginationPbsaPropCount
        log.info("total property cards present on PBSA -->" + str(totalCardCountPbsa))
        listing.hmoBtn().click()
        time.sleep(3)
        lastPaginationHmo = int(listing.lastPagination().text)
        listing.lastPagination().click()
        time.sleep(2)
        lastPaginationHmoPropCount = len(listing.totalPropertyCardsBtmOnPage())
        totalCardCountHmo = (lastPaginationHmo - 1) * 12 + lastPaginationHmoPropCount
        log.info("total property cards present on HMO -->" + str(totalCardCountHmo))
        if totalCardCountPbsa == pbsaStayCount and totalCardCountHmo == hmoStayCount:
            log.info(
                "stay count and property card count is same for both category type"
            )
        else:
            log.critical("stay count and property card count are not equal plz check")
        listing.pbsaBtn().click()
        listing.filterByBtn().click()
        listing.filterShowResultBtn().click()
        for clsoeBtn in listing.filterPillClose():
            clsoeBtn.click()
        listing.filterByBtn().click()
        listing.filterDistanceBtn().click()
        listing.filterShowResultBtn().click()
        time.sleep(3)
        distanceList = []
        for distances in listing.propertyDistances():
            try:
                distanceList.append(distances.text)
            except Exception:
                listing.propertyDistances()
                distanceList.append(distances.text)

        cleanDistance_List = [
            float(item.replace(" miles", "")) for item in distanceList
        ]
        log.info("Distance list after after filter application %s", cleanDistance_List)
        sortedDistace = sorted(cleanDistance_List)
        log.info("Sorted distance list from low ot high %s", sortedDistace)
        if sortedDistace == cleanDistance_List:
            log.info("Distance filter is working fine")
        else:
            log.warning("Distance filter is not workig fine plz check")
        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()

        try:
            listing.filterByBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterByBtn().click()

        listing.filterPriceLowToHighBtn().click()
        listing.filterShowResultBtn().click()
        time.sleep(2)
        priceList = []
        for priceLowToHigh in listing.propertyPrices():
            priceList.append(priceLowToHigh.text)
        log.info("price list after filter application %s", priceList)
        currencyList = []
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]
        cleanedPriceLowToHigh_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]
        log.info(
            "cleaned price low to high integer list -->%s", cleanedPriceLowToHigh_list
        )
        sortedPriceList = sorted(cleanedPriceLowToHigh_list)
        log.info("sorted list price low to high %s", sortedPriceList)
        if sortedPriceList == cleanedPriceLowToHigh_list:
            log.info("Price low to high filter is working fine")
        else:
            log.warning("Price low to high filter is not working fine")
        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()
        try:
            listing.filterByBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            time.sleep(3)
            listing.filterByBtn().click()

        # listing.filterPriceHighToLowBtn().click()
        try:
            listing.filterPriceHighToLowBtn().click()
            listing.filterShowResultBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterPriceHighToLowBtn().click()
            listing.filterShowResultBtn().click()

        time.sleep(2)
        priceList = []
        for priceHighToLow in listing.propertyPrices():
            priceList.append(priceHighToLow.text)
        log.info("price high to low list -->%s", priceList)
        currencyList = []
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]
        cleanedPriceHighToLow_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]
        log.info("cleaned price high to low list -->%s", cleanedPriceHighToLow_list)
        sortedPriceList = sorted(cleanedPriceHighToLow_list)
        log.info("sorted list price high to low %s", sortedPriceList[::-1])
        if sortedPriceList[::-1] == cleanedPriceHighToLow_list:
            log.info("Price high to low filter is working fine")
        else:
            log.warning("Price high to low filter is not working fine")
        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()
        try:
            listing.filterByBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterByBtn().click()

        listing.filterBestOfferBtn().click()
        try:
            listing.filterShowResultBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterShowResultBtn().click()

        time.sleep(2)
        offerList = []
        for offer in listing.offerUptoValue():
            offerList.append(offer.text)
        log.info("offer list --> %s", offerList)
        currencyList = []
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]
        cleanedBestOffer_list = [
            int(item.replace(currency, "").replace(",", "").strip())
            for item in offerList
        ]
        log.info("cleaned best offer list -->%s", cleanedBestOffer_list)
        sortedOfferList = sorted(cleanedBestOffer_list)
        if sortedOfferList[::-1] == cleanedBestOffer_list:
            log.info("best offer filter is working fine")
        else:
            log.warning("best offer filter is not working fine.")
        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()
        try:
            listing.filterByBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterByBtn().click()
        listing.filterMostPopularBtn().click()
        try:
            listing.filterShowResultBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
        propertyName_list = []
        for propNames in listing.propertyNames():
            propertyName_list.append(propNames.text)
        log.info("most popular property names --> %s", propertyName_list)
        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()
        listing.filterByBtn().click()
        listing.startPriceInput().send_keys(200)
        time.sleep(5)
        listing.endPriceInput().send_keys(250)
        try:
            listing.filterShowResultBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            time.sleep(3)
            listing.filterShowResultBtn().click()

        time.sleep(2)
        priceList = []
        for prices in listing.propertyPrices():
            priceList.append(prices.text)
            time.sleep(1)
        log.info("price list ->%s", priceList)
        currencyList = []
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]
        cleanedPrice_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]
        log.info("cleaned price low to high integer list -->%s", cleanedPrice_list)
        for value in cleanedPrice_list:
            if value >= 200 and value <= 250:
                flag = True
            else:
                flag = False
        if flag == True:
            log.info("start and end price filter is working fine")
        elif flag == False:
            log.warning("start and end price filter is not working fine")
        listing.filterByBtn().click()
        listing.filterClearAllBtn().click()
        listing.filterMostPopularBtn()
        listing.filterShowResultBtn().click()
        listing.addToFavIconOne().click()
        loginPopUPObj.emailfield().send_keys(Test_lising.newEmail.lower())
        log.info(
            "used email id for add to favorite-->" + str(Test_lising.newEmail.lower())
        )
        time.sleep(2)
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.firstName().send_keys("test")
        loginPopUPObj.lastName().send_keys("test")
        loginPopUPObj.phoneNumber().send_keys(Test_lising.phone_number)
        log.info(
            "used phone number for add to favorite -->" + str(Test_lising.phone_number)
        )
        loginPopUPObj.signUpBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()
        listing.addToFavIconOne().click()
        listing.addToFavIconTwo().click()
        listing.addFavToaster().is_displayed()
        propertynames = []
        for prop in listing.propertyNames():
            propertynames.append(prop.text)
        addToFavProperty = propertynames[0:2]
        log.info("Add to favorite properties-->%s", addToFavProperty)
        loginPopUPObj.profileIcon().click()
        time.sleep(5)
        loginPopUPObj.wishListSection().click()
        wishlistPropertyNames = []
        for prop in loginPopUPObj.wishListPropertyNames():
            wishlistPropertyNames.append(prop.text)
        log.info("Property names in profile wishlist -->%s", wishlistPropertyNames[0:2])
        if addToFavProperty[0:2] == wishlistPropertyNames[0:2]:
            log.info("add to favorite is working fine")
        else:
            log.warning("add to favorite is not working fine.")
        self.driver.back()
        self.driver.back()
        listing.compareWidgetBtn().click()
        assert listing.goToCompareBtn().is_displayed()
        listing.goToCompareBtn().click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        propertyNames = []
        for properties in listing.propertyNames():
            propertyNames.append(properties.text)
        addToCompareEventList = []
        for i in listing.addToCompareBtn():
            addToCompareEventList.append(i)
        compareCount = 0
        while compareCount < 4:
            addToCompareEventList[compareCount].click()
            compareCount = compareCount + 1
        listing.compareWidgetBtn().click()
        compareWidgetProperteis = []
        for item in listing.compareWidgetPropertiesName():
            compareWidgetProperteis.append(item.text)
        assert listing.compareWidgetBtnCount().text == "4"
        log.info("added properties in compare -> %s", propertyNames[0:4])
        log.info("widget property names -> %s", compareWidgetProperteis)
        assert propertyNames[0:4] == compareWidgetProperteis
        listing.compareWidgetBtn().click()
        listing.selectUniversityBar().click()
        universities = []
        for item in listing.universityNameList():
            universities.append(item.text)
        try:
            while listing.universityNameList()[-1].text == "Load more":
                listing.universityNameList()[-1].click()
            log.info(
                "last university name -> %s", listing.universityNameList()[-1].text
            )
            listing.universityNameList()[-1].click()
            log.info("universities name list -> %s", universities)
            time.sleep(3)
        except Exception:
            listing.universityNameList()[0].click()
            log.info("universities name list -> %s", universities)
        try:
            listing.filterByBtn().click()
        except Exception:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "siqiframe"))
            time.sleep(3)
            self.driver.find_element(By.ID, "min_window").click()
            self.driver.switch_to.default_content()
            listing.filterByBtn().click()
        listing.filterShowResultBtn().click()
        filterKeyAfterUniversity = []
        filterValueAfterUniversity = []
        for item in listing.filterPillKey():
            filterKeyAfterUniversity.append(item.text)
            time.sleep(1)
        for item in listing.filterPillValue():
            filterValueAfterUniversity.append(item.text)
            time.sleep(1)
        time.sleep(3)
        log.info("filter key ->%s", filterKeyAfterUniversity)
        log.info("filter value ->%s", filterValueAfterUniversity)
        appliedFilters = []
        for i in range(0, len(filterKeyAfterUniversity)):
            appliedFilters.append(
                filterKeyAfterUniversity[i] + filterValueAfterUniversity[i]
            )
        log.info("applied filters -->%s", appliedFilters)
        time.sleep(3)
        try:
            isNearBy = listing.nearByText().is_displayed()
        except Exception:
            isNearBy = False
        if isNearBy:
            log.info("near by places are available on the listing page")
            nearBylist = []
            for places in listing.nearByPlacesNames():
                nearBylist.append(places.text)
            log.info("near by places ->%s", nearBylist)
        else:
            log.info("no near by places are present")
        assert listing.helpCenterLinkFAQ().is_displayed()
        listing.helpCenterLinkFAQ().click()
        time.sleep(3)
        helpCentreRedirectionUrl = self.driver.current_url
        assert helpCentreRedirectionUrl == Test_lising.faqPageUrl
        self.driver.back()
        log.info("FAQ help centre link redirection is working fine.")
        listing.breadCrumCityUni().click()
        time.sleep(2)
        try:
            listedFAQ = []
            for faq in listing.allFAQs():
                listedFAQ.append(faq.text)
            log.info("Listed FAQs on the pages ->%s", listedFAQ)
            log.info("Total FAQs on page -> " + str(len(listedFAQ)))
        except Exception:
            log.critical("FAQs are not present for the respective city")
        for faq in listing.allFAQs():
            faq.click()
