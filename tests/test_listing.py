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
import pytest
from selenium.webdriver.common.alert import Alert
import re


class Test_lising(Invokation):
    @mark.testomatio("@T51683ec0")
    def test_listing_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        homepageObj = Homepageclass(self.driver)
        listing = listingClass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        loginEmail = "harsh.sachan@universityliving.com"
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except Exception:
            pass
        cityKey = "birmingham"
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

        # --------------------------------------- property stay count of PBSA ---------------------------------------

        listing.pbsaBtn().click()  # click on PBSA.
        time.sleep(2)
        pbsaStayText = listing.placesToStayCount().text
        pbsaStayCount = int("".join(re.findall("\\d", pbsaStayText)))
        log.info(pbsaStayCount)  # logging the PBSA stay count.

        # -------------------------------------- property stay count of HMO ---------------------------------------

        listing.hmoBtn().click()  # click on HMO
        time.sleep(2)
        hmoStayText = listing.placesToStayCount().text
        hmoStayCount = int("".join(re.findall("\\d", hmoStayText)))
        log.info(hmoStayCount)  # logging the HMO stay count.

        # ----------------------------------------- calculating the total stay count ( PBSA stay count + HMO stay count )----------------------------------------

        totalStayCount = pbsaStayCount + hmoStayCount
        log.info(
            "total stay count --> " + str(totalStayCount)
        )  # logging the total stay count of PBSA and HMO

        # ------------------------------------- calculating the total card count of PBSA and HMO ----------------------------------------------------------

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

        # ------------------------------- validating the stay count and total property count.

        if totalCardCountPbsa == pbsaStayCount and totalCardCountHmo == hmoStayCount:
            log.info("stay count and property card count are same")
        else:
            log.critical("stay count and property card count are not equal plz check")

        # ---------------------------------- Distance filter validations ---------------------------------.

        listing.pbsaBtn().click()  # clicking on PBSA btn
        listing.filterByBtn().click().click()  # opne filters
        listing.filterShowResultBtn().click  # clickin on show result button so to get all the pre-applied filters

        for (
            clsoeBtn
        ) in listing.filterPillClose():  # removing all the pre-applied filters
            clsoeBtn.click()

        # applying the distance filter only.
        listing.filterByBtn().click()
        listing.filterDistanceBtn().click()
        listing.filterShowResultBtn().click()

        distanceList = []
        for distances in listing.propertyDistances():
            distanceList.append(distances.text)

        log.info("%s", distanceList)
