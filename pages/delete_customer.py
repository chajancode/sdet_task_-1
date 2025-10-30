from time import sleep
from typing import List

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from utils.utils import customer_to_delete
from config.locators import ManagerPageLocators
from pages.base import BasePage


@allure.feature("Управление клиентами")
@allure.story("Удаление клиента")
class DeleteCustomer(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Получение содержимого таблицы клиентов")
    def _get_table_content(self) -> List[WebElement]:
        return self.wait.until(
                    EC.presence_of_all_elements_located(
                        ManagerPageLocators.TABLE_OF_CUSTOMERS
                    )
                )

    @allure.step("Получение списка имен всех клиентов из таблицы")
    def _get_customers_names_list(self) -> List[str]:
        customer_names: List = []
        for row in self._get_table_content():
            first_name_cell = row.find_element(
                *ManagerPageLocators.FIRST_NAME_CELL
                ).text
            customer_names.append(first_name_cell)
        return customer_names

    @allure.step("Удаление клиента")
    def remove_customer(self) -> None:
        customers: List[str] = self._get_customers_names_list()
        customer_to_remove: str = customer_to_delete(customers)
        table_content: WebElement = self._get_table_content()
        for row in table_content:
            first_name_cell = row.find_element(
                *ManagerPageLocators.FIRST_NAME_CELL
            )
            if first_name_cell.text.strip() == customer_to_remove:
                delete_button: WebElement = row.find_element(
                    *ManagerPageLocators.DELETE_BUTTON
                )
                delete_button.click()
                break
        sleep(5)
