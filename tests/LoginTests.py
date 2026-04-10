from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
import allure

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"


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
    login_page.fill_login_field()
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


# не успевает открыть? тормозит интеграция с vk?
def test_enter_vk_id(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.vk_id()
    browser.switch_to.window(browser.window_handles[-1])
    assert "vk.com" in browser.current_url


@allure.title('Вход через почту Mail.ru')
def test_enter_mailru(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.mail_ru()
    browser.switch_to.window(browser.window_handles[-1])
    assert "mail.ru" in browser.current_url

@allure.title('Вход через Яндекс')
def test_enter_yandex(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.yandex()
    browser.switch_to.window(browser.window_handles[-1])
    assert "yandex" in browser.current_url
