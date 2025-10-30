from time import sleep
from typing import List
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver

from config.params import URL
from utils.utils import (
                customer_to_delete,
                generate_last_name,
                generate_post_code,
                generate_first_name
    )
from config.locators import ManagerPageLocators


driver = webdriver.Chrome()
driver.get(URL)


class BasePage():
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait: WebDriver = WebDriverWait(self.driver, 10)

    def _is_clickable(self, by_value: tuple) -> WebElement:
        return self.wait.until(
            EC.element_to_be_clickable(by_value)
        )

    def _find_element(self, by_value: tuple) -> WebElement:
        return self.wait.until(
            EC.presence_of_element_located(by_value)
        )

    def _alert_is_present(self) -> None:
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        sleep(3)
        alert.accept()


class ManagerPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.post_code: str = generate_post_code()
        self.first_name: str = generate_first_name(self.post_code)
        self.last_name: str = generate_last_name()

    def _get_table_content(self) -> List[WebElement]:
        return self.wait.until(
                    EC.presence_of_all_elements_located(
                        ManagerPageLocators.TABLE_OF_CUSTOMERS
                    )
                )

    def _get_customers_names_list(self) -> List[str]:
        customer_names: List = []
        for row in self._get_table_content():
            first_name_cell = row.find_element(
                ManagerPageLocators.FIRST_NAME_CELL
                ).text
            customer_names.append(first_name_cell)
            print(f"customer_names_list {customer_names}")
        return customer_names

    def click_add_customer_tab(self) -> None:
        button: WebElement = self._is_clickable(
            ManagerPageLocators.ADD_CUSTOMER_TAB
        )
        button.click()
        sleep(2)

    def fill_post_code(self) -> None:
        post_code_field: WebElement = self._find_element(
            ManagerPageLocators.POST_CODE_FIELD
        )
        post_code_field.send_keys(self.post_code)
        sleep(2)

    def fill_first_name(self) -> None:
        first_name_field: WebElement = self._find_element(
            ManagerPageLocators.FIRST_NAME_FIELD
        )
        first_name_field.send_keys(self.first_name)
        sleep(2)

    def fill_last_name(self) -> None:
        last_name_field: WebElement = self._find_element(
            ManagerPageLocators.LAST_NAME_FIELD
        )
        last_name_field.send_keys(self.last_name)
        sleep(2)

    def click_add_customer_button(self) -> None:
        add_customer_button: WebElement = self._is_clickable(
            ManagerPageLocators.ADD_CUSTOMER_BUTTON
        )
        add_customer_button.click()
        self._alert_is_present()
        sleep(2)

    def click_customers_tab(self) -> None:
        customers_tab: WebElement = self._is_clickable(
            ManagerPageLocators.CUSTOMERS_TAB
        )
        customers_tab.click()
        sleep(2)

    def sort_customers_by_first_name(self) -> None:
        first_name_header: WebElement = self._is_clickable(
            ManagerPageLocators.FIRST_NAME_HEADER
        )
        first_name_header.click()
        sleep(2)

    def remove_customer(self) -> None:
        customers: List[str] = self._get_customers_names_list()
        customer_to_remove: str = customer_to_delete(customers)
        table_content: WebElement = self._get_table_content()
        for row in table_content:
            first_name_cell = row.find_element(
                ManagerPageLocators.FIRST_NAME_CELL
            )
            if first_name_cell.text.strip() == customer_to_remove:
                print("Deleting customer:", customer_to_remove)
                delete_button: WebElement = row.find_element(
                    *ManagerPageLocators.DELETE_BUTTON
                )
                delete_button.click()
                break
        sleep(2)


page = ManagerPage(driver)
page.click_add_customer_tab()
page.fill_post_code()
page.fill_first_name()
page.fill_last_name()
page.click_add_customer_button()
page.click_customers_tab()
page.sort_customers_by_first_name()
page.remove_customer()
