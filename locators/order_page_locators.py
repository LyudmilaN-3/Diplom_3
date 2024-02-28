from selenium.webdriver.common.by import By


class OrderPageLocator:

    TITLE_ORDER_PAGE = (By.XPATH, "//h1[text()='Лента заказов']")

    # Блок "Лента заказов"
    PART_OF_FIRST_ORDER = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']")  # Первый заказ
    MODAL_WINDOW_ORDER = (By.XPATH, "//body/div/div/section[last()]")  # Модальное окно заказа
    NUMBER_ORDER_IN_ORDERS = (By.XPATH, "//li[last()]/a/div/p[@class='text text_type_digits-default']")  # Номер заказа

    # Блок статистики
    COUNTER_ALL_TIME = (
        By.XPATH, "//div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )  # Счётчик "Выполнено за всё время"
    COUNTER_TODAY = (
        By.XPATH, "//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )  # Счётчик "Выполнено за сегодня
    SECTION_IN_WORK = (
        By.XPATH, "//main/div/div/div/div/ul[2]/li[@class='text text_type_main-small']"
    )  # Раздел "В работе"
