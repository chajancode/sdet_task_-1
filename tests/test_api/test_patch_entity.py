import allure
import pytest

from api.entity import APIEntity


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест изменения сущности")
    def test_patch_entity(self, api_client: APIEntity, patch_entity):
        api_client.patch_entity(*patch_entity)
