import requests

import utils.utils as utils
from logger.logger import get_logger
from schema.schema import APIResponsePostGet, APIResponseWallPost, APIResponseDeletePost
from settings.settings import settings

logger = get_logger(__name__)


class VkApi:
    base_url = "https://api.vk.com/method"

    def __init__(self, group_id):
        self.owner_id = group_id
        self.params = {
            "access_token": settings.token,
            "v": settings.version_vk
        }
        self.last_post_id = None

    def send_post_wall(self) -> APIResponseWallPost | None:
        endpoint = f"{self.base_url}/wall.post"
        params_for_wall_post = {
            "owner_id": self.owner_id,
            "message": utils.message,
            "attachments": utils.photos,
        }

        response = requests.post(
            url=endpoint, params={**self.params, **params_for_wall_post}
        )
        if response.status_code != 200 or response.json().get("error"):
            logger.error(
                f"Не удалось создать пост, статус код - {response.status_code}, ответ сервера - {response.text}")
            return
        logger.info(f"Создана запись в сообществе {self.owner_id} - {response.json()}")
        return APIResponseWallPost.parse_obj(response.json())

    def delete_post_wall(self, post_id: int) -> APIResponseDeletePost | None:
        endpoint = f"{self.base_url}/wall.delete"
        params_for_wall_post = {
            "owner_id": self.owner_id,
            "post_id": post_id,
        }
        response = requests.post(
            url=endpoint, params={**self.params, **params_for_wall_post}
        )
        if response.status_code != 200 or response.json().get("error"):
            logger.error(
                f"Не удалось удалить запись {post_id}, статус код - {response.status_code}, ответ сервера - {response.text}")
            return
        logger.info(f"Удалена запись {post_id} в сообществе {self.owner_id} - {response.json()}")
        return APIResponseDeletePost.parse_obj(response.json())

    def get_post_wall(self) -> APIResponsePostGet | None:
        endpoint = f"{self.base_url}/wall.get"
        params_for_wall_post = {
            "owner_id": self.owner_id,
            "count": 7,
            "offset": 0
        }

        response = requests.post(
            url=endpoint, params={**self.params, **params_for_wall_post}
        )
        if response.status_code != 200 or response.json().get("error"):
            logger.error(
                f"Не удалось получить посты со стены сообщества {self.owner_id}, статус код - {response.status_code}, ответ сервера - {response.text}")
            return
        return APIResponsePostGet.parse_obj(response.json())


    def send_post_topic(self):
        endpoint = f"{self.base_url}/board.createComment"
        params_for_wall_post_board = {
            "group_id": self.owner_id[1:],
            "message": utils.message,
            "attachments": utils.photos,
            "topic_id": settings.topic_id_yarovoe_arenda,
        }
        response = requests.post(
            endpoint, params={**self.params, **params_for_wall_post_board}
        )
        if response.status_code != 200 or response.json().get("error"):
            logger.error(
                f"Не удалось создать пост, статус код - {response.status_code}, ответ сервера - {response.text}")
            return
        logger.info(f"Создана запись в обсуждении сообщества {self.owner_id} - {response.json()}")
        return APIResponsePostTopic.parse_obj(response.json())


