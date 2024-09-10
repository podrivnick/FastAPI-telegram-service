from dataclasses import dataclass
from urllib.parse import urljoin

from domain.arts.dto import GetArtfromAPIResponses
from infrastructure.exceptions.arts import ArtNotReceivedException
from infrastructure.exceptions.flowers import FlowerNotReceivedException
from infrastructure.services.base import BaseWebArtsService
from infrastructure.services.config import (
    GET_RANDOM_ART_URL,
    GET_RANDOM_FLOWER_URL,
)
from infrastructure.services.convertors import (
    convert_json_art_response_to_art_dto,
    convert_json_flower_response_to_flower_dto,
)


@dataclass
class WebArtsService(BaseWebArtsService):
    async def get_random_art(self, art_direction: str) -> GetArtfromAPIResponses:
        response = await self.http_client.post(
            url=urljoin(base=self.base_url, url=GET_RANDOM_ART_URL),
            params={"art_direction": art_direction},
        )

        if not response.is_success:
            raise ArtNotReceivedException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        res = await response.json()

        return convert_json_art_response_to_art_dto(res)


@dataclass
class WebFlowersService(BaseWebArtsService):
    async def get_random_flower(self):
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=GET_RANDOM_FLOWER_URL),
            params={"get_random_flower_photo": True},
        )

        if not response.is_success:
            raise FlowerNotReceivedException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        res = await response.json()

        return convert_json_flower_response_to_flower_dto(res)
