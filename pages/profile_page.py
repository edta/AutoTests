from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProfilePage(BasePage):
    PAGE_URL = Links.PROFILE_PAGE

    PERSONAL_DETAILS_BUTTON = ('xpath', "(//a[@data-automation-id='menu_employee_profile_PersonalDetails'])[1]")

    @allure.step("Open Personal detail tab")
    def open_personal_detail_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.PERSONAL_DETAILS_BUTTON)).click()


