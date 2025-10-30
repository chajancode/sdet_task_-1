from time import sleep

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

    def _fill_field(self, locator: tuple, value: str, name: str) -> None:
        field: WebElement = self._find_element(locator)
        assert field is not None, f"Поле {name} не найдено"
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
