import allure

from pages.delete_customer import DeleteCustomer


class TestDeleteCustomer:
    @allure.title("Тест удаления клиента")
    @allure.description("Удаляет клиента, согласно алгоритму в тест-кейсе")
    def test_delete_customer(
        self,
        delete_customer: DeleteCustomer
    ) -> None:
        delete_customer.click_customers_tab()
        delete_customer.remove_customer()

