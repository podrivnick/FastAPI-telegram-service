import json
from dataclasses import dataclass

from infrastructure.exceptions.base import BaseApplicationException


@dataclass(frozen=True, eq=False)
class BaseWebFlowersServiceException(BaseApplicationException):
    status_code: int
    response_content: str

    @property
    def response_json(self) -> dict:
        return json.loads(self.response_content)

    @property
    def error_text(self) -> str:
        return self.response_json.get("detail", {}).get("error", "")


@dataclass(frozen=True, eq=False)
class FlowerNotReceivedException(BaseWebFlowersServiceException):
    @property
    def message(self):
        return "No flower data received from the API"
