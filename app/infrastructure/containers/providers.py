from dishka import (
    provide,
    Provider,
    Scope,
)
from httpx import AsyncClient
from infrastructure.services.base import (
    BaseWebArtsService,
    BaseWebFlowersService,
    BaseWebPoemsService,
)
from infrastructure.services.web import (
    WebArtsService,
    WebFlowersService,
    WebPoemsService,
)
from settings.config import Config
from telegram import Bot


class DefaultProvider(Provider):
    @provide(scope=Scope.APP)
    def get_configs(self) -> Config:
        return Config()

    @provide(scope=Scope.REQUEST)
    def get_http_art_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.REQUEST)
    def get_http_flower_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.REQUEST)
    def get_http_poem_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.REQUEST)
    def get_arts_web_service(self) -> BaseWebArtsService:
        return WebArtsService(
            http_client=self.get_http_art_client(),
            base_url=self.get_configs().WEB_API_URL,
        )

    @provide(scope=Scope.REQUEST)
    def get_flowers_web_service(self) -> BaseWebFlowersService:
        return WebFlowersService(
            http_client=self.get_http_flower_client(),
            base_url=self.get_configs().WEB_API_URL,
        )

    @provide(scope=Scope.REQUEST)
    def get_poems_web_service(self) -> BaseWebPoemsService:
        return WebPoemsService(
            http_client=self.get_http_poem_client(),
            base_url=self.get_configs().WEB_API_URL,
        )

    @provide(scope=Scope.REQUEST)
    def get_telegram_bot(self) -> Bot:
        return Bot(token=self.get_configs().TG_TOKEN)
