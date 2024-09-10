from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.arts.dto import GetArtfromAPIResponses
from httpx import AsyncClient


@dataclass
class BaseWebArtsService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_random_art(self) -> GetArtfromAPIResponses:
        raise NotImplementedError()


@dataclass
class BaseWebFlowersService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_random_flower(self) -> None:
        raise NotImplementedError()
