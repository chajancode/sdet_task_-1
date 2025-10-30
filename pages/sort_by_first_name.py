from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config.locators import ManagerPageLocators
from pages.base import BasePage


class SortByFirstName(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def sort_customers_by_first_name(self) -> None:
        first_name_header: WebElement = self._is_clickable(
            ManagerPageLocators.FIRST_NAME_HEADER
        )
        first_name_header.click()
        sleep(2)
