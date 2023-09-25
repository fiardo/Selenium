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

    @mark.testomatio("@T51683ec0")
    def test_listing_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
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
        homepageObj.searchbar().send_keys(cityKey)
        time.sleep(3)
        homepageObj.searchbar().send_keys(Keys.ENTER)

        # asserting important elements of page

        assert listing.selectUniversityBar().is_displayed()
        assert listing.filterByBtn().is_displayed()
        assert listing.accTitle().is_displayed()
        assert listing.readMoreBtn().is_displayed()
        assert listing.perfectHomeTitle().is_displayed()
        assert listing.searchCompareRelaxTitle().is_displayed()
        assert listing.easyPeasyTitle().is_displayed()
        assert listing.priceMatchGuaranteeTitle().is_displayed()
        assert listing.helpCenterLinkFAQ().is_displayed()
        assert listing.breadCrumCity().text == cityKey.capitalize()

        assert listing

        # --------------------------------------- property stay count of PBSA ---------------------------------------

        listing.pbsaBtn().click()  # click on PBSA.
        time.sleep(2)
        pbsaStayText = listing.placesToStayCount().text
        pbsaStayCount = int("".join(re.findall("\\d", pbsaStayText)))
        log.info(pbsaStayCount)  # logging the PBSA stay count.

        # # -------------------------------------- property stay count of HMO ---------------------------------------

        listing.hmoBtn().click()  # click on HMO
        time.sleep(2)
        hmoStayText = listing.placesToStayCount().text
        hmoStayCount = int("".join(re.findall("\\d", hmoStayText)))
        log.info(hmoStayCount)  # logging the HMO stay count.

        # # ----------------------------------------- calculating the total stay count ( PBSA stay count + HMO stay count )----------------------------------------

        totalStayCount = pbsaStayCount + hmoStayCount
        log.info(
            "total stay count --> " + str(totalStayCount)
        )  # logging the total stay count of PBSA and HMO

        # # ------------------------------------- calculating the total card count of PBSA and HMO ----------------------------------------------------------

        # for PBSA
        listing.pbsaBtn().click()  # clicking on PBSA button
        time.sleep(2)
        lastPaginationPbsa = int(
            listing.lastPagination().text
        )  # getting last page count of PBSA
        listing.lastPagination().click()  # clicking on last page.
        time.sleep(2)
        lastPaginationPbsaPropCount = len(
            listing.totalPropertyCardsBtmOnPage()
        )  # getting count of property cards on last page of PBSA listing.

        totalCardCountPbsa = (
            (lastPaginationPbsa - 1) * 12
        ) + lastPaginationPbsaPropCount  # --> total card count [ (lastPagination -1) *12 + last page property cards]
        log.info(totalCardCountPbsa)  # logging the PBSA card count.

        # for HMO
        listing.hmoBtn().click()  # clicking on HMO button
        time.sleep(3)
        lastPaginationHmo = int(
            listing.lastPagination().text
        )  # getting last page count of HMO
        listing.lastPagination().click()  # clicking on last page of HMO
        time.sleep(2)
        lastPaginationHmoPropCount = len(
            listing.totalPropertyCardsBtmOnPage()
        )  # getting last page property cards on last page of HMO listing.
        totalCardCountHmo = (
            (lastPaginationHmo - 1) * 12
        ) + lastPaginationHmoPropCount  # --> total card count [ (lastPagination -1) *12 + last page property cards]
        log.info(totalCardCountHmo)  # logging the HMO card count

        # # ------------------------------- validating the stay count and total property count.

        if totalCardCountPbsa == pbsaStayCount and totalCardCountHmo == hmoStayCount:
            log.info("stay count and property card count are same")
        else:
            log.critical("stay count and property card count are not equal plz check")

        # ---------------------------------- Distance filter validations ---------------------------------.

        listing.pbsaBtn().click()  # clicking on PBSA btn
        listing.filterByBtn().click()  # opne filters
        listing.filterShowResultBtn().click()  # clickin on show result button so to get all the pre-applied filters

        for (
            clsoeBtn
        ) in listing.filterPillClose():  # removing all the pre-applied filters
            clsoeBtn.click()

        # applying the distance filter only.
        listing.filterByBtn().click()
        listing.filterDistanceBtn().click()
        listing.filterShowResultBtn().click()

        distanceList = (
            []
        )  # will contain all distance value on listing when distance filter is applied.
        for (
            distances
        ) in (
            listing.propertyDistances()
        ):  # adding distance values ( but the value will appears in miles format -> .13 miles,[need to remove miles] )
            distanceList.append(distances.text)

        cleanDistance_List = [
            float(item.replace(" miles", "")) for item in distanceList
        ]  # new cleaned list ( which contains distance without miles text )

        log.info("Distance list after after filter application %s", cleanDistance_List)

        # validating the distance sort filter

        sortedDistace = sorted(
            cleanDistance_List
        )  # sorting the cleaned list from low to high.

        log.info("Sorted distance list from low ot high %s", sortedDistace)

        if sortedDistace == cleanDistance_List:
            log.info("Distance filter is working fine")
        else:
            log.warning("Distance filter is not workig fine plz check")

        # ----------------------------------------------- Price Low to high filter validations -------------------------------------

        listing.pbsaBtn().click()  # cicking on PBSA
        for (
            closeBtn
        ) in listing.filterPillClose():  # removing all the pre-applied filters
            closeBtn.click()

        listing.filterByBtn().click()  # opening the filters
        listing.filterPriceLowToHighBtn().click()  # applying the price low to high filter
        listing.filterShowResultBtn().click()

        priceList = (
            []
        )  # this array will hold the values of price after filter application.

        for (
            priceLowToHigh
        ) in listing.propertyPrices():  # adding filters to the priceList Array
            priceList.append(priceLowToHigh.text)

        log.info("%s", priceList)

        currencyList = []  # currency list to hold the currency value
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]  # extracting the currency from the list

        cleanedPriceLowToHigh_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]  # removing /week and currecny from the list
        # validating the price low to high filter

        log.info(
            "cleaned price low to high integer list -->%s", cleanedPriceLowToHigh_list
        )

        sortedPriceList = sorted(cleanedPriceLowToHigh_list)
        log.info("sorted list price low to high %s", sortedPriceList)
        if sortedPriceList == cleanedPriceLowToHigh_list:
            log.info("Price low to high filter is working fine")
        else:
            log.warning("Price low to high filter is not working fine")

        # # ----------------------------------------------- Price High to Low filter validations -------------------------------------

        listing.pbsaBtn().click()  # cicking on PBSA
        for (
            closeBtn
        ) in listing.filterPillClose():  # removing all the pre-applied filters
            closeBtn.click()

        listing.filterByBtn().click()  # opening the filters
        listing.filterPriceHighToLowBtn().click()  # applying the price low to high filter
        listing.filterShowResultBtn().click()

        priceList = (
            []
        )  # this array will hold the values of price after filter application.

        for (
            priceHighToLow
        ) in listing.propertyPrices():  # adding filters to the priceList Array
            priceList.append(priceHighToLow.text)

        log.info("%s", priceList)

        currencyList = []  # currency list to hold the currency value
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]  # extracting the currency from the list

        cleanedPriceHighToLow_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]  # removing /week and currecny from the list
        # validating the price low to high filter

        log.info("cleaned price high to low list -->%s", cleanedPriceHighToLow_list)

        sortedPriceList = sorted(cleanedPriceHighToLow_list)
        log.info("sorted list price high to low %s", sortedPriceList[::-1])

        if sortedPriceList[::-1] == cleanedPriceHighToLow_list:
            log.info("Price high to low filter is working fine")
        else:
            log.warning("Price high to low filter is not working fine")

        # # -------------------------------- Best offer filter validation -----------------------------

        listing.pbsaBtn().click()  # click on PBSA
        for closeBtn in listing.filterPillClose():  # closing all pre-applied filter
            closeBtn.click()

        listing.filterByBtn().click()  # opening filter
        listing.filterBestOfferBtn().click()  # applying bes offer filter
        listing.filterShowResultBtn().click()

        offerList = []  # list to hold the offers values from the page

        for (
            offer
        ) in listing.offerUptoValue():  # adding offer values to the above temp list
            offerList.append(offer.text)

        log.info("offer list --> %s", offerList)  # logging the offer list

        currencyList = []  # currency list to hold the currency value
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]

        cleanedBestOffer_list = [
            int(item.replace(currency, "").replace(",", "").strip())
            for item in offerList
        ]  # removing the currency from the offer values

        log.info(
            "cleaned best offer list -->%s", cleanedBestOffer_list
        )  # logging the cleaned best offer list [ without currency ]

        sortedOfferList = sorted(cleanedBestOffer_list)  # sorting the offer list

        if sortedOfferList[::-1] == cleanedBestOffer_list:  # validating the sorted list
            log.info("best offer filter is working fine")
        else:
            log.warning("best offer filter is not working fine.")

        # # -------------------------------- Most popular filter validation -----------------------------

        listing.pbsaBtn().click()
        for closeBtn in listing.filterPillClose():
            closeBtn.click()

        listing.filterByBtn().click()
        listing.filterMostPopularBtn().click()
        listing.filterShowResultBtn().click()

        propertyName_list = []

        for propNames in listing.propertyNames():
            propertyName_list.append(propNames.text)

        log.info("most popular property names --> %s", propertyName_list)

        # # ---------------------------------- start price and end price validation -----------------------

        listing.pbsaBtn().click()

        for closeBtn in listing.filterPillClose():
            closeBtn.click()

        listing.filterByBtn().click()
        listing.startPriceInput().send_keys(200)
        time.sleep(5)
        listing.endPriceInput().send_keys(250)
        listing.filterShowResultBtn().click()

        priceList = []
        for prices in listing.propertyPrices():
            priceList.append(prices.text)

        log.info("%s", priceList)

        currencyList = []  # currency list to hold the currency value
        for value in priceList[0]:
            currencyList.append(value)
        currency = currencyList[0]  # extracting the currency from the list

        cleanedPrice_list = [
            float(item.replace("/week", "").replace(currency, "").strip())
            for item in priceList
        ]  # removing /week and currecny from the list
        # validating the price low to high filter

        log.info("cleaned price low to high integer list -->%s", cleanedPrice_list)

        for value in cleanedPrice_list:  # compare the ranged values
            if value >= 200 and value <= 250:
                flag = True
            else:
                flag = False

        if flag == True:  # logging the comparison result
            log.info("start and end price filter is working fine")
        elif flag == False:
            log.warning("start and end price filter is not working fine")

        listing.filterByBtn().click()
        listing.filterClearAllBtn().click()  # reseting the filter
        listing.filterMostPopularBtn()
        listing.filterShowResultBtn().click()  # selecting the most popular filter

        # # ------------------------------------ Add to favorites ---------------------------------------------

        # for new user
        listing.addToFavIconOne().click()  # Add to favorite [ login / sign up popup will appear ]

        loginPopUPObj.emailfield().send_keys(Test_lising.newEmail.lower())
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.firstName().send_keys("test")
        loginPopUPObj.lastName().send_keys("test")
        loginPopUPObj.phoneNumber().send_keys(Test_lising.phone_number)
        loginPopUPObj.signUpBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()

        listing.addToFavIconOne().click()  # clicking again on first property fav icon to add the propperty in wishlist.
        listing.addToFavIconTwo().click()  # clicking on second property fav icon to add the property in wishlist.
        listing.addFavToaster().is_displayed()  # validate the toaster appearance

        propertynames = []  # temporary list

        for prop in listing.propertyNames():  # adding property names in the temp list
            propertynames.append(prop.text)

        addToFavProperty = propertynames[
            0:2
        ]  # getting two properties which have been added in list
        log.info(addToFavProperty)
        loginPopUPObj.profileIcon().click()  # opening the dashboard
        time.sleep(5)
        loginPopUPObj.wishListSection().click()  # opening the wishlist section

        wishlistPropertyNames = []  # temporary list for wishlist properties

        for (
            prop
        ) in (
            loginPopUPObj.wishListPropertyNames()
        ):  # adding the wishlist property names to the temporary list
            wishlistPropertyNames.append(prop.text)

        log.info(wishlistPropertyNames[0:2])

        if (
            addToFavProperty[0:2] == wishlistPropertyNames[0:2]
        ):  # compare the properties names in wishlist from the listing.
            log.info("add to favorite is working fine")
        else:
            log.warning("add to favorite is not working fine.")

        self.driver.back()
        self.driver.back()

        # --------------------------------- compare widget validations ----------------------------------------

        listing.compareWidgetBtn().click()  # openin the compare widget
        assert (
            listing.goToCompareBtn().is_displayed()
        )  # asserting the go to compare button displayed property

        listing.goToCompareBtn().click()  # moving to compare page using go to compare button.
        time.sleep(3)
        # assert (
        #     self.driver.current_url
        #     == "https://www.universityliving.com/compare-property?ul_utm_source=city-desktop-website"
        # )

        self.driver.back()  # moving back to listing page
        time.sleep(3)

        propertyNames = []
        for (
            properties
        ) in listing.propertyNames():  #   adding property names in temporary list
            propertyNames.append(properties.text)

        addToCompareEventList = []
        for (
            i
        ) in (
            listing.addToCompareBtn()
        ):  # adding add to compare elements in temporary list
            addToCompareEventList.append(i)

        compareCount = 0
        while compareCount < 4:  # clicking on the add to compare till 4th element
            addToCompareEventList[compareCount].click()
            compareCount = compareCount + 1

        listing.compareWidgetBtn().click()
        compareWidgetProperteis = []
        for item in listing.compareWidgetPropertiesName():
            compareWidgetProperteis.append(item.text)

        assert listing.compareWidgetBtnCount().text == "4"

        log.info("listing properties -> %s", propertyNames[0:4])
        log.info("widget property names -> %s", compareWidgetProperteis)

        assert propertyNames[0:4] == compareWidgetProperteis

        # ------------------------------------------ university selction validations ----------------------------------------

        listing.selectUniversityBar().click()  # opening the unviersity bar
        universities = []
        for (
            item
        ) in (
            listing.universityNameList()
        ):  # getting all university name list with city and country names
            universities.append(item.text)

        try:
            while (
                listing.universityNameList()[-1].text == "Load more"
            ):  # clicking on load more and selcting the last university
                listing.universityNameList()[-1].click()

            log.info(
                "last university name -> %s", listing.universityNameList()[-1].text
            )
            listing.universityNameList()[-1].click()
            log.info("universities name list -> %s", universities)

            time.sleep(3)
        except (
            Exception
        ):  # if no load more element is present then select the first university
            listing.universityNameList()[0].click()
            log.info("universities name list -> %s", universities)

        listing.filterByBtn().click()  # opening the filter window
        listing.filterShowResultBtn().click()  # clicking on the show result btn

        filterKeyAfterUniversity = []  # temporary list for filter key
        filterValueAfterUniversity = []  # temporary list for filter value

        for item in listing.filterPillKey():
            filterKeyAfterUniversity.append(
                item.text
            )  # getting all the applied filter keys

        for item in listing.filterPillValue():
            filterValueAfterUniversity.append(
                item.text
            )  # getting all the applied filter values

        log.info("filter key ->%s", filterKeyAfterUniversity)
        log.info("filter value ->%s", filterValueAfterUniversity)

        appliedFilters = []
        for i in range(
            0, len(filterKeyAfterUniversity)
        ):  # appending key-value pair for the applied filters
            appliedFilters.append(
                filterKeyAfterUniversity[i] + filterValueAfterUniversity[i]
            )

        log.info("applied filters -->%s", appliedFilters)

        assert appliedFilters == [
            "FillingFast: Yes",
            "Sort: Distance",
        ]  # asserting the applied filters after selection of university.

        # ----------------------------------------- near by places validations --------------------------

        isNearBy = listing.nearByText().is_displayed()

        if isNearBy:
            log.info("near by places are available on the listing page")
            nearBylist = []
            for places in listing.nearByPlacesNames():
                nearBylist.append(places.text)

            log.info("near by places ->%s", nearBylist)

        else:
            log.info("no near by places are present")

        # ------------------------------------ help center validation ---------------------------------

        assert listing.helpCenterLinkFAQ().is_displayed()

        listing.helpCenterLinkFAQ().click()
        time.sleep(3)

        helpCentreRedirectionUrl = self.driver.current_url

        assert helpCentreRedirectionUrl == Test_lising.faqPageUrl
        self.driver.back()

        log.info("FAQ help centre link redirection is working fine.")

        # -------------------------------- city desription validations ------------------------------

        isCityDescription = listing.cityDescMainTitle().is_displayed()
        if isCityDescription:
            log.info(listing.cityDescMainTitle().text)
            assert (
                listing.cityDescMainTitle().text
                == "Best " + cityKey.capitalize() + " Accommodation For Students"
            )
        else:
            log.warning("city description is missing")

        # FAQ testing

        isFAQ = listing.faqTitleText().is_displayed()

        if isFAQ:
            listedFAQ = []
            for faq in listing.allFAQs():
                listedFAQ.append(faq.text)

            log.info("Listed FAQs on the pages ->%s", listedFAQ)
            log.info("Total FAQs on page -> " + str(len(listedFAQ)))

        else:
            log.critical("FAQs are not present for the respective city")

        # opening all faqs

        for faq in listing.allFAQs():
            faq.click()

        # --------------------------------------- university cases validation ------------------------------------------

        listing.selectUniversityBar().click()
        uni = []
        for item in listing.uniNameOnly():
            uni.append(item.text)
        log.info(uni)

        firstUniName = uni[0]
        listing.uniNameOnly()[0].click()

        isUniDesc = listing.cityDescMainTitle().is_displayed()
        if isUniDesc:
            log.info("university description is present")
            cleaned_text = re.sub(r"\([^)]*\)", "", firstUniName)

            log.info(listing.cityDescMainTitle().text)
            log.info("Everything about student accommodation near " + cleaned_text)
            assert (
                listing.cityDescMainTitle().text
                == "Everything about student accommodation near "
                + cleaned_text.rstrip()
            )
        else:
            log.warning("university / campus description is not present")

        # -FAQ testing

        isFAQ = listing.faqTitleText().is_displayed()

        if isFAQ:
            listedFAQ = []
            for faq in listing.allFAQs():
                listedFAQ.append(faq.text)

            log.info("Listed FAQs on the pages ->%s", listedFAQ)
            log.info("Total FAQs on page -> " + str(len(listedFAQ)))

        else:
            log.critical("FAQs are not present for the respective university")

        # opening all faqs

        for faq in listing.allFAQs():
            faq.click()
