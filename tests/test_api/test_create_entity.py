import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.create_and_patch_model import CreateAndPatchModel
from models.create_response_model import CreateResponseModel
from tests.mocks.api_scenarios import MockScenarios


@pytest.mark.api
@allure.feature("Создание новой сущности")
@allure.suite("API тесты")
class TestCreateEntity:

    @allure.title("Тест создания новой сущности")
    @allure.description("Проверяет успешное создание сущности через АПИ.")
    def test_create_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        create_entity_data: CreateAndPatchModel,
        use_api_mocks: bool  # conftest.py
    ):

        if use_api_mocks:
            with allure.step("Мокирование запроса `CREATE`"):
                mock_response = MockScenarios.CREATE["positive"]
                mocker.patch.object(
                    api_client,
                    "create_entity",
                    return_value=mock_response
                )

        with allure.step("Выполнение запроса `CREATE`"):
            response = api_client.create_entity(create_entity_data)
            allure.attach(
                str(response),
                name="Ответ API",
                attachment_type=allure.attachment_type.JSON
            )

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
        assert isinstance(response, int), "Ожидаемый ответ int"
