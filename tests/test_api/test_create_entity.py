import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.create_and_patch_model import CreateAndPatchModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
class TestCreateEntity:

    @allure.title("Тест создания новой сущности")
    def test_create_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        create_entity_data: CreateAndPatchModel,
        use_api_mocks: bool  # conftest.py
    ):

        if use_api_mocks:
            mock_response = MockScenarios.CREATE["positive"]
            mocker.patch.object(
                api_client,
                "create_entity",
                return_value=mock_response
            )

        response = api_client.create_entity(create_entity_data)

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
