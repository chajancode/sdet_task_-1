import allure
import pytest

from api.entity import APIEntity


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест удаления сущности")
    def test_delete_entity(self, api_client: APIEntity, delete_params):
        api_client.delete_entity(delete_params)
