from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper
import allure


BASE_URL = "https://ok.ru/help"


@allure.suite('Проверка страницы помощи')
@allure.title('Переход в рекламый кабинет со страницы помощи')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    help_page = HelpPageHelper(browser)
    help_page.scrolltoitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)