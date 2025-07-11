import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

def set_env() -> None:
    dotenv_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


set_env()


class Settings(BaseSettings):
    token: str = Field(alias="TOKEN")

    owner_id_my: str = Field(alias="OWNER_ID_MY")
    owner_id_altay_sea: str = Field(alias="OWNER_ID_ALTAY_SEA")
    owner_id_crazy_summer: str = Field(alias="OWNER_ID_CRAZY_SUMMER")
    owner_id_jarovoe22: str = Field(alias="OWNER_ID_JAROVOE22")
    owner_id_jarovoe_arenda: str = Field(alias="OWNER_ID_YAROVOE_ARENDA")
    telegram_bot_token: str = Field(alias="TG_TOKEN")
    telegram_chat_id: int = Field(alias="TH_CHAT_ID")

    version_vk: str = Field(alias="VERSION_VK", default="5.199")

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


OWNER_ID_ALTAY_SEA = "-974577"
# OWNER_ID_ALTAY_SEA = "https://vk.com/altaysea?from=groups" 13к

OWNER_ID_CRAZY_SUMMER = "-56550271"
# OWNER_ID_CRAZY_SUMMER = "https://vk.com/crazy__summer?from=groups" 4.4к

OWNER_ID_JAROVOE22 = "-146076175"
# OWNER_ID_JAROVOE22 = "https://vk.com/jarovoe22?from=groups" 2.7к

OWNER_ID_YAROVOE_ARENDA = "-145007828"
# OWNER_ID_YAROVOE_ARENDA = "https://vk.com/yarovoe_arenda?from=groups" 2.2k

settings = Settings()