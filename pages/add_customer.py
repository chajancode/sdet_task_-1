from time import sleep
from typing import List

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.utils import (
                generate_last_name,
                generate_post_code,
                generate_first_name
    )
from config.locators import ManagerPageLocators
from pages.base import BasePage


@allure.feature("Управление клиентами")
@allure.story("Добавление нового клиента")
class AddCustomer(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.post_code: str = generate_post_code()
        self.first_name: str = generate_first_name(self.post_code)
        self.last_name: str = generate_last_name()
        self._initial_rows: int = self.initial_count

    @property
    def initial_count(self) -> List[WebElement]:
        self.click_customers_tab()
        table_content: List[WebElement] = self._get_table_content()
        return len(table_content)

    @allure.step("Поле {name} заполнено значением {value}")
    def _fill_field(self, locator: tuple, value: str, name: str) -> None:
        field: WebElement = self._find_element(locator)
        field.send_keys(value)

    @allure.step("Нажата вкладка 'Add Customer'")
    def click_add_customer_tab(self) -> None:
        self._click_element(
            ManagerPageLocators.ADD_CUSTOMER_TAB,
            "вкладка 'Add Customer'"
        )
        sleep(2)

    @allure.step("Заполнение поля 'Post Code'")
    def fill_post_code(self) -> None:
        self._fill_field(
            ManagerPageLocators.POST_CODE_FIELD,
            self.post_code,
            "Post code"
        )
        sleep(2)

    @allure.step("Заполнение поля 'First Name'")
    def fill_first_name(self) -> None:
        self._fill_field(
            ManagerPageLocators.FIRST_NAME_FIELD,
            self.first_name,
            "First name"
        )
        sleep(2)

    @allure.step("Заполнение поля 'Last Name'")
    def fill_last_name(self) -> None:
        self._fill_field(
            ManagerPageLocators.LAST_NAME_FIELD,
            self.last_name,
            "Last name"
        )
        sleep(2)

    @allure.step("Нажата кнопка 'Add Customer'")
    def click_add_customer_button(self) -> None:
        self._click_element(
            ManagerPageLocators.ADD_CUSTOMER_BUTTON,
            "кнопка 'Add Customer'"
        )
        self._alert_is_present()
        sleep(2)

    @allure.step("Данные добавлены")
    def check_if_customer_added(self) -> None:
        self.click_customers_tab()
        current_names_in_table: List[str] = self._get_customers_names_list()

        if self.first_name not in current_names_in_table:
            raise AssertionError(
                f"Клиент с именем {self.first_name} не был добавлен"
            )
