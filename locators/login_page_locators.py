from selenium.webdriver.common.by import By


class LoginPageLocator:

    # Страница входа в аккаунт
    EMAIL_FIELD = (By.CSS_SELECTOR, "fieldset input[type='text']")  # Поле ввода "Email"
    PASSWORD_FIELD = (By.CSS_SELECTOR, "fieldset input[type='password']")  # Поле ввода "Пароль"
    BUTTON_INTO = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    LINK_RECOV_PASS = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль"

    # Страница запроса восстановления пароля
    TITLE_RECOV_PAGE = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"
    EMAIL_FIELD_RECOV = (
        By.XPATH, "//input[@class='text input__textfield text_type_main-default']"
    )  # Поле ввода "Email"

    # Страница восстановления пароля
    PASSWORD_FIELD_RECOV = (
        By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']"
    )  # Поле ввода "Пароль"
    BUTTON_HIDE_SHOW_PASS = (
        By.XPATH, "//div[@class='input__icon input__icon-action']/*"
    )  # Кнопка "Скрыть/Показать пароль"
    PASSWORD_FIELD_ALL = (
        By.XPATH, "//div[@class='input__container']/div[contains(@class, 'input')]"
    )  # Рамка поля ввода "Пароль"
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
