from selenium.webdriver.common.by import By


class GuarantorClass:
    def __init__(self, driver):
        self.driver = driver

    # ---------------------- selectors ---------------------------------------
    findGuarantorBtn_selector = (By.XPATH, "//div[text()='Find A Guarantor']")
    formSubmitBtn_selector = (By.XPATH, "//div[text()='Submit']")

    # ------------------------ Methods ------------------------------------------

    def findGuarantorBtn(self):
        return self.driver.find_element(*GuarantorClass.findGuarantorBtn_selector)

    def formSubmitBtn(self):
        return self.driver.find_element(*GuarantorClass.formSubmitBtn_selector)
