from selenium.webdriver.common.by import By


class GetVisaClass:
    def __init__(self, driver):
        self.driver = driver

    # ---------------------- selectors ---------------------------------------

    firstName_selector = (By.NAME, "firstName")
    lastName_selector = (By.NAME, "lastName")
    email_selector = (By.NAME, "email")
    phoneNumber_selector = (By.ID, "contactNo")
    submitBtn_selector = (By.XPATH, "//div[text()='Submit']")

    # ------------------- error message selector --------------------------------

    firstNameError_selector = (By.XPATH, "//p[text()='Please enter your first name']")
    lastNameError_selector = (By.XPATH, "//p[text()='Please enter your last name']")
    emailError_selector = (By.XPATH, "//p[text()='Please enter your email address']")
    phoneNumberError_selector = (
        By.XPATH,
        "//p[text()='Please enter your Phone number']",
    )

    okBtn_selector = (By.XPATH, "//div[text()='OK']")

    # ------------------------ Methods ------------------------------------------

    def firstName(self):
        return self.driver.find_element(*GetVisaClass.firstName_selector)

    def lastName(self):
        return self.driver.find_element(*GetVisaClass.lastName_selector)

    def email(self):
        return self.driver.find_element(*GetVisaClass.email_selector)

    def phoneNumber(self):
        return self.driver.find_element(*GetVisaClass.phoneNumber_selector)

    def submitBtn(self):
        return self.driver.find_element(*GetVisaClass.submitBtn_selector)

    # ----------------------------------- error message methods -----------------------------

    def firstNameError(self):
        return self.driver.find_element(*GetVisaClass.firstNameError_selector)

    def lastNameError(self):
        return self.driver.find_element(*GetVisaClass.lastNameError_selector)

    def emailError(self):
        return self.driver.find_element(*GetVisaClass.emailError_selector)

    def phoneNumberError(self):
        return self.driver.find_element(*GetVisaClass.phoneNumberError_selector)

    def okBtn(self):
        return self.driver.find_element(*GetVisaClass.okBtn_selector)
