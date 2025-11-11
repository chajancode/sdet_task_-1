from config.params import HOST


class Endpoints():
    BASE_URL = f"{HOST}/api"
    CREATE = BASE_URL + "/create"
    DELETE = BASE_URL + "/delete/"
    GET = BASE_URL + "/get/"
    GET_ALL = BASE_URL + "/getAll"
    PATCH = BASE_URL + "/patch/"
