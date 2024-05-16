import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent

def set_env() -> None:
    dotenv_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


set_env()


class Settings(BaseSettings):
    token: str = Field(env="TOKEN")
    owner_id_my: str = Field(env="OWNER_ID_MY")
    owner_id_yarovoe_arenda: str = Field(env="OWNER_ID_YAROVOE_ARENDA")
    owner_id_altay_sea: str = Field(env="OWNER_ID_ALTAY_SEA")
    owner_id_crazy_summer: str = Field(env="OWNER_ID_CRAZY_SUMMER")
    topic_id_yarovoe_arenda: str = Field(env="TOPIC_ID_YAROVOE_ARENDA")
    topic_id_2024: str = Field(env="TOPIC_ID_YAROVOE_2024")
    topic_id_2024_1: str = Field(env="TOPIC_ID_YAROVOE_2024_1")
    topic_id_2024_2: str = Field(env="TOPIC_ID_YAROVOE_2024_2")
    version_vk: str = Field(env="VERSION_VK")

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
