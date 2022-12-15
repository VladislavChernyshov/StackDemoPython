from selenium.webdriver.common.by import By


class Cookies():

    ACCEPT_COOKIES = (By.XPATH, "/html/body/div[4]/div/button[1]")


class Login_page_Locators():

    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    USER_EMAIL = (By.ID, "email")
    USER_PASSWORD = (By.ID, "password")
    BTN_SIGN_IN = (By.ID, "submit-button")
    Welcome_page = (By.XPATH, "//h1[normalize-space()='Top Questions']")


class Signin_page_Locators():

    SIGN_UP_DISPLAY_NAME = (By.ID, "display-name")
    SIGN_UP__EMAIL = (By.ID, "email")
    SIGN_UP_PASSWORD = (By.ID, "password")
    SIGN_UP_BTN = (By.ID, "submit-button")


class Profile():

    PROFILE_AVATAR = (By.XPATH, "/html/body/header/div/nav/ol/li[2]/a/div[1]")
    WELCOME_TEXT_PROFILE = (By.XPATH, "//*[@id='mainbar-full']/div[1]/div[1]/div/div/div[1]")
    EDIT_PROFILE_BTN = (By.XPATH, "//*[@id='mainbar-full']/div[1]/div[2]/a")
    PROFILE_DISPLAY_NAME = (By.ID, "displayName")
    PROFILE_LOCATION = (By.ID, "location")
    PROFILE_TITLE = (By.ID, "Title")
    PROFILE_ABOUT_ME = (By.ID, "wmd-input")
    PROFILE_WEB_SITE_LINK = (By.ID, "WebsiteUrl")
    PROFILE_TWITTER_LINK = (By.ID, "TwitterUrl")
    PROFILE_GIT_HUB = (By.ID, "GitHubUrl")
    PROFILE_FULL_NAME = (By.ID, "RealName")
    PROFILE_SAVE_BUTTON = (By.XPATH, "//*[@id='form-submit']/div/button")
    PROFILE_CANCEL_BUTTON = (By.ID, "cancel")

