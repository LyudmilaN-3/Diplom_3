import allure

from ..constants import Constant
from ..pages.order_page import OrderPage
from ..locators.main_page_locators import MainPageLocator as MainPL


class TestOrderPage:

    @allure.title('Проверка возможности открыть всплывающее окно с заказом')
    def test_move_to_main_page_by_button(self, driver):
        order_page = OrderPage(driver)
        # Открыть главную страницу сайта
        order_page.go_to_site()
        # Перейти на страницу заказов
        order_page.get_order_page_by_button_on_header()
        # Получить атрибут первого заказа
        class_text_before = order_page.get_class_of_section_order()
        # Кликнуть по первому заказу
        order_page.click_first_order()
        # Получить атрибут первого заказа
        class_text_after = order_page.get_class_of_section_order()
        assert class_text_before != class_text_after
        assert Constant.PART_CLASS_TEXT in class_text_after

    @allure.title('Проверка отображения заказов пользователя в "Истории заказов"')
    def test_get_user_order_in_order_page(self, driver):
        order_page = OrderPage(driver)
        # Открыть главную страницу сайта
        order_page.go_to_site()
        # Войти в аккаунт
        order_page.get_site_as_login_user()
        # Перейти в личный кабинет
        order_page.get_profile_page()
        # Перейти в раздел "История заказов" личного кабинета
        order_page.move_to_order_history_page()
        # Получить номер заказа пользователя
        user_number = order_page.get_number_user_order()
        # Перейти на страницу заказов
        order_page.get_order_page_by_button_on_header()
        # Получить номера заказов
        numbers = order_page.get_number_orders()
        assert user_number in numbers

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время"')
    def test_increase_counter_orders_all_time(
            self,
            driver,
            element=MainPL.FIRST_INGREDIENT,
            target=MainPL.PLACE_ORDER
    ):
        order_page = OrderPage(driver)
        # Открыть главную страницу сайта
        order_page.go_to_site()
        # Перейти на страницу заказов по кнопке на хедере
        order_page.get_order_page_by_button_on_header()
        # Получить количество заказов за всё время
        count_before = order_page.get_count_orders_all_time()
        # Войти в аккаунт
        order_page.get_site_as_login_user()
        # Сделать заказ
        order_page.get_order(element, target)
        # Закрыть всплывающее окно
        order_page.close_order_window()
        # Перейти на страницу заказов по кнопке на хедере
        order_page.get_order_page_by_button_on_header()
        # Получить количество заказов за всё время
        count_after = order_page.get_count_orders_all_time()
        assert count_before != count_after
        assert int(count_before) + 1 == int(count_after)

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня"')
    def test_increase_counter_orders_today(
            self,
            driver,
            element=MainPL.FIRST_INGREDIENT,
            target=MainPL.PLACE_ORDER
    ):
        order_page = OrderPage(driver)
        # Открыть главную страницу сайта
        order_page.go_to_site()
        # Перейти на страницу заказов по кнопке на хедере
        order_page.get_order_page_by_button_on_header()
        # Получить количество заказов за сегодня
        count_before = order_page.get_count_orders_today()
        # Войти в аккаунт
        order_page.get_site_as_login_user()
        # Сделать заказ
        order_page.get_order(element, target)
        # Закрыть всплывающее окно
        order_page.close_order_window()
        # Перейти на страницу заказов по кнопке на хедере
        order_page.get_order_page_by_button_on_header()
        # Получить количество заказов за всё время
        count_after = order_page.get_count_orders_today()
        assert count_before != count_after
        assert int(count_before) + 1 == int(count_after)

    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_get_new_order_in_section_in_work(
            self,
            driver,
            element=MainPL.FIRST_INGREDIENT,
            target=MainPL.PLACE_ORDER
    ):
        order_page = OrderPage(driver)
        # Открыть главную страницу сайта
        order_page.go_to_site()
        # Войти в аккаунт
        order_page.get_site_as_login_user()
        # Сделать заказ
        order_page.get_order(element, target)
        # Получить номер заказа
        number = order_page.get_number_new_order()
        # Закрыть всплывающее окно
        order_page.close_order_window()
        # Перейти на страницу заказов по кнопке на хедере
        order_page.get_order_page_by_button_on_header()
        # Получить номера заказов в разделе "В работе"
        numbers = order_page.get_number_orders_in_section_in_work()
        assert number in numbers
