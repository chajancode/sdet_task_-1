class APIError(Exception):
    def __init__(self, status_code: int, details: str, url: str):
        self.status_code = status_code
        self.details = details
        self.url = url
        super().__init__(f"[{status_code}] {details} (URL: {url})")


class ResponseValidationError(Exception):
    def __init__(self, details: list, url: str):
        self.details = details
        self.url = url
        super().__init__(f"Ошибка валидации {url}: {details}")
