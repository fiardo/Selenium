from selenium.webdriver.common.by import By


class StudentFinancingClass:
    def __init__(self, driver):
        self.driver = driver

    # ---------------------- selectors ---------------------------------------
    submitBtn_selector = (By.XPATH, "//div[text()='Submit']")
    firstNameError_selector = (By.XPATH, "//p[text()='Please enter your first name']")
    lastNameError_selector = (By.XPATH, "//p[text()='Please enter your last name']")
    emailError_selector = (By.XPATH, "//p[text()='Please enter your email address']")
    phoneError_selector = (By.XPATH, "//p[text()='Please enter your Phone number']")

    firstName_selector = (By.NAME, "firstName")
    lastName_selector = (By.NAME, "lastName")
    email_selector = (By.NAME, "email")
    phoneNumber_selector = (By.ID, "contactNo")
    countryDropdown_selector = (By.NAME, "country")
    providerDropDown_selector = (By.NAME, "provider")
    okBtn_selector = (By.XPATH, "//div[text()='OK']")

    # ------------------------ error Methods ------------------------------------------
    def submitBtn(self):
        return self.driver.find_element(*StudentFinancingClass.submitBtn_selector)

    def firstNameError(self):
        return self.driver.find_element(*StudentFinancingClass.firstNameError_selector)

    def lastNameError(self):
        return self.driver.find_element(*StudentFinancingClass.lastNameError_selector)

    def emailError(self):
        return self.driver.find_element(*StudentFinancingClass.emailError_selector)

    def phoneNumberError(self):
        return self.driver.find_element(*StudentFinancingClass.phoneError_selector)

    # --------------------- field methods ----------------------

    def firstName(self):
        return self.driver.find_element(*StudentFinancingClass.firstName_selector)

    def lastName(self):
        return self.driver.find_element(*StudentFinancingClass.lastName_selector)

    def email(self):
        return self.driver.find_element(*StudentFinancingClass.email_selector)

    def phoneNumber(self):
        return self.driver.find_element(*StudentFinancingClass.phoneNumber_selector)

    def country(self):
        return self.driver.find_element(*StudentFinancingClass.countryDropdown_selector)

    def provider(self):
        return self.driver.find_element(
            *StudentFinancingClass.providerDropDown_selector
        )

    def okBtn(self):
        return self.driver.find_element(*StudentFinancingClass.okBtn_selector)
