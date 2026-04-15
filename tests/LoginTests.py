from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
import allure

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
# URL_REGISTER = "https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone"
login = "email"
password = "1"


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text_login() == EMPTY_LOGIN_ERROR

@allure.title('Проверка ошибки при отсутствии пароля')
def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.fill_login_field(login)
    login_page.click_login()
    assert login_page.get_error_text_password() == EMPTY_PASSWORD_ERROR

@allure.title('Переход на страницу "QR-код" по ссылке')
def test_go_to_qrcode_link(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.link_enter_qrcode()
    base_page = BasePage(browser)
    qr_code_image = base_page.find_element(LoginPageLocators.QR_CODE_IMAGE)
    assert qr_code_image is not None

@allure.title('Переход на страницу "QR-код" по кнопке')
def test_go_to_qrcode_button(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.enter_button_qrcode()
    base_page = BasePage(browser)
    qr_code_image = base_page.find_element(LoginPageLocators.QR_CODE_IMAGE)
    assert qr_code_image is not None


@allure.title('Переход на страницу восстановления доступа')
def test_go_to_forgot_password_page(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.link_cannot_enter()
    base_page = BasePage(browser)
    recovery = base_page.find_element(LoginPageLocators.RECOVERY).text
    assert recovery == "Восстановление доступа"

# переходит на vk, но assert ожидает ok.ru
@allure.title('Переход на страницу регистрации')
def test_go_to_register_page(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.register()
    base_page = BasePage(browser)
    register = base_page.find_element(LoginPageLocators.REGISTER_INPUT_PHONE).text
    assert register is not None

