import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_and_delete_model import GetAndDeleteModel
from models.get_response_model import GetResponseModel
from tests.mocks.api_scenarios import MockScenarios


@pytest.mark.api
@allure.feature("Создание новой сущности")
@allure.suite("API тесты")
class TestGetEntity:

    @allure.title("Тест получения сущности по ID")
    @allure.description("Проверяет успешное создание сущности через АПИ.")
    def test_get_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        get_params: GetAndDeleteModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            with allure.step("Мокирование запроса `GET`"):
                mock_response = MockScenarios.GET["positive"]
                mocker.patch.object(
                    api_client,
                    "get_entity",
                    return_value=mock_response
                )
        with allure.step("Выполнение запроса `GET`"):
            response = api_client.get_entity(get_params)
            allure.attach(
                str(response),
                name="Ответ API",
                attachment_type=allure.attachment_type.JSON
            )

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
        else:
            assert GetResponseModel.model_validate(
                response
            ), f"Ответ не соответсвует {GetResponseModel}"
