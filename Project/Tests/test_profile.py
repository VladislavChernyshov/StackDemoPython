from Project.Pages.homepage import HomePage
from Project.Pages.profile import TestProfile


class TestProfileLogin:

    def test_login_profile(self, driver):
        homepage = HomePage(driver, 'https://stackoverflow.com')
        homepage.open()
        homepage.UserLogin()
        print(homepage.Resilt_login())
        result = homepage.Resilt_login()
        assert result == homepage.Resilt_login()


class TestProfileOpen:

    def test_profile_open(self, driver):
        profile_page = TestProfile(driver, 'https://stackoverflow.com')
        profile_page.open()
        profile_page.OpenProfile()
        print(profile_page.resilt_profile_page())
        result = profile_page.resilt_profile_page()
        assert result == profile_page.resilt_profile_page()


class TestProfileEdit:

    def test_profile_edit(self, driver):
        profile_page = TestProfile(driver, 'https://stackoverflow.com')
        profile_page.open()
        profile_page.OpenProfile()
        profile_page.EditProfile()




