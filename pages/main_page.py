import allure

from ..locators.login_page_locators import LoginPageLocator as LoginPL
from ..locators.main_page_locators import MainPageLocator as MainPL
from ..locators.order_page_locators import OrderPageLocator as OrderPL
from ..pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перейти на главную страницу по кнопке "Конструктор" на хедере')
    def get_main_page_by_button_on_header(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_CONSTR)

    @allure.step('Перейти на страницу заказов по кнопке "Лента заказов" на хедере')
    def get_order_page_by_button_on_header(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_ORDERS)

    @allure.step('Получить название страницы заказов')
    def get_title_of_order_page(self):
        text = self.find_element_by_locator(OrderPL.TITLE_ORDER_PAGE).text
        return text

    @allure.step('Получить название главной страницы')
    def get_title_of_main_page(self):
        text = self.find_element_by_locator(MainPL.TITLE_MAIN_PAGE).text
        return text

    @allure.step('Кликнуть по ингредиенту')
    def click_by_first_ingredient(self):
        self.find_element_by_locator_and_click(MainPL.FIRST_INGREDIENT)

    @allure.step('Получить название всплывающего окна с деталями ингредиента')
    def get_title_of_pop_up_ingredient(self):
        text = self.find_element_by_locator(MainPL.INGREDIENT_DETAIL).text
        return text

    @allure.step('Закрыть всплывающее окно с деталями ингредиента')
    def close_pop_up_ingredient(self):
        self.find_element_by_locator_and_click(MainPL.X_CLOSE)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_in_order(self, element, target):
        self.drag_and_drop_element(element, target)

    @allure.step('Проверка счетчика ингредиента')
    def check_counter_ingredient(self):
        text = self.find_element_by_locator(MainPL.FIRST_INGREDIENT_COUNTER).text
        return text

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

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_button_to_get_order(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_GET_ORDER)

    @allure.step('Получить текст в модальном окне')
    def get_text_modal_window(self):
        text = self.find_element_by_locator(MainPL.MODAL_WINDOW_TEXT).text
        return text

    @allure.step('Получить текущий url главной страницы')
    def get_current_url_main_page(self):
        current_url = self.get_url(MainPL.BUTTON_INTO_ACC)
        return current_url

    @allure.step('Получить текущий url страницы заказов')
    def get_current_url_order_page(self):
        current_url = self.get_url(OrderPL.SECTION_IN_WORK)
        return current_url

    @allure.step('Получить текущий url при всплывающем окне с деталями')
    def get_current_url_pop_up_page(self):
        current_url = self.get_url(MainPL.X_CLOSE)
        return current_url
