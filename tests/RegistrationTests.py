from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper, LoginPageLocators
import allure
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = "https://ok.ru/"


@allure.suite('Проверка формы регистрации')
@allure.title('Проверка кода телефона при выборе страны')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.register()
    registration_page = RegistrationPageHelper(browser)
    selected_country_code = registration_page.select_random_country()
    actual_country_code = registration_page.get_phone_field_value()
    assert  actual_country_code == selected_country_code
