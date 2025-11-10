from unittest.mock import Mock

from tests.mocks.api_scenarios import MockScenarios
from tests.test_api.test_create_entity import TestCreateEntity


def get_mock_response(method, scenario="positive"):
    match method:
        case "CREATE":
            return MockScenarios.CREATE[scenario]
        case "DELETE":
            return MockScenarios.DELETE[scenario]


def create_mock_by_method(client: TestCreateEntity, method: str, scenario="positive"):
    # method = client.method
    mock = Mock()
    mock.return_value = get_mock_response(method=method, scenario=scenario)
    client.create_entity = mock
    return mock
