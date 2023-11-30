from selenium.webdriver.common.by import By


class BankAccountClass:
    def __init__(self, driver):
        self.driver = driver

    # ---------------------- selectors ---------------------------------------
    openAccBtn_selector = (By.XPATH, "//div[text()='Open Account']")
    formSubmitBtn_selector = (By.XPATH, "//div[text()='Submit']")
    irelandBankPopup_selector = (
        By.XPATH,
        "//div[@class='border-0 p-3 md:p-6 rounded-xl shadow-xl flex flex-col w-full bg-white focus:outline-none bg-white max-h-[80vh] overflow-y-auto']",
    )

    # ------------------------ Methods ------------------------------------------

    def openAccountBtn(self):
        return self.driver.find_element(*BankAccountClass.openAccBtn_selector)

    def formSubmitBtn(self):
        return self.driver.find_element(*BankAccountClass.formSubmitBtn_selector)

    def irelandPopup(self):
        return self.driver.find_element(*BankAccountClass.irelandBankPopup_selector)
