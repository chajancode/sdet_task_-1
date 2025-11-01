from time import sleep
from typing import List

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from config.locators import ManagerPageLocators
from pages.base import BasePage


@allure.feature("Управление клиентами")
@allure.story("Сортировка клиентов по имени")
class SortByFirstName(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._unsorted_list: List[str] = self.get_unsorted_list

    @property
    def get_unsorted_list(self) -> List[str]:
        self.click_customers_tab()
        return self._get_customers_names_list()

    @allure.step("Сортировка прошла успешно")
    def _check_if_sorted(self) -> None:
        sorted_list: List[str] = self._get_customers_names_list()
        if sorted_list == self._unsorted_list:
            raise AssertionError(
                "Сортировка по столбцу 'First Name' не удалась"
            )

    @allure.step("Выполнение сортировки клиентов по имени")
    def sort_customers_by_first_name(self) -> None:
        self._click_element(
            ManagerPageLocators.FIRST_NAME_HEADER,
            "First Name"
        )
        self._check_if_sorted()
        sleep(2)
