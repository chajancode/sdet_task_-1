import allure
import pytest

from pages.add_customer import AddCustomer


@pytest.mark.fill_forms
@pytest.mark.ui
class TestAddCustomer:
    @allure.title("Тест создания нового клиента")
    @allure.description("Генерирует почтовый индекс, имя и фамилию")
    def test_add_customer(self, add_customer: AddCustomer) -> None:
        add_customer.click_add_customer_tab()
        add_customer.fill_post_code()
        add_customer.fill_first_name()
        add_customer.fill_last_name()
        add_customer.click_add_customer_button()
        add_customer.check_if_customer_added()
