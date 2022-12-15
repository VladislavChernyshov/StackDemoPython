from Project.Pages.homepage import HomePage


class TestHomepage:

    def test_homepage(self, driver):
        homepage = HomePage(driver, 'https://stackoverflow.com')
        homepage.open()
        homepage.UserLogin()
        print(homepage.Resilt_login())
        result = homepage.Resilt_login()
        assert result == homepage.Resilt_login()