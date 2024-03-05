import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1400,1800')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

