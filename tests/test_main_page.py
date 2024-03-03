import allure

from ..constants import Constant
from ..pages.main_page import MainPage
from ..locators.main_page_locators import MainPageLocator as MainPL


class TestMainPage:

    @allure.title('Проверка возможности перехода по клику на "Конструктор"')
    def test_move_to_main_page_by_button(self, driver):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Кликнуть по кнопке "Лента заказов" на хедере
        main_page.get_order_page_by_button_on_header()
        # Кликнуть по кнопке "Конструктор" на хедере
        main_page.get_main_page_by_button_on_header()
        # Получить название текущей страницы
        current_title = main_page.get_title_of_main_page()
        # Получить текущий url
        current_url = main_page.get_current_url_main_page()
        assert current_title == Constant.TITLE_MAIN_PAGE
        assert current_url == Constant.MAIN_URL

    @allure.title('Проверка возможности перехода по клику на "Ленту заказов"')
    def test_move_to_order_page_by_button(self, driver):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Кликнуть по кнопке "Лента заказов" на хедере
        main_page.get_order_page_by_button_on_header()
        # Получить название текущей страницы
        current_title = main_page.get_title_of_order_page()
        # Получить текущий url
        current_url = main_page.get_current_url_order_page()
        assert current_title == Constant.TITLE_ORDER_PAGE
        assert Constant.ORDER_PATH_URL in current_url

    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    def test_get_pop_up_ingedient(self, driver):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Кликнуть по первому ингредиенту
        main_page.click_by_first_ingredient()
        # Получить название окна
        current_title = main_page.get_title_of_pop_up_ingredient()
        # Получить текущий url
        current_url = main_page.get_current_url_pop_up_page()
        assert current_title == Constant.TITLE_POP_UP_INGREDIENT
        assert Constant.INGREDIENT_PATH_URL in current_url

    @allure.title('Проверка возможности закрыть всплывающее окно с деталями по крестику')
    def test_close_pop_up_ingedient(self, driver):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Кликнуть по первому ингредиенту
        main_page.click_by_first_ingredient()
        # Кликнуть в окне по крестику
        main_page.close_pop_up_ingredient()
        # Получить название текущей страницы
        current_title = main_page.get_title_of_main_page()
        assert current_title == Constant.TITLE_MAIN_PAGE

    @allure.title('Проверка увеличения счётчика ингредиента при его добавлении в заказ')
    def test_add_count_ingedient(
            self,
            driver,
            element=MainPL.FIRST_INGREDIENT,
            target=MainPL.PLACE_ORDER
    ):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Проверить счётчик ингредиента
        count_before = main_page.check_counter_ingredient()
        # Перетащить ингредиент в блок заказа
        main_page.drag_and_drop_element(element, target)
        # Проверить счётчик ингредиента
        count_after = main_page.check_counter_ingredient()
        assert count_before != count_after
        assert count_after == '2'

    @allure.title('Проверка возможности оформления заказа')
    def test_get_order_by_login_user(
            self,
            driver,
            element=MainPL.FIRST_INGREDIENT,
            target=MainPL.PLACE_ORDER
    ):
        main_page = MainPage(driver)
        # Открыть главную страницу сайта
        main_page.go_to_site()
        # Войти в аккаунт
        main_page.get_site_as_login_user()
        # Перетащить ингредиент в блок заказа
        main_page.drag_and_drop_element(element, target)
        # Нажать на кнопку "Оформить заказ"
        main_page.click_button_to_get_order()
        # Получить текст в модальном окне
        text = main_page.get_text_modal_window()
        assert text == Constant.TEXT_ORDER_WINDOW
