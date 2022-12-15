import time
from selenium.webdriver.common.by import By
import random
from Project.Locators.base import Base
from Project.Locators.locator import Login_page_Locators
from Project.Locators.locator import Cookies
from Project.Locators.locator import Profile


class TestProfile(Base):

    def OpenProfile(self):
        Email_Stack = "eld.rus@rambler.ru"
        Pass_Stack = "AAAqqq111"
        self.element_is_visible(Login_page_Locators.LOGIN_LINK).click()
        self.element_is_visible(Cookies.ACCEPT_COOKIES).click()
        self.element_is_visible(Login_page_Locators.USER_EMAIL).send_keys(Email_Stack)
        self.element_is_visible(Login_page_Locators.USER_PASSWORD).send_keys(Pass_Stack)
        self.element_is_visible(Login_page_Locators.BTN_SIGN_IN).click()
        self.element_is_visible(Profile.PROFILE_AVATAR).click()

    def resilt_profile_page(self):
        result = self.element_is_present(Profile.WELCOME_TEXT_PROFILE).text
        return result

    def EditProfile(self):
        num = random.random()
        self.element_is_visible(Profile.EDIT_PROFILE_BTN).click()
        self.element_is_visible(Profile.PROFILE_DISPLAY_NAME).send_keys("AutoTest")
        self.element_is_visible(Profile.PROFILE_LOCATION).send_keys("Selenium")
        self.element_is_visible(Profile.PROFILE_TITLE).send_keys("Write Selenium test")
        self.element_is_visible(Profile.PROFILE_ABOUT_ME).send_keys("About me testcase")
        self.element_is_visible(Profile.PROFILE_WEB_SITE_LINK).send_keys("google.com")
        self.element_is_visible(Profile.PROFILE_FULL_NAME).send_keys("Auto Test Selenium Python")
        self.element_is_visible(Profile.PROFILE_SAVE_BUTTON).click()