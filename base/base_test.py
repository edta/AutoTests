import pytest

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.dashboard_page import DashboardPage
from pages.personal_details_page import PersonalDetailsPage
from config.data import Data


class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: ProfilePage
    personal_details_page: PersonalDetailsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = ProfilePage(driver)
        request.cls.personal_details_page = PersonalDetailsPage(driver)
