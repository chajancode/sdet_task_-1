import requests
from requests import Session

from endpoints.endpoints import Endpoints
from models.create_and_patch_model import MainModel
from models.get_all_model import GetAllParamsModel
from models.get_and_delete_model import GetAndDeleteModel


class APIEntity:
    def __init__(self, timeout=10):
        self.timeout: int = timeout
        self.session: Session = Session()

    def _request(
                self,
                method: str,
                endpoint: str,
                params=None,
                json=None
                ):

        response = self.session.request(
                        method=method,
                        url=endpoint,
                        params=params,
                        json=json,
                        timeout=self.timeout
        )
        return response

    def create_entity(self, data: MainModel):
        response = self._request(
            method="POST",
            endpoint=Endpoints.CREATE,
            json=data.model_dump()
        )
        return response

    def delete_entity(self, data: GetAndDeleteModel):
        response = self._request(
            method="DELETE",
            endpoint=f"{Endpoints.DELETE}{data.id}"
        )
        return response

    def get_entity(self, data: GetAndDeleteModel):
        response = self._request(
            method="GET",
            endpoint=f"{Endpoints.GET}{data.id}"
        )
        return response

    def get_all(self, params: GetAllParamsModel):
        response = self._request(
            method="GET",
            endpoint=Endpoints.GET_ALL,
            params=params.model_dump()
        )
        return response
