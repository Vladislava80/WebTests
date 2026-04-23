from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver import ActionChains


class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//span[@name="illustrations/ill_actual"]')
    REGISTRATION = (By.XPATH, '//span[@name="illustrations/ill_registration"]')
    MY_PROFILE = (By.XPATH, '//a[@href="/help/moi-profil"]')
    COMMUNICATION = (By.XPATH, '//span[@name="illustrations/ill_communication"]')
    PROFILE_ACCESS = (By.XPATH, '//a[@href="/help/dostup-k-profilu"]')
    SECURITY = (By.XPATH, '//span[@name="illustrations/ill_security"]')
    GROUPS = (By.XPATH, '//span[@name="illustrations/ill_group_group"]')
    PAID_OPTIONS = (By.XPATH, '//span[@name="illustrations/ill_paid_features"]')
    VIOLATION_SPAM = (By.XPATH, '//span[@name="illustrations/ill_violation_spam"]')
    GAMES_APPS = (By.XPATH, '//span[@name="illustrations/ill_app_game"]')
    OTHER_SERVICES = (By.XPATH, '//span[@name="illustrations/ill_other_services"]')
    USEFUL_INFORMATION = (By.XPATH, '//span[@name="illustrations/ill_useful_info"]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//span[@name="illustrations/ill_advertising_cabinet"]')



class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAID_OPTIONS)
        self.find_element(HelpPageLocators.VIOLATION_SPAM)
        self.find_element(HelpPageLocators.GAMES_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.USEFUL_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)


    @allure.step('Проматываем страницу до нужного элемента')
    def scrolltoitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()