from selenium.webdriver.common.by import By


class RemittanceClass:
    def __init__(self, driver):
        self.driver = driver

    # ---------------------- selectors ---------------------------------------
    recipientInput_selector = (By.CSS_SELECTOR, "#email")
    recipientCountryText_selector = (
        By.XPATH,
        "(//div[@class='relative flex items-center cursor-pointer flag_countryFlag__nZR_S'])[1]",
    )
    youSendInput_selector = (
        By.XPATH,
        "(//span[@class='block text-theme-black-text'])[2]",
    )
    youSendCountryText_selector = (
        By.XPATH,
        "(//div[@class='relative flex items-center cursor-pointer flag_countryFlag__nZR_S'])[2]",
    )

    sendNowBtn_selector = (By.XPATH, "//div[text()='Send Now']")

    # ------------------------------------ step 2 selector -------------------------------

    selectproperty_selector = (By.XPATH, "//input[@placeholder='Select Property']")
    firstProperty_selector = (By.ID, "-item-0")
    wireTransfer_selector = (By.ID, "bankwire")
    agentAssisted_selector = (By.ID, "agentAssisted")
    continueBtn_selector = (By.XPATH, "//div[text()='Continue']")

    # --------------------------- detail validation elements ---------------------

    receivingAmount_selector = (
        By.XPATH,
        "//div[@class='relative md:flex text-right items-center flag_countryFlag__nZR_S']",
    )
    payingAmount_selector = (
        By.XPATH,
        "//div[@class='text-theme-blue flex flex-wrap text-right']",
    )
    fxRate_selector = (By.XPATH, "//p[@class='text-theme-blue']")
    thankYouOKbtn_selector = (By.XPATH, "//div[text()='OK']")

    # ------------------------ Methods ------------------------------------------

    def recipientInput(self):
        return self.driver.find_element(*RemittanceClass.recipientInput_selector)

    def youSendInput(self):
        return self.driver.find_element(*RemittanceClass.youSendInput_selector)

    def recipientCountryText(self):
        return self.driver.find_element(*RemittanceClass.recipientCountryText_selector)

    def youSendCountryText(self):
        return self.driver.find_element(*RemittanceClass.youSendCountryText_selector)

    def sendNowBtn(self):
        return self.driver.find_element(*RemittanceClass.sendNowBtn_selector)

    # --------------------- step 2 methods -----------------------------------------

    def selectProperty(self):
        return self.driver.find_element(*RemittanceClass.selectproperty_selector)

    def firstProperty(self):
        return self.driver.find_element(*RemittanceClass.firstProperty_selector)

    def wireTransfer(self):
        return self.driver.find_element(*RemittanceClass.wireTransfer_selector)

    def agentAssisted(self):
        return self.driver.find_element(*RemittanceClass.agentAssisted_selector)

    def continueBtn(self):
        return self.driver.find_element(*RemittanceClass.continueBtn_selector)

    # ----------------------------- detial validation methods -----------------------------

    def receivingAmount(self):
        return self.driver.find_element(*RemittanceClass.receivingAmount_selector)

    def amountNeedToPay(self):
        return self.driver.find_element(*RemittanceClass.payingAmount_selector)

    def fxRate(self):
        return self.driver.find_element(*RemittanceClass.fxRate_selector)

    def thankYouOKbtn(self):
        return self.driver.find_element(*RemittanceClass.thankYouOKbtn_selector)
