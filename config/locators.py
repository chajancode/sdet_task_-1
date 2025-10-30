from selenium.webdriver.common.by import By


class ManagerPageLocators:
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"]")
    ADD_CUSTOMER_TAB = (By.CSS_SELECTOR, "button[ng-click=\"addCust()\"]")
    CUSTOMERS_TAB = (By.CSS_SELECTOR, "button[ng-click=\"showCust()\"]")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[ng-model=\"fName\"]")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "[ng-model=\"lName\"]")
    POST_CODE_FIELD = (By.CSS_SELECTOR, "[ng-model=\"postCd\"]")
    FIRST_NAME_HEADER = (
        By.CSS_SELECTOR,
        "a[ng-click=\"sortType = 'fName'; sortReverse = !sortReverse\"]"
        )
    CUSTOMER_TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    FIRST_NAME_CELL = (By.CSS_SELECTOR, "td:first-child")
    TABLE_OF_CUSTOMERS = (By.CSS_SELECTOR, "tbody tr")
    DELETE_BUTTON = (By.CSS_SELECTOR, "td button")
