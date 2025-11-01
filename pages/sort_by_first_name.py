from time import sleep

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from config.locators import ManagerPageLocators
from pages.base import BasePage


@allure.feature("Управление клиентами")
@allure.story("Сортировка клиентов по имени")
class SortByFirstName(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.names

    @allure.step("Выполнение сортировки клиентов по имени")
    def sort_customers_by_first_name(self) -> None:
        self._click_element(
            ManagerPageLocators.FIRST_NAME_HEADER,
            "First Name"
        )
        sleep(2)
