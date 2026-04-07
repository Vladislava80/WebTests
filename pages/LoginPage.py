from BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_BUTTON = (By.XPATH, '//button[@label="Войти"]')
    ENTER_QRCODE_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    EYE_HIDE_PASSWORD = (By.XPATH, '//button/span[text()="Показать пароль"]')
    LINK_ENTER = (By.XPATH, '//a[@title="Вход"]')
    LINK_ENTER_QRCODE = (By.XPATH, '//a[@title="QR-код"]')
    LINK_CANNOT_ENTER = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER = (By.XPATH, '//button/span/span[text()="Зарегистрироваться"]')
    REGISTER_VK = (By.XPATH, '//a[@data-module="registration/vkconnect"]')
    REGISTER_MAILRU = (By.XPATH, '//a[@data-l="t,mailru"]')
    REGISTER_YANDEX = (By.XPATH, '//a[@data-provider="YANDEX"]')
    ERROR_LOGIN = (By.XPATH, '//div/span[text()="Введите логин"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        self.find_element(LoginPageLocators.ENTER_BUTTON)
        self.find_element(LoginPageLocators.ENTER_QRCODE_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.EYE_HIDE_PASSWORD)
        self.find_element(LoginPageLocators.LINK_ENTER)
        self.find_element(LoginPageLocators.LINK_ENTER_QRCODE)
        self.find_element(LoginPageLocators.LINK_CANNOT_ENTER)
        self.find_element(LoginPageLocators.REGISTER)
        self.find_element(LoginPageLocators.REGISTER_VK)
        self.find_element(LoginPageLocators.REGISTER_MAILRU)
        self.find_element(LoginPageLocators.REGISTER_YANDEX)


    def click_login(self):
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()


    def fill_login_field(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("Romashka")


    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_LOGIN).text
