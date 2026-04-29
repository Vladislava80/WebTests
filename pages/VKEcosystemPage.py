from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class VKEcosystemPageLocators:
    VKLOGO = (By.ID, 'header-logo')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.VKLOGO)