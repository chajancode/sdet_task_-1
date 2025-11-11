import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_all_params_model import GetAllParamsModel
from models.get_all_response_model import GetAllResponseModel
from tests.mocks.api_scenarios import MockScenarios


@pytest.mark.api
@allure.feature("Получение списка сущностей")
@allure.suite("API тесты")
class TestGetAll:

    @allure.title("Тест получения всех сущностей")
    @allure.description("Проверяет успешное получение сущностей через АПИ.")
    def test_get_all(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        get_all_params: GetAllParamsModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            with allure.step("Мокирование запроса `GET_ALL`"):
                mock_response = MockScenarios.GET_ALL["positive"]
                mocker.patch.object(
                    api_client,
                    "get_all",
                    return_value=mock_response
                )

        with allure.step("Выполнение запроса `GET_ALL`"):
            response = api_client.get_all(get_all_params)
            allure.attach(
                str(response),
                name="Ответ API",
                attachment_type=allure.attachment_type.JSON
            )

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
        else:
            assert GetAllResponseModel.model_validate(
                    response
            ), "Ответ не соответсвует \n"
            f"{GetAllResponseModel.model_dump_json()}"
