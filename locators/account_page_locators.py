from selenium.webdriver.common.by import By


class AccountPageLocator:

    # Личный кабинет
    BUTTON_PROFILE = (By.CSS_SELECTOR, "main nav a[href='/account/profile']")  # Кнопка "Профиль"
    BUTTON_HISTORY = (By.CSS_SELECTOR, "main nav a[href='/account/order-history']")  # Кнопка "История заказов"
    BUTTON_LOG_OUT = (By.CSS_SELECTOR, "main nav button")  # Кнопка "Выход"

    # История заказов
    NUMBER_ORDER_IN_HISTORY = (
        By.XPATH, "//p[@class='text text_type_digits-default'][last()]"
    )  # Номер последнего заказа
