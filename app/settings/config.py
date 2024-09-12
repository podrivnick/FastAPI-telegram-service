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

    GREETING_TEXT: str = env(
        "GREETING_TEXT",
        default=(
            "Добро пожаловать в бот сеющий прекрасное.\n"
            "Пожалуйста выберите чтобы Вы хотели посмотреть."
        ),
    )

    AWS_ACCESS_KEY_ID: str = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = env("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME: str = env("AWS_REGION_NAME", default="us-east-1")
    EXPIRATION_PHOTO_LINK: int = env("EXPIRATION_PHOTO", default=3600)


@lru_cache(1)
def get_config() -> Config:
    return Config()
