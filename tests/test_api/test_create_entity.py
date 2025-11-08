import allure
import pytest

from api.entity import APIEntity


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест создания новой сущности")
    def test_create_entity(self, api_client: APIEntity, create_entity_data):
        api_client.create_entity(create_entity_data)
