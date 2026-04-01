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


class LoginPageHelper(BasePage):
