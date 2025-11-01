from typing import List
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from time import sleep

from config.locators import ManagerPageLocators
from config.params import URL


class BasePage():
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = self.driver.get(URL)
        self.wait: WebDriver = WebDriverWait(self.driver, 10)

    @allure.step("Получение содержимого таблицы клиентов")
    def _get_table_content(self) -> List[WebElement]:
        content = self.wait.until(
                    EC.presence_of_all_elements_located(
                        ManagerPageLocators.TABLE_OF_CUSTOMERS
                    )
                )
        assert content is not None, "Таблица клиентов не найдена"
        return content

    @allure.step("Получение списка имен всех клиентов из таблицы")
    def _get_customers_names_list(self) -> List[str]:
        customer_names: List[str] = []
        table_rows: List[WebElement] = self._get_table_content()

        for row in table_rows:
            first_name_cell = row.find_element(
                *ManagerPageLocators.FIRST_NAME_CELL
                ).text
            customer_names.append(first_name_cell)

        assert customer_names, "Невозможно получить данные"
        return customer_names

    def _is_clickable(self, by_value: tuple) -> WebElement:
        element = self.wait.until(
            EC.element_to_be_clickable(by_value)
        )
        assert element is not None, "Элемент не найден"
        return element

    def _find_element(self, by_value: tuple) -> WebElement:
        element = self.wait.until(
            EC.presence_of_element_located(by_value)
        )
        assert element is not None, "Элемент не найден"
        return element

    @allure.step("Кликнут алерт")
    def _alert_is_present(self) -> None:
        alert = WebDriverWait(
            self.driver, 10
            ).until(
                EC.alert_is_present()
        )
        assert alert is not None, "Алерт не появился"
        sleep(3)
        alert.accept()

    @allure.step("Кликнут элемент {name}")
    def _click_element(self, locator: tuple, name: str) -> None:
        element = self._is_clickable(locator)
        assert element is not None, f"Элемент {name} не найден"
        element.click()

    def click_customers_tab(self) -> None:
        self._click_element(
            ManagerPageLocators.CUSTOMERS_TAB,
            "Customers"
        )
        sleep(2)
