from typing import Tuple
import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.create_and_patch_model import CreateAndPatchModel
from models.patch_id_model import PatchIdModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
@allure.feature("Обновление сущности")
@allure.suite("API тесты")
class TestPatchEntity:
    @allure.title("Тест обновления сущности")
    @allure.description("Проверяет успешное обновление сущности через АПИ.")
    def test_patch_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        patch_entity: Tuple[PatchIdModel, CreateAndPatchModel],
        use_api_mocks: bool
    ):

        with allure.step("Мокирование запроса `CREATE`"):
            if use_api_mocks:
                mock_response = MockScenarios.PATCH["positive"]
                mocker.patch.object(
                    api_client,
                    "patch_entity",
                    return_value=mock_response
                )

        with allure.step("Выполнение запроса `CREATE`"):
            response = api_client.patch_entity(*patch_entity)
            allure.attach(
                str(response),
                name="Ответ API",
                attachment_type=allure.attachment_type.JSON
            )

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
