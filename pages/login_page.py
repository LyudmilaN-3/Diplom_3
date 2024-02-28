import allure

from ..locators.login_page_locators import LoginPageLocator as LoginPL
from ..locators.main_page_locators import MainPageLocator as MainPL
from ..pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Перейти на страницу входа в аккаунт по кнопке "Личный кабинет" на хедере')
    def get_login_page_by_button_on_main_page(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_ACC)

    @allure.step('Перейти на страницу запроса восстановления пароля по кнопке "Восстановить пароль"')
    def get_request_recov_password_page_by_button(self):
        self.find_element_by_locator_and_click(LoginPL.LINK_RECOV_PASS)

    @allure.step('Ввести почту в поле ввода "Email" на странице запроса восстановления пароля')
    def set_email(self, email):
        self.find_element_by_locator_and_send_keys(LoginPL.EMAIL_FIELD_RECOV, email)

    @allure.step('Перейти на страницу восстановления пароля по кнопке "Восстановить"')
    def get_recov_password_page_by_button(self):
        self.find_element_by_locator_and_click(LoginPL.BUTTON_RECOVER)

    @allure.step('Ввести пароль в поле "Пароль" на странице восстановления пароля')
    def set_password(self, password):
        self.find_element_by_locator_and_send_keys(LoginPL.PASSWORD_FIELD_RECOV, password)

    @allure.step('Кликнуть по кнопке "Скрыть/Показать пароль"')
    def click_button_hide_show_password(self):
        self.find_element_by_locator_and_click(LoginPL.BUTTON_HIDE_SHOW_PASS)

    @allure.step('Получить название страницы')
    def get_title_of_current_page(self):
        text = self.find_element_by_locator(LoginPL.TITLE_RECOV_PAGE).text
        return text

    @allure.step('Получить атрибут локатора')
    def get_class_of_field_password(self):
        element = self.find_element_by_locator(LoginPL.PASSWORD_FIELD_ALL)
        class_text = element.get_attribute('class')
        return class_text

    @allure.step('Перейти на страницу восстановления пароля')
    def get_recov_password_page(self, email):
        # Кликнуть по кнопке "Личный кабинет" на хедере
        self.get_login_page_by_button_on_main_page()
        # Перейти на страницу авторизации и кликнуть по ссылке "Восстановить пароль"
        self.get_request_recov_password_page_by_button()
        # Перейти на страницу запроса восстановления пароля и ввести email в поле ввода "Email"
        self.set_email(email)
        # Кликнуть по кнопке "Восстановить"
        self.get_recov_password_page_by_button()

    def get_button_save(self):
        return self.find_element_by_locator(LoginPL.BUTTON_SAVE)
