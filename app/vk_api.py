import datetime
import os

import requests


class VkApi():
    url = 'https://api.vk.com/method/'

    def __init__(self, group_id):
        self.owner_id = group_id
        self.params = {
            'access_token': config.token,
            'v': config.version
        }
        self.params_for_wall_post = {
            'owner_id': self.owner_id,
            'message': config.message,
            'attachments': config.photos
        }
        self.params_for_wall_post_board = {
            'group_id': self.owner_id[1:],
            'message': config.message,
            'attachments': config.photos,
            'topic_id': config.topic_id_main_arenda
        }


    def send_post(self):
        endpoint = self.url + 'wall.post'
        response = requests.post(endpoint, params={**self.params, **self.params_for_wall_post, })
        response.raise_for_status()
        if response.status_code != 200 or response.json().get('error') is not None:
            raise Exception
        else:
            print(f'Функция {self.send_post.__name__} успешно отработала {datetime.datetime.now()}')

    def send_post_board(self):
        endpoint = self.url + 'board.createComment'
        response = requests.post(endpoint, params={**self.params, **self.params_for_wall_post_board})
        response.raise_for_status()
        if response.status_code != 200 or response.json().get('error') is not None:
            raise Exception
        else:
            print(f'Функция {self.send_post_board.__name__} успешно отработала {datetime.datetime.now()}')
