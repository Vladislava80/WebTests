from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
from pages.RecoveryPage import RecoveryPageHelper, RecoveryPageLocators
import allure
import pytest

BASE_URL = "https://ok.ru/"
login = "email"
password = "1"

@pytest.mark.xfail
@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.fill_login_field(login)
    for i in range(3):
        login_page.fill_password_field(password)
        login_page.click_login()
    login_page.click_recovery()
    RecoveryPageHelper(BasePage)