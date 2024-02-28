import allure

from ..locators.account_page_locators import AccountPageLocator as AccounPL
from ..locators.login_page_locators import LoginPageLocator as LoginPL
from ..locators.main_page_locators import MainPageLocator as MainPL
from ..pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Зайти на сайт под залогиненным пользователем')
    def get_site_as_login_user(
            self,
            email,
            password,
            locator1=MainPL.BUTTON_ACC,
            locator2=LoginPL.EMAIL_FIELD,
            locator3=LoginPL.PASSWORD_FIELD,
            locator4=LoginPL.BUTTON_INTO
    ):
        self.get_login_page_by_button_on_header(locator1)
        self.fill_email_password_fields(locator2, locator3, email, password)
        self.get_main_page_as_login_user(locator4)

    @allure.step('Перейти в личный кабинет кликом по кнопке на хедере')
    def get_profile_page(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_ACC)

    @allure.step('Перейти в раздел "История заказов" личного кабинета')
    def move_to_order_history_page(self):
        self.find_element_by_locator_and_click(AccounPL.BUTTON_HISTORY)

    @allure.step('Выйти из аккаунта кликом по кнопке "Выход"')
    def logout(self):
        self.find_element_by_locator_and_click(AccounPL.BUTTON_LOG_OUT)

    @allure.step('Получить текущий url личного кабинета')
    def get_current_url_account(self):
        current_url = self.get_url(AccounPL.BUTTON_PROFILE)
        return current_url

    @allure.step('Получить текущий url истории заказов')
    def get_current_url_history_orders(self):
        current_url = self.get_url(AccounPL.NUMBER_ORDER_IN_HISTORY)
        return current_url

    @allure.step('Получить текущий url главной страницы')
    def get_current_url_main_page(self):
        current_url = self.get_url(LoginPL.BUTTON_INTO)
        return current_url
