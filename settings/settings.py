from pydantic import BaseModel, BaseSettings, Field


class SubModel(BaseModel):
    foo = 'bar'
    apple = 1


class Settings(BaseSettings):
    token: str = Field(env='TOKEN')
    owner_id_my: str = Field(env='OWNER_ID_MY')
    owner_id_yarovoe_arenda: str = Field(env='OWNER_ID_YAROVOE_ARENDA')
    owner_id_altay_sea: str = Field(env='OWNER_ID_ALTAY_SEA')
    owner_id_crazy__summer: str = Field(env='OWNER_ID_CRAZY_SUMMER')
    topic_id_yarovoe_arenda: str = Field(env='TOPIC_ID_YAROVOE_ARENDA')
    version_vk: str = Field(env='VERSION_VK')

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
