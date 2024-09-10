from functools import lru_cache

import environ
from pydantic_settings import BaseSettings


env = environ.Env()
environ.Env.read_env(".env")


class Config(BaseSettings):
    TG_TOKEN: str = env("TELEGRAM_BOT_TOKEN")

    RECIEVED_RANDOM_ART_TOPIC: str = env(
        "RECIEVED_RANDOM_ART_TOPIC",
        default="recieved_random_art",
    )
    RECIEVED_RANDOM_FLOWER_TOPIC: str = env(
        "RECIEVED_RANDOM_FLOWER_TOPIC",
        default="recieved_random_flower",
    )
    RECIEVED_RANDOM_POEM_TOPIC: str = env(
        "RECIEVED_RANDOM_POEM_TOPIC",
        default="recieved_random_poem",
    )

    WEB_API_URL: str = env("WEB_API_URL", default="http://app:8000")
    KAFKA_BROKER_URL: str = env("KAFKA_BROKER_URL", default="kafka:29092")


@lru_cache(1)
def get_config() -> Config:
    return Config()
