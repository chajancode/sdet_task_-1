import allure
import pytest

from api.entity import APIEntity


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест получения всех сущностей")
    def test_create_entity(self, api_client: APIEntity, get_all_params):
        api_client.get_all(get_all_params)
