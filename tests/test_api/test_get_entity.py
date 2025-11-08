import allure
import pytest

from api.entity import APIEntity


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест получения сущности по ID")
    def test_get_entity(self, api_client: APIEntity, get_params):
        api_client.get_entity(get_params)
