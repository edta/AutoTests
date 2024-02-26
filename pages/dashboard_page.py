from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ('xpath', "//a[@data-automation-id='menu_pim_viewMyDetails']")

    @allure.step("Click on 'My info' link")
    def click_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()