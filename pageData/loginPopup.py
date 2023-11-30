from selenium.webdriver.common.by import By
import string
import random
from invokeBaseClass import Invokation


class loginpopupClass:
    def __init__(self, driver):
        self.driver = driver

    N = 7
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    phone_number = "".join([str(random.randint(0, 9)) for i in range(10)])
    newEmail = res + ".university@yopmail.com"

    emailfieldSelector = (By.ID, "email")
    emailfieldSelector_usingPlaceholder = (
        By.XPATH,
        "//input[@placeholder='Enter Email']",
    )
    loginBtnSelector = (By.XPATH, "//div[text()='Login']")
    otp1Selector = (By.NAME, "otp0")
    otp2Selector = (By.NAME, "otp1")
    otp3Selector = (By.NAME, "otp2")
    otp4Selector = (By.NAME, "otp3")
    otp5Selector = (By.NAME, "otp4")
    continueBtnSelector = (By.XPATH, "//div[text()='Continue']")
    profileiconSelector = (By.XPATH, "//a[@href='/dashboard?tab=booking']")
    dashboardemailSelector = (
        By.XPATH,
        "(//p[text()='harsh.sachan@universityliving.com'])",
    )
    profilesectionSelector = (By.XPATH, "(//img[@alt='Profile'])")
    profileemailSelector = (
        By.XPATH,
        "(//p[text()='harsh.sachan@universityliving.com'])[2]",
    )
    continueWithGoogleSelector = (By.XPATH, "//img[@alt='SignUp with Google']")
    googleLoginIDselector = (
        By.XPATH,
        "//div[text()='harsh.sachan@universityliving.com']",
    )

    firstnameSelector = (By.NAME, "firstName")
    lastnameSelector = (By.NAME, "lastName")
    PhoneNumberSelector = (By.ID, "contactNumber")
    signUpBtnSelector = (By.XPATH, "//div[text()='Sign Up']")
    PopUpTitleSelector = (By.XPATH, "//p[text()='Welcome to University Living']")

    # ------------------------------- Dashboard selectors -------------------------------

    wishlistSection_selector = (By.XPATH, "//p[text()='Wishlist']")
    wishlistPropertyName_selector = (
        By.XPATH,
        "//div[@class='w-full bg-white rounded-b-md p-3']/div[1]/a/p",
    )

    def emailfield(self):
        return self.driver.find_element(*loginpopupClass.emailfieldSelector)

    def emailfield_using_placeholder(self):
        return self.driver.find_element(
            *loginpopupClass.emailfieldSelector_usingPlaceholder
        )

    def loginBtn(self):
        return self.driver.find_element(*loginpopupClass.loginBtnSelector)

    def otpFirst(self):
        return self.driver.find_element(*loginpopupClass.otp1Selector)

    def otpsecond(self):
        return self.driver.find_element(*loginpopupClass.otp2Selector)

    def otpthird(self):
        return self.driver.find_element(*loginpopupClass.otp3Selector)

    def otpfourth(self):
        return self.driver.find_element(*loginpopupClass.otp4Selector)

    def otpfifth(self):
        return self.driver.find_element(*loginpopupClass.otp5Selector)

    def continueBtn(self):
        return self.driver.find_element(*loginpopupClass.continueBtnSelector)

    def profileIcon(self):
        return self.driver.find_element(*loginpopupClass.profileiconSelector)

    def dashboardEmail(self):
        return self.driver.find_element(*loginpopupClass.dashboardemailSelector)

    def profileSection(self):
        return self.driver.find_element(*loginpopupClass.profilesectionSelector)

    def profileEmail(self):
        return self.driver.find_element(*loginpopupClass.profileemailSelector)

    def continueWithGoogleBtn(self):
        return self.driver.find_element(*loginpopupClass.continueWithGoogleSelector)

    def LogingoogleID(self):
        return self.driver.find_element(*loginpopupClass.googleLoginIDselector)

    def firstName(self):
        return self.driver.find_element(*loginpopupClass.firstnameSelector)

    def lastName(self):
        return self.driver.find_element(*loginpopupClass.lastnameSelector)

    def phoneNumber(self):
        return self.driver.find_element(*loginpopupClass.PhoneNumberSelector)

    def signUpBtn(self):
        return self.driver.find_element(*loginpopupClass.signUpBtnSelector)

    def popUpTitle(self):
        return self.driver.find_element(*loginpopupClass.PopUpTitleSelector)

    # ---------------------------- dashboard elements ------------------------------

    def wishListSection(self):
        return self.driver.find_element(*loginpopupClass.wishlistSection_selector)

    def wishListPropertyNames(self):
        return self.driver.find_elements(*loginpopupClass.wishlistPropertyName_selector)

    # --------------------------------- login method --------------------------------

    def loginMethod(self):
        self.driver.find_element(*loginpopupClass.emailfieldSelector).send_keys(
            "harsh.sachan@universityliving.com"
        )
        self.driver.find_element(*loginpopupClass.loginBtnSelector).click()
        self.driver.find_element(*loginpopupClass.otp1Selector).send_keys(1)
        self.driver.find_element(*loginpopupClass.otp2Selector).send_keys(2)
        self.driver.find_element(*loginpopupClass.otp3Selector).send_keys(3)
        self.driver.find_element(*loginpopupClass.otp4Selector).send_keys(4)
        self.driver.find_element(*loginpopupClass.otp5Selector).send_keys(5)
        self.driver.find_element(*loginpopupClass.continueBtnSelector).click()

    # -------------------------------------- sign up method ----------------------------------

    def signUPMethod(self):
        res = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        new_email = res + ".university@yopmail.com"
        new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
        testing_key = "test"

        self.driver.find_element(*loginpopupClass.emailfieldSelector).send_keys(
            new_email
        )

        self.driver.find_element(*loginpopupClass.loginBtnSelector).click()

        self.driver.find_element(*loginpopupClass.firstnameSelector).send_keys(
            testing_key
        )
        self.driver.find_element(*loginpopupClass.lastnameSelector).send_keys(
            testing_key
        )
        self.driver.find_element(*loginpopupClass.PhoneNumberSelector).send_keys(
            new_phoneNumber
        )
        self.driver.find_element(*loginpopupClass.signUpBtnSelector).click()
        self.driver.find_element(*loginpopupClass.otp1Selector).send_keys(1)
        self.driver.find_element(*loginpopupClass.otp2Selector).send_keys(2)
        self.driver.find_element(*loginpopupClass.otp3Selector).send_keys(3)
        self.driver.find_element(*loginpopupClass.otp4Selector).send_keys(4)
        self.driver.find_element(*loginpopupClass.otp5Selector).send_keys(5)
        self.driver.find_element(*loginpopupClass.continueBtnSelector).click()

    # ----------------------------------------  login method using name ---------------------------

    def loginMethodUsingPlaceholder(self):
        self.driver.find_element(
            *loginpopupClass.emailfieldSelector_usingPlaceholder
        ).send_keys("harsh.sachan@universityliving.com")
        self.driver.find_element(*loginpopupClass.loginBtnSelector).click()
        self.driver.find_element(*loginpopupClass.otp1Selector).send_keys(1)
        self.driver.find_element(*loginpopupClass.otp2Selector).send_keys(2)
        self.driver.find_element(*loginpopupClass.otp3Selector).send_keys(3)
        self.driver.find_element(*loginpopupClass.otp4Selector).send_keys(4)
        self.driver.find_element(*loginpopupClass.otp5Selector).send_keys(5)
        self.driver.find_element(*loginpopupClass.continueBtnSelector).click()
