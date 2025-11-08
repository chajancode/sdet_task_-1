from typing import Generator, Tuple
import pytest

from api.entity import APIEntity
from data_for_tests.data_for_tests import DataForTests
from models.create_and_patch_model import CreateAndPatchModel
from models.get_all_model import GetAllParamsModel
from models.get_and_delete_model import GetAndDeleteModel
from models.patch_id_model import PatchIdModel


@pytest.fixture(scope="session")
def api_client() -> Generator[APIEntity, None, None]:
    client = APIEntity(timeout=10)
    yield client
    client.session.close()


@pytest.fixture()
def create_entity_data() -> CreateAndPatchModel:
    return DataForTests.create_entity_body


@pytest.fixture()
def delete_params() -> GetAndDeleteModel:
    return DataForTests.delete_entity


@pytest.fixture()
def get_params() -> GetAndDeleteModel:
    return DataForTests.get_entity_id


@pytest.fixture()
def get_all_params() -> GetAllParamsModel:
    return DataForTests.get_all_params


@pytest.fixture()
def patch_entity() -> Tuple[PatchIdModel, CreateAndPatchModel]:
    return (DataForTests.patch_entity_id, DataForTests.patch_entity_body)
