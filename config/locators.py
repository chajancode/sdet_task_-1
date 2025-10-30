from selenium.webdriver.common.by import By


class ManagerPageLocators:
    ADD_CUSTOMER_BUTTON: tuple[By, str] = (
        By.CSS_SELECTOR, "button[type=\"submit\"]"
        )
    ADD_CUSTOMER_TAB: tuple[By, str] = (
        By.CSS_SELECTOR, "button[ng-click=\"addCust()\"]"
        )
    CUSTOMERS_TAB: tuple[By, str] = (
        By.CSS_SELECTOR, "button[ng-click=\"showCust()\"]"
        )
    FIRST_NAME_FIELD: tuple[By, str] = (
        By.CSS_SELECTOR, "[ng-model=\"fName\"]"
        )
    LAST_NAME_FIELD: tuple[By, str] = (
        By.CSS_SELECTOR, "[ng-model=\"lName\"]"
        )
    POST_CODE_FIELD: tuple[By, str] = (
        By.CSS_SELECTOR, "[ng-model=\"postCd\"]"
        )
    FIRST_NAME_HEADER: tuple[By, str] = (
        By.CSS_SELECTOR,
        "a[ng-click=\"sortType = 'fName'; sortReverse = !sortReverse\"]"
        )
    CUSTOMER_TABLE_ROWS: tuple[By, str] = (By.CSS_SELECTOR, "table tbody tr")
    FIRST_NAME_CELL: tuple[By, str] = (By.CSS_SELECTOR, "td:first-child")
    TABLE_OF_CUSTOMERS: tuple[By, str] = (By.CSS_SELECTOR, "tbody tr")
    DELETE_BUTTON: tuple[By, str] = (By.CSS_SELECTOR, "td button")
