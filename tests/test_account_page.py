import allure

from ..constants import Constant
from ..pages.account_page import AccountPage


class TestAccountPage:

    @allure.title('Проверка возможности перехода в личный кабинет')
    def test_get_profile_page_by_button_success(self, driver):
        account_page = AccountPage(driver)
        # Открыть главную страницу сайта
        account_page.go_to_site()
        # Зайти на сайт под залогиненным пользователем
        account_page.get_site_as_login_user()
        # Перейти в личный кабинет кликом по кнопке на хедере
        account_page.get_profile_page()
        # Получить текущий url
        current_url = account_page.get_current_url_account()
        assert Constant.PROFILE_PATH_URL in current_url

    @allure.title('Проверка возможности перехода в раздел "История заказов"')
    def test_move_to_order_history_page(self, driver):
        account_page = AccountPage(driver)
        # Открыть главную страницу сайта
        account_page.go_to_site()
        # Зайти на сайт под залогиненным пользователем
        account_page.get_site_as_login_user()
        # Перейти в личный кабинет кликом по кнопке на хедере
        account_page.get_profile_page()
        # Перейти в раздел "История заказов" личного кабинета
        account_page.move_to_order_history_page()
        # Получить текущий url
        current_url = account_page.get_current_url_history_orders()
        assert Constant.HISTORY_PATH_URL in current_url

    @allure.title('Проверка возможности выйти из аккаунта')
    def test_logout_by_button(self, driver):
        account_page = AccountPage(driver)
        # Открыть главную страницу сайта
        account_page.go_to_site()
        # Зайти на сайт под залогиненным пользователем
        account_page.get_site_as_login_user()
        # Перейти в личный кабинет кликом по кнопке на хедере
        account_page.get_profile_page()
        # Выйти из аккаунта кликом по кнопке "Выход"
        account_page.logout()
        # Получить текущий url
        current_url = account_page.get_current_url_main_page()
        assert Constant.PART_PATH_URL not in current_url
