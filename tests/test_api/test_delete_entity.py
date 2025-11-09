import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_and_delete_model import GetAndDeleteModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест удаления сущности")
    def test_delete_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        delete_params: GetAndDeleteModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            mock_response = MockScenarios.DELETE["positive"]
            mocker.patch.object(
                api_client,
                "delete_entity",
                return_value=mock_response
            )

        response = api_client.delete_entity(delete_params)

        if use_api_mocks:
            assert response == mock_response, "Ответ не соответствует моку"
