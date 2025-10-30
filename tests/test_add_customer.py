from pages.add_customer import AddCustomer


class TestAddCustomer:
    def test_add_customer(self, add_customer: AddCustomer) -> None:
        add_customer.click_add_customer_tab()
        add_customer.fill_post_code()
        add_customer.fill_first_name()
        add_customer.fill_last_name()
        add_customer.click_add_customer_button()
