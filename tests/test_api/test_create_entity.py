import allure
import pytest
from pytest_mock import MockerFixture, mocker

from api.entity import APIEntity
from models.create_and_patch_model import CreateAndPatchModel
from tests.mocks.scenarios import MockScenarios
from conftest import use_api_mocks


@pytest.mark.api
class TestCreateEntity:

    method = "CREATE"

    @allure.title("Тест создания новой сущности")
    def test_create_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        create_entity_data: CreateAndPatchModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            mock_response = MockScenarios.CREATE["positive"]
            mocker.patch(
                api_client,
                "create_entity",
                return_value=mock_response
            )

        api_client.create_entity(create_entity_data)
