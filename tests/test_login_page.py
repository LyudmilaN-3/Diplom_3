import allure

from ..constants import Constant
from ..pages.login_page import LoginPage


class TestLoginPage:

    @allure.title('Проверка возможности перехода на страницу восстановления пароля')
    def test_get_recov_password_page_by_button_success(self, driver):
        login_page = LoginPage(driver)
        # Открыть главную страницу сайта
        login_page.go_to_site()
        # Кликнуть по кнопке "Личный кабинет" на хедере
        login_page.get_login_page_by_button_on_main_page()
        # Перейти на страницу авторизации и кликнуть по ссылке "Восстановить пароль"
        login_page.get_request_recov_password_page_by_button()
        # Перейти на страницу запроса восстановления пароля и получить её название
        text = login_page.get_title_of_current_page()
        assert text == Constant.TEXT_LINK_RECOV_PASSWORD

    @allure.title('Проверка возможности клика по кнопке "Восстановить" на странице запроса восстановления пароля')
    def test_click_on_button(self, driver, email=Constant.TEST_EMAIL):
        login_page = LoginPage(driver)
        # Открыть главную страницу сайта
        login_page.go_to_site()
        # Перейти на страницу восстановления пароля
        login_page.get_recov_password_page(email)
        assert login_page.get_button_save()

    @allure.title('Проверка подсветки поля ввода "Пароль"')
    def test_active_field(self, driver, email=Constant.TEST_EMAIL):
        login_page = LoginPage(driver)
        # Открыть главную страницу сайта
        login_page.go_to_site()
        # Перейти на страницу восстановления пароля
        login_page.get_recov_password_page(email)
        # Кликнуть по кнопке "Скрыть/Показать пароль"
        login_page.click_button_hide_show_password()
        # Получить аттрибут class поля "Пароль"
        class_text = login_page.get_class_of_field_password()
        assert Constant.PART_CLASS_TEXT_FIELD_PASSWORD in class_text
