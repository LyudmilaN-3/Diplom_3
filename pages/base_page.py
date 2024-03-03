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

    def scroll_to_element(self, locator, time=10):
        element = self.find_element_by_locator(locator, time)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.element_to_be_clickable(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')
