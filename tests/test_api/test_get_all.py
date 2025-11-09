import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_all_params_model import GetAllParamsModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
class TestCreateEntity:

    @allure.title("Тест получения всех сущностей")
    def test_create_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        get_all_params: GetAllParamsModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            mock_response = MockScenarios.GET_ALL["positive"]
            mocker.patch.object(
                api_client,
                "get_all",
                return_value=mock_response
            )

        response = api_client.get_all(get_all_params)

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
