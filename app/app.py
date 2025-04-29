from time import sleep

from app.vk_api import VkApi

from logger.logger import get_logger
from settings.settings import settings

logger = get_logger(__name__)


def start():
    print("Приложение запущено")
    altay_sea = VkApi(settings.owner_id_altay_sea)
    crazy__summer = VkApi(settings.owner_id_crazy_summer)
    club117687082 = VkApi(settings.owner_id_club117687082)
    our = VkApi(settings.owner_id_my)

    while True:
        try:
            check_our_post_in_wall(altay_sea)
        except Exception as err:
            logger.error(err)
        try:
            check_our_post_in_wall(crazy__summer)
        except Exception as err:
            logger.error(err)
        try:
            check_our_post_in_wall(club117687082)
        except Exception as err:
            logger.error(err)


        sleep(180)


def check_our_post_in_wall(vk: VkApi):
    posts = vk.get_post_wall()
    posts_id_list = [post.id for post in posts.response.items]
    if vk.last_post_id is None:
        current_post = vk.send_post_wall()
        vk.last_post_id = current_post.response.post_id
    elif vk.last_post_id not in posts_id_list:
        vk.delete_post_wall(vk.last_post_id)
        current_post = vk.send_post_wall()
        vk.last_post_id = current_post.response.post_id
