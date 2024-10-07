from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.arts.dto import GetArtfromAPIResponses
from domain.flowers.dto import GetFlowerfromAPIResponses
from domain.poems.dto import GetPoemfromAPIResponses
from httpx import AsyncClient


@dataclass
class BaseWebArtsService(ABC):
    http_client: AsyncClient
    base_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    region_name: str
    expiration_photo_link: int

    @abstractmethod
    async def get_random_art(self) -> GetArtfromAPIResponses:
        raise NotImplementedError()

    @abstractmethod
    async def get_art_photo_from_remote_storage(
        self,
        storage_name: str,
        storage_path: str,
    ):
        raise NotImplementedError()


@dataclass
class BaseWebFlowersService(ABC):
    http_client: AsyncClient
    base_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    region_name: str
    expiration_photo_link: int

    @abstractmethod
    async def get_random_flower(self) -> GetFlowerfromAPIResponses:
        raise NotImplementedError()

    @abstractmethod
    async def get_flower_photo_from_remote_storage(
        self,
        storage_name: str,
        storage_path: str,
    ):
        raise NotImplementedError()


@dataclass
class BaseWebPoemsService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_random_poem(self) -> GetPoemfromAPIResponses:
        raise NotImplementedError()
