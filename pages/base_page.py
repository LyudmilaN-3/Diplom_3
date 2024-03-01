import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..constants import Constant


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Открыть главную страницу "Stellar Burgers" '
                 f'{Constant.MAIN_URL}')
    def go_to_site(self):
        return self.driver.get(Constant.MAIN_URL)

    def find_element_by_locator(self, locator, time=30):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')

    def find_elements_by_locator(self, locator, time=30):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_all_elements_located(locator),
                          message=f'Элементы не найдены по локатору - {[*locator]}')

    def find_element_by_locator_and_click(self, locator, time=30):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.element_to_be_clickable(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}').click()

    def find_element_by_locator_and_send_keys(self, locator, value, time=10):
        self.find_element_by_locator(locator, time).send_keys(value)

    def get_url(self, locator, time=30):
        self.find_element_by_locator(locator, time)
        current_url = self.driver.current_url
        return current_url

    def drag_and_drop_element(self, element, target):
        element = self.find_element_by_locator(element)
        target = self.find_element_by_locator(target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Перейти на страницу входа в аккаунт по кнопке на хедере')
    def get_login_page_by_button_on_header(self, locator):
        self.find_element_by_locator_and_click(locator)

    @allure.step('Заполнить поля ввода "Почта" и "Пароль" для входа в аккаунт')
    def fill_email_password_fields(self, locator1, locator2, email, password):
        self.find_element_by_locator_and_send_keys(locator1, email)
        self.find_element_by_locator_and_send_keys(locator2, password)

    @allure.step('Перейти на главную страницу по кнопке "Войти" на странице входа в аккаунт')
    def get_main_page_as_login_user(self, locator):
        self.find_element_by_locator_and_click(locator)

    @allure.step('Зайти на сайт под залогиненным пользователем')
    def get_site_as_login_user(self, email, password):
        # Перейти на страницу входа в аккаунт по кнопке на хедере
        self.get_login_page_by_button_on_header()
        # Заполнить поля ввода "Почта" и "Пароль" для входа в аккаунт
        self.fill_email_password_fields(email, password)
        # Перейти на главную страницу по кнопке "Войти"
        self.get_main_page_as_login_user()

    def scroll_to_element(self, locator, time=10):
        element = self.find_element_by_locator(locator, time)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.element_to_be_clickable(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')
