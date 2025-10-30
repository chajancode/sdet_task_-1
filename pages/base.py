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

    @allure.step("Нажата вкладка Customers")
    def click_customers_tab(self) -> None:
        customers_tab: WebElement = self._is_clickable(
            ManagerPageLocators.CUSTOMERS_TAB
        )
        customers_tab.click()
        sleep(2)
