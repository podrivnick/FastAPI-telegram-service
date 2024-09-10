from dataclasses import dataclass
from urllib.parse import urljoin

from app.domain.arts.dto import GetArtfromAPIResponses
from app.infrastructure.exceptions.arts import ArtNotReceivedException
from app.infrastructure.services.config import GET_RANDOM_ART_URL
from app.infrastructure.services.convertors import convert_json_response_to_art_dto
from app.infrastructure.services.services import BaseWebArtsService


@dataclass  # noqa
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

        return convert_json_response_to_art_dto(res)
