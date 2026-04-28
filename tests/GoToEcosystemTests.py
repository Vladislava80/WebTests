from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper
import allure



BASE_URL = "https://ok.ru/"

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы ВК')
def test_open_vk_ecosystem(browser):
    base_page = BasePageHelper(browser)
    base_page.get_url(BASE_URL)
    base_page.check_page()
    login_page = LoginPageHelper(browser)
    current_window_id = login_page.get_window_id(0)
    login_page.click_vk_ecosystem()
    login_page.click_more_button()
    new_window_id = login_page.get_window_id(1)
    login_page.switch_window(new_window_id)
    vkecosystem_page = VKEcosystemPageHelper(browser)
    vkecosystem_page.switch_window(current_window_id)
    BasePageHelper(browser)