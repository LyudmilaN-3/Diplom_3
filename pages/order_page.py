import allure

from ..locators.account_page_locators import AccountPageLocator as AccountPL
from ..locators.login_page_locators import LoginPageLocator as LoginPL
from ..locators.main_page_locators import MainPageLocator as MainPL
from ..locators.order_page_locators import OrderPageLocator as OrderPL
from ..pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получить название страницы')
    def get_title_of_current_page(self):
        text = self.find_element_by_locator(OrderPL.TITLE_ORDER_PAGE).text
        return text

    @allure.step('Перейти на страницу заказов по кнопке "Лента заказов" на хедере')
    def get_order_page_by_button_on_header(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_ORDERS)

    @allure.step('Кликнуть по первому заказу')
    def click_first_order(self):
        self.find_element_by_locator_and_click(OrderPL.PART_OF_FIRST_ORDER)

    @allure.step('Получить атрибут локатора модального окна')
    def get_class_of_section_order(self):
        element = self.find_element_by_locator(OrderPL.MODAL_WINDOW_ORDER)
        class_text = element.get_attribute('class')
        return class_text

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

    @allure.step('Перейти в раздел "История заказов" личного кабинета')
    def move_to_order_history_page(self):
        self.find_element_by_locator_and_click(AccountPL.BUTTON_HISTORY)

    @allure.step('Перейти в личный кабинет кликом по кнопке на хедере')
    def get_profile_page(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_ACC)

    @allure.step('Получить номер заказа пользователя')
    def get_number_user_order(self):
        self.scroll_to_element(OrderPL.NUMBER_ORDER_IN_ORDERS)
        user_number = self.find_element_by_locator(OrderPL.NUMBER_ORDER_IN_ORDERS).text
        return user_number

    @allure.step('Получить номера заказов в "Ленте заказов"')
    def get_number_orders(self):
        numbers = []
        elements = self.find_elements_by_locator(AccountPL.NUMBER_ORDER_IN_HISTORY)
        for element in elements:
            number = element.text
            numbers.append(number)
        return numbers

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_in_order(self, element, target):
        self.drag_and_drop_element(element, target)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_button_to_get_order(self):
        self.find_element_by_locator_and_click(MainPL.BUTTON_GET_ORDER)

    @allure.step('Сделать заказ')
    def get_order(self, element, target):
        # Добавить ингредиент в заказ
        self.add_ingredient_in_order(element, target)
        # Нажать на кнопку "Оформить заказ"
        self.click_button_to_get_order()

    @allure.step('Получить количество заказов за всё время')
    def get_count_orders_all_time(self):
        count_all_time = self.find_element_by_locator(OrderPL.COUNTER_ALL_TIME).text
        return count_all_time

    @allure.step('Закрыть всплывающее окно')
    def close_order_window(self):
        self.find_element_by_locator_and_click(MainPL.X_CLOSE_WINDOW)

    @allure.step('Получить количество заказов за сегодня')
    def get_count_orders_today(self):
        count_today = self.find_element_by_locator(OrderPL.COUNTER_TODAY).text
        return count_today

    @allure.step('Получить номер нового заказа')
    def get_number_new_order(self):
        number = self.find_element_by_locator(MainPL.NUMBER_NEW_ORDER).text
        return number

    @allure.step('Получить номера заказов в разделе "В работе"')
    def get_number_orders_in_section_in_work(self):
        numbers = []
        elements = self.find_elements_by_locator(OrderPL.SECTION_IN_WORK)
        for element in elements:
            number = element.text
            numbers.append(number)
        return numbers
