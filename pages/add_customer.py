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

    @allure.step("Нажата вкладка 'Add Customer'")
    def click_add_customer_tab(self) -> None:
        button: WebElement = self._is_clickable(
            ManagerPageLocators.ADD_CUSTOMER_TAB
        )
        button.click()
        sleep(2)

    @allure.step("Заполнение поля 'Post Code'")
    def fill_post_code(self) -> None:
        post_code_field: WebElement = self._find_element(
            ManagerPageLocators.POST_CODE_FIELD
        )
        post_code_field.send_keys(self.post_code)
        sleep(2)

    @allure.step("Заполнение поля 'First Name'")
    def fill_first_name(self) -> None:
        first_name_field: WebElement = self._find_element(
            ManagerPageLocators.FIRST_NAME_FIELD
        )
        first_name_field.send_keys(self.first_name)
        sleep(2)

    @allure.step("Заполнение поля 'Last Name'")
    def fill_last_name(self) -> None:
        last_name_field: WebElement = self._find_element(
            ManagerPageLocators.LAST_NAME_FIELD
        )
        last_name_field.send_keys(self.last_name)
        sleep(2)

    @allure.step("Нажата кнопка 'Add Customer' и подтверждение алерта")
    def click_add_customer_button(self) -> None:
        add_customer_button: WebElement = self._is_clickable(
            ManagerPageLocators.ADD_CUSTOMER_BUTTON
        )
        add_customer_button.click()
        self._alert_is_present()
        sleep(2)
