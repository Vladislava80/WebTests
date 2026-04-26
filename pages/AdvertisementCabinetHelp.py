from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class AdvertisementCabinetHelpLocators:
    TITLE_AD_CAB = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class AdvertisementCabinetHelpHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisementCabinetHelpLocators.TITLE_AD_CAB)