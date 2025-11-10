import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.get_and_delete_model import GetAndDeleteModel
from tests.mocks.api_scenarios import MockScenarios


@pytest.mark.api
@allure.feature("Удаление сущности")
@allure.suite("API тесты")
class TestDeleteEntity:
    @allure.title("Тест удаления сущности")
    @allure.description("Проверяет успешное удаление сущности через АПИ.")
    def test_delete_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        delete_params: GetAndDeleteModel,
        use_api_mocks: bool
    ):

        if use_api_mocks:
            with allure.step("Мокирование запроса `DELETE`"):
                mock_response = MockScenarios.DELETE["positive"]
                mocker.patch.object(
                    api_client,
                    "delete_entity",
                    return_value=mock_response
                )
        with allure.step("Выполнение запроса `DELETE`"):
            response = api_client.delete_entity(delete_params)
            allure.attach(
                str(response),
                name="Ответ API",
                attachment_type=allure.attachment_type.JSON
            )

        if use_api_mocks:
            assert response == mock_response, "Ответ не соответствует моку"
