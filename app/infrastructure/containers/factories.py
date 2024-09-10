from functools import lru_cache

from app.infrastructure.containers.providers import DefaultProvider
from dishka import (
    AsyncContainer,
    make_async_container,
)


@lru_cache(1)
def get_container() -> AsyncContainer:
    return make_async_container(DefaultProvider())
