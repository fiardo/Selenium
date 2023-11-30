from selenium.webdriver.common.by import By


class FlightTicketClass:
    def __init__(self, driver):
        self.driver = driver

    oneWay_selector = (By.XPATH, "//p[text()='One Way']")
    roundTrip_selector = (By.XPATH, "//p[text()='Round Trip']")
    # ----------------------- deatils selectors------------------------------

    toDestination_selector = (By.XPATH, "(//p[text()='-----'])[1]")
    returnDate_selector = (By.XPATH, "//p[text()='Select your return date']")
    toCitySearchBar_selector = (By.XPATH, "//input[@placeholder='Search by']")
    toCitySearchDublin_selector = (By.XPATH, "(//p[text()='Dublin'])[1]")
    lastDate_selector = (By.XPATH, "(//td[text()='30'])[2]")
    travellerAndClass_selector = (By.ID, "TravelClass")
    travelSeat_selector = (By.XPATH, "//p[text()='2']")
    searchFlightsBtn_selector = (By.XPATH, "//div[text()='Search Flights']")

    # ----------------------- form fields selector ----------------------------------

    submitBtn_selector = (By.XPATH, "//div[text()='Submit']")

    # ------------------------------------- Methods ------------------------------------

    def oneWay(self):
        return self.driver.find_element(*FlightTicketClass.oneWay_selector)

    def roundTrip(self):
        return self.driver.find_element(*FlightTicketClass.roundTrip_selector)

    # -------------------------------- details methods ------------------------------

    def toDestination(self):
        return self.driver.find_element(*FlightTicketClass.toDestination_selector)

    def returnDate(self):
        return self.driver.find_element(*FlightTicketClass.returnDate_selector)

    def toCitySearchBar(self):
        return self.driver.find_element(*FlightTicketClass.toCitySearchBar_selector)

    def toCitySearchDublin(self):
        return self.driver.find_element(*FlightTicketClass.toCitySearchDublin_selector)

    def lastDate(self):
        return self.driver.find_element(*FlightTicketClass.lastDate_selector)

    def travellerAndClass(self):
        return self.driver.find_element(*FlightTicketClass.travellerAndClass_selector)

    def travelSeat(self):
        return self.driver.find_element(*FlightTicketClass.travelSeat_selector)

    def searchFlightsBtn(self):
        return self.driver.find_element(*FlightTicketClass.searchFlightsBtn_selector)

    # ---------------- form methods ---------------------------------------

    def submitBtn(self):
        return self.driver.find_element(*FlightTicketClass.submitBtn_selector)
