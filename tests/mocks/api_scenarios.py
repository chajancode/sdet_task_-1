from typing import Dict


class MockScenarios:

    CREATE: Dict = {
        "positive": {"value": "12"},
        "negative": 12
    }
    DELETE: Dict = {
        "positive": "201",
        "negative": "400"
    }
    GET_ALL: Dict = {
        "positive": [{"one": 1, "two": 2}, {"three": 3, "four": 4}],
        "negative": {"three": 30}
    }
    GET: Dict = {
        "positive": {"id": 1, "name": "entity"},
        "negative": "400"
    }
    PATCH: Dict = {
        "positive": {"id": 4, "name": "patched"},
        "negative": "500"
    }
