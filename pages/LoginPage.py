from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    ENTER_BUTTON = (By.XPATH, '//button[@label="Войти"]')
    ENTER_QRCODE_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    # EYE_HIDE_PASSWORD = (By.XPATH, '//div/span[@class="vkuiFormField__after_vkuiInternalFormField__after"]')
    LINK_ENTER = (By.XPATH, '//a[@title="Вход"]')
    LINK_ENTER_QRCODE = (By.XPATH, '//a[@title="QR-код"]')
    LINK_CANNOT_ENTER = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER = (By.XPATH, '//button/span/span[text()="Зарегистрироваться"]')
    REGISTER_INPUT_PHONE = (By.XPATH, '//div[text()="Введите номер телефона"]')
    VK = (By.XPATH, '//a[@data-module="registration/vkconnect"]')
    MAILRU = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX = (By.XPATH, '//a[@data-provider="YANDEX"]')
    ERROR_LOGIN = (By.XPATH, '//div/span[text()="Введите логин"]')
    ERROR_PASSWORD = (By.XPATH, '//div/span[text()="Введите пароль"]')
    RECOVERY = (By.XPATH, "//div[text()='Восстановление доступа']")
    QR_CODE_IMAGE = (By.XPATH, "//div/img[@class ='qr_code_image']")


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        self.find_element(LoginPageLocators.ENTER_BUTTON)
        self.find_element(LoginPageLocators.ENTER_QRCODE_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        # self.find_element(LoginPageLocators.EYE_HIDE_PASSWORD)
        self.find_element(LoginPageLocators.LINK_ENTER)
        self.find_element(LoginPageLocators.LINK_ENTER_QRCODE)
        self.find_element(LoginPageLocators.LINK_CANNOT_ENTER)
        self.find_element(LoginPageLocators.REGISTER)
        self.find_element(LoginPageLocators.VK)
        self.find_element(LoginPageLocators.MAILRU)
        self.find_element(LoginPageLocators.YANDEX)


    @allure.step('Нажимаем на кнопку"Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()

    @allure.step('Переходим по ссылке "QR-код"')
    def link_enter_qrcode(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LINK_ENTER_QRCODE).click()

    @allure.step('Заполняем поле логина')
    def fill_login_field(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("Romashka")

    @allure.step('Получаем текст ошибки')
    def get_error_text_login(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_LOGIN).text

    @allure.step('Получаем текст ошибки')
    def get_error_text_password(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_PASSWORD).text

    @allure.step('Нажимаем на кнопку "Войти по QR-коду"')
    def enter_button_qrcode(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.ENTER_QRCODE_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Не получается войти?"')
    def link_cannot_enter(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LINK_CANNOT_ENTER).click()

    @allure.step('Нажимаем на кнопку "Зарегистрироваться"')
    def register(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER).click()
        self.driver.get("https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone")





