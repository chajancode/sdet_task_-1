from typing import Generator
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
    chrome_options.add_argument("--start-maximized")
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
