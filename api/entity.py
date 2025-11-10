from typing import Type, TypeVar
from pydantic import BaseModel, ValidationError
from requests import RequestException, Session

import allure

from Exceptions.APIExceptions import APIError, ResponseValidationError
from endpoints.endpoints import Endpoints
from models.create_and_patch_model import CreateAndPatchModel
from models.get_all_params_model import GetAllParamsModel
from models.get_all_response_model import GetAllResponseModel
from models.get_and_delete_model import GetAndDeleteModel
from models.get_response_model import GetResponseModel
from models.patch_id_model import PatchIdModel


T = TypeVar("T", bound=BaseModel)


class APIEntity:
    def __init__(self, timeout=10):
        self.timeout: int = timeout
        self.session: Session = Session()

    def _request(
                self,
                method: str,
                endpoint: str,
                params=None,
                json=None,
                response_model: Type[T] | None = None
                ):
        try:
            response = self.session.request(
                            method=method,
                            url=endpoint,
                            params=params,
                            json=json,
                            timeout=self.timeout,
            )

            if not response.ok:
                raise APIError(
                    status_code=response.status_code,
                    details=response.text,
                    url=response.url
                )

            if response_model is None:
                match method:
                    case "POST":
                        return response.json()
                    case "DELETE":
                        return
                    case "PATCH":
                        return

            return response_model.model_validate(response.json())

        except ValidationError as e:
            raise ResponseValidationError(
                detail=e.errors(),
                url=response.url if response else endpoint
                ) from e
        except TimeoutError:
            raise APIError(
                status_code=response.status_code,
                details="Истекло время запроса",
                url=endpoint
            )
        except RequestException as e:
            raise APIError(
                status_code=response.status_code,
                details=str(e),
                url=endpoint
            ) from e

    @allure.step("Отправка запроса для создания сущности")
    def create_entity(self, data: CreateAndPatchModel):
        allure.attach(
            str(data),
            name="Передана модель",
            attachment_type=allure.attachment_type.JSON
        )
        return self._request(
            method="POST",
            endpoint=Endpoints.CREATE,
            json=data.model_dump(),
        )

    @allure.step("Отправка запроса для удаления сущности")
    def delete_entity(self, params: GetAndDeleteModel):
        allure.attach(
            str(params),
            name="Передан ID",
            attachment_type=allure.attachment_type.JSON
        )
        return self._request(
            method="DELETE",
            endpoint=f"{Endpoints.DELETE}{params.id}",
            params=params.model_dump(),
            response_model=None
        )

    @allure.step("Отправка запроса для получения сущности")
    def get_entity(self, params: GetAndDeleteModel):
        allure.attach(
            str(params),
            name="Передан ID",
            attachment_type=allure.attachment_type.JSON
        )
        return self._request(
            method="GET",
            endpoint=f"{Endpoints.GET}{params.id}",
            params=params.model_dump(),
            response_model=GetResponseModel
        )

    @allure.step("Отправка запроса для получения списка сущностей")
    def get_all(self, params: GetAllParamsModel):
        allure.attach(
            str(params),
            name="Переданы параметры",
            attachment_type=allure.attachment_type.JSON
        )
        return self._request(
            method="GET",
            endpoint=Endpoints.GET_ALL,
            params=params.model_dump(),
            response_model=GetAllResponseModel
        )

    @allure.step("Отправка запроса для обновления сущности")
    def patch_entity(self, id: PatchIdModel, data: CreateAndPatchModel):
        allure.attach(
            f"ID: {str(id)}, body: {str(data)}",
            name="Передана модель",
            attachment_type=allure.attachment_type.JSON
        )
        return self._request(
            method="PATCH",
            endpoint=f"{Endpoints.PATCH}{id.id}",
            json=data.model_dump()
        )
