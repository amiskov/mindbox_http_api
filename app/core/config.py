import os
from logging import config as logging_config
from pydantic import BaseSettings
from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Config(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME',
                                  'Categories & Products HTTP API')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'mindbox_categories')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', '')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT: int = int(os.getenv('POSTGRES_PORT', 4321))


config = Config()
