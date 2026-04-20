from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure, random


# страница регистрации https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone

class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    # кнопка регистрации, кнопка "далее"
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//a[@data-l="t,support"]')


class RegistrationPageHelper(BasePage):
        def __init__(self, driver):
            self.driver = driver
            self.check_page()
        # проверяем только те локаторы, что видны при открытии страницы
        def check_page(self):
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

        @allure.step('Выбираем произвольную страну из списка')
        def select_random_country(self):
            random_number = random.randint(0, 212)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
            self.attach_screenshot()
            country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
            country_code = country_items[random_number].get_attribute("text")
            country_items[random_number].click()
            self.attach_screenshot()
            return country_code

        @allure.step('Считываем код выбранной страны')
        def get_phone_field_value(self):
            self.attach_screenshot()
            return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute("value")

