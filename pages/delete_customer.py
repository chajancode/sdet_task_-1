from typing import List

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.utils import customer_to_delete
from locators.manager_page_locators import ManagerPageLocators
from pages.base import BasePage


@allure.feature("Управление клиентами")
@allure.story("Удаление клиента")
class DeleteCustomer(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Поиск строки клиента для удаления")
    def _find_customer_row(self, customer_name: str) -> WebElement | None:
        table_rows: List[WebElement] = self._get_table_content()

        for row in table_rows:
            first_name_cell: WebElement = row.find_element(
                *ManagerPageLocators.FIRST_NAME_CELL
            )
            if first_name_cell.text == customer_name:
                return row

    @allure.step("Клиент {name} удалён")
    def _check_if_customer_removed(self, name: str) -> None:
        current_names_in_table: List[str] = self._get_customers_names_list()

        if name in current_names_in_table:
            raise AssertionError(f"Клиент {name} не был удалён")

    @allure.step("Удаление клиента")
    def remove_customer(self) -> None:
        customers: List[str] = self._get_customers_names_list()
        customer_to_remove: str = customer_to_delete(customers)

        customer_row: WebElement | None = self._find_customer_row(
            customer_to_remove
        )
        if not customer_row:
            raise ValueError(f"Клиент {customer_to_remove} не найден")

        delete_button: WebElement = customer_row.find_element(
            *ManagerPageLocators.DELETE_BUTTON
        )
        delete_button.click()
        self._check_if_customer_removed(customer_to_remove)
