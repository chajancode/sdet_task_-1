import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_and_delete_model import GetAndDeleteModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест получения сущности по ID")
    def test_get_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        get_params: GetAndDeleteModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            mock_response = MockScenarios.GET["positive"]
            mocker.patch.object(
                api_client,
                "get_entity",
                return_value=mock_response
            )

        response = api_client.get_entity(get_params)

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
