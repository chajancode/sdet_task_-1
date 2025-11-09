from typing import Tuple
import allure
import pytest
from pytest_mock import MockerFixture

from api.entity import APIEntity
from models.create_and_patch_model import CreateAndPatchModel
from models.patch_id_model import PatchIdModel
from tests.mocks.scenarios import MockScenarios


@pytest.mark.api
class TestCreateEntity:
    @allure.title("Тест изменения сущности")
    def test_patch_entity(
        self,
        mocker: MockerFixture,
        api_client: APIEntity,
        patch_entity: Tuple[PatchIdModel, CreateAndPatchModel],
        use_api_mocks: bool
    ):

        if use_api_mocks:
            mock_response = MockScenarios.PATCH["positive"]
            mocker.patch.object(
                api_client,
                "patch_entity",
                return_value=mock_response
            )

        response = api_client.patch_entity(*patch_entity)

        if use_api_mocks:
            assert response == mock_response, "Ответ не оответствует моку"
