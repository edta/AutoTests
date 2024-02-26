from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.PERSONAL_DETAILS_PAGE

    SAVE_BUTTON = ('xpath', "//button[@type='submit']")
    FIRST_NAME_FIELD = ('xpath', "//input[@id='firstName']")
    SUCCESSFULLY_UPDATE_MESSAGE = ('xpath', "//div[@class='toast-message']")

    def change_name(self, new_name):
        with allure.step(f"Change name on {new_name}"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.clear()
            assert first_name_field.get_attribute('value') == "", "There is some text in first name field"
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def is_changes_saved(self):
        self.wait.until(EC.presence_of_element_located(self.SUCCESSFULLY_UPDATE_MESSAGE))