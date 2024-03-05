from selenium.webdriver.common.by import By


class MainPageLocator:

    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок главной страницы

    # Хедер
    BUTTON_ACC = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    BUTTON_CONSTR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    BUTTON_ORDERS = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка "Лента заказов"

    # Блок выбора ингредиентов
    FIRST_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # Первый ингредиент
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")  # Счётчик первого ингредиента

    # Всплывающее окно ингредиента
    INGREDIENT_DETAIL = (By.XPATH, "//h2[text()='Детали ингредиента']")  # Заголовок окна
    X_CLOSE = (By.XPATH, "//div/div/section/div/button[1]/*[1]")  # Крестик

    # Блок заказа
    PLACE_ORDER = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Место для сбора заказа
    BUTTON_INTO_ACC = (
        By.XPATH, "//main/section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button"
    )  # Кнопка "Войти в аккаунт"
    BUTTON_GET_ORDER = (By.XPATH, "//main/section[2]/div/button")  # Кнопка "Оформить заказ"

    # Всплывающее окно заказа
    MODAL_WINDOW_TEXT = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")  # Надпись в окне
    X_CLOSE_WINDOW = (By.XPATH, "//div/div/section/div/button")  # Крестик
    NUMBER_NEW_ORDER = (
        By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m text text_type_digits-large mb-8')]"
    )  # Номер заказа
