from time import sleep

import requests

from app.vk_api import VkApi

from logger.logger import get_logger
from settings.settings import settings

logger = get_logger(__name__)


def notify_on_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger.error(f"Ошибка в функции {func.__name__}: {err}")
            send_telegram_message(f"❗️Ошибка в функции <b>{func.__name__}</b>:\n<pre>{err}</pre>")
    return wrapper


def send_telegram_message(message: str):
    BOT_TOKEN = settings.telegram_bot_token
    CHAT_ID = settings.telegram_chat_id
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения в Telegram: {e}")


@notify_on_error
def start():
    print("Приложение запущено")
    altay_sea = VkApi(settings.owner_id_altay_sea)
    crazy__summer = VkApi(settings.owner_id_crazy_summer)
    club117687082 = VkApi(settings.owner_id_club117687082)
    our = VkApi(settings.owner_id_my)

    while True:
        for vk_instance in (altay_sea, crazy__summer, club117687082):
            check_our_post_in_wall(vk_instance)
        sleep(180)


@notify_on_error
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


