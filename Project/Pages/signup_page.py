import time

from selenium.webdriver.common.by import By

from Project.Locators.base import Base
from Project.Locators.locator import Login_page_Locators
from Project.Locators.locator import Cookies


class SignUp_page(Base):

    def UserSignUp(self):
        Email_Stack = "eld.rus@rambler.ru"
        Pass_Stack = "AAAqqq111"
        self.element_is_visible(Login_page_Locators.LOGIN_LINK).click()
        self.element_is_visible(Cookies.ACCEPT_COOKIES).click()
        self.element_is_visible(Login_page_Locators.USER_EMAIL).send_keys(Email_Stack)
        self.element_is_visible(Login_page_Locators.USER_PASSWORD).send_keys(Pass_Stack)
        self.element_is_visible(Login_page_Locators.BTN_SIGN_IN).click()
        time.sleep(3)

    def Resilt_login(self):
        result = self.element_is_present(Login_page_Locators.Welcome_page).text

        return result