from dataclasses import dataclass
from urllib.parse import urljoin

import boto3
from botocore.exceptions import (
    NoCredentialsError,
    PartialCredentialsError,
)
from domain.arts.dto import GetArtfromAPIResponses
from domain.flowers.dto import GetFlowerfromAPIResponses
from domain.poems.dto import GetPoemfromAPIResponses
from infrastructure.exceptions.arts import ArtNotReceivedException
from infrastructure.exceptions.flowers import FlowerNotReceivedException
from infrastructure.exceptions.poems import PoemNotReceivedException
from infrastructure.services.base import (
    BaseWebArtsService,
    BaseWebFlowersService,
    BaseWebPoemsService,
)
from infrastructure.services.config import (
    GET_RANDOM_ART_URL,
    GET_RANDOM_FLOWER_URL,
    GET_RANDOM_POEM_URL,
)
from infrastructure.services.convertors import (
    convert_json_art_response_to_art_dto,
    convert_json_flower_response_to_flower_dto,
    convert_json_poem_response_poem_dto,
)


@dataclass
class WebArtsService(BaseWebArtsService):
    async def get_random_art(self, art_direction: str) -> GetArtfromAPIResponses:
        response = await self.http_client.post(
            url=urljoin(
                base=self.base_url,
                url=GET_RANDOM_ART_URL,
            ),
            json={"art_direction": art_direction},
            follow_redirects=True,
        )

        if not response.is_success:
            raise ArtNotReceivedException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        res = response.json()

        art_res = convert_json_art_response_to_art_dto(res["result"][0])
        return art_res

    async def get_art_photo_from_remote_storage(
        self,
        storage_name: str,
        storage_path: str,
    ):
        # TODO: create service for getting s3_client
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
        )
        try:
            response = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": storage_name, "Key": storage_path},
                ExpiresIn=self.expiration_photo_link,
            )
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(e)
            return None

        return response


@dataclass
class WebFlowersService(BaseWebFlowersService):
    async def get_random_flower(self) -> GetFlowerfromAPIResponses:
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=GET_RANDOM_FLOWER_URL),
            params={"get_random_flower_photo": True},
            follow_redirects=True,
        )

        if not response.is_success:
            raise FlowerNotReceivedException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        res = response.json()

        flower_res = convert_json_flower_response_to_flower_dto(res["result"][0])
        return flower_res


@dataclass
class WebPoemsService(BaseWebPoemsService):
    async def get_random_poem(self, poem_author: str) -> GetPoemfromAPIResponses:
        response = await self.http_client.post(
            url=urljoin(
                base=self.base_url,
                url=GET_RANDOM_POEM_URL,
            ),
            json={"poem_author": poem_author},
            follow_redirects=True,
        )

        if not response.is_success:
            raise PoemNotReceivedException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        res = response.json()

        poem_res = convert_json_poem_response_poem_dto(res["result"][0])
        return poem_res
