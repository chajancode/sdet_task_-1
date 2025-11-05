from typing import Generator
import allure
import pytest

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_customer import AddCustomer
from pages.sort_by_first_name import SortByFirstName
from pages.delete_customer import DeleteCustomer


@pytest.fixture(scope="session")
def browser() -> Generator[WebDriver, None, None]:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver: WebDriver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.fixture()
def add_customer(browser: WebDriver) -> AddCustomer:
    page = AddCustomer(browser)
    return page


@pytest.fixture()
def sort_by_first_name(browser: WebDriver) -> SortByFirstName:
    page = SortByFirstName(browser)
    return page


@pytest.fixture()
def delete_customer(browser: WebDriver) -> DeleteCustomer:
    page = DeleteCustomer(browser)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(
        item: pytest.Item,
        call: pytest.CallInfo) -> Generator[None, None, None]:
    outcome = yield
    rep: pytest.TestReport = outcome.get_result()
    driver = item.funcargs["browser"]

    if rep.when == "call" and rep.failed:
        screenshot = driver.get_screenshot_as_png()
        screenshot_name = f"Ошибка: в тесте {item.name}"
        allure.attach(
            screenshot,
            name=screenshot_name,
        )
