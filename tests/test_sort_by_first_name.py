import allure
import pytest

from pages.sort_by_first_name import SortByFirstName


@pytest.mark.ui
class TestSortByFirstName:
    @allure.title("Тест сортировки клиентов по имени")
    @allure.description("Сортирует клиентов по имени в алфавитном порядке")
    def test_sort_by_first_name(
        self,
        sort_by_first_name: SortByFirstName
    ) -> None:
        sort_by_first_name.click_customers_tab()
        sort_by_first_name.sort_customers_by_first_name()
