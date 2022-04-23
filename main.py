import config
import time
import requests
import os
import datetime


class VkPost():
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

    @staticmethod
    def __error_func(error: dict):
        print('Error')
        data = f'Error ID: {error.get("error_code")}, ' \
               f'Error message: {error.get("error_msg")},' \
               f'Datetime: {datetime.datetime.now()}'
        path_ = f'{os.getcwd()}/{config.path}'
        with open(path_, 'a', encoding='utf-8') as f:
            f.write(data + '\n')

    def send_post(self):
        get_foto_list_url = self.url + 'wall.post'
        response = requests.post(get_foto_list_url, params={**self.params, **self.params_for_wall_post, })
        response.raise_for_status()
        if response.status_code != 200 or response.json().get('error') is not None:
            VkPost.__error_func(response.json().get('error'))
            raise Exception
        else:
            print(f'Функция {self.send_post.__name__} успешно отработала {datetime.datetime.now()}')

    def send_post_board(self):
        get_foto_list_url = self.url + 'board.createComment'
        response = requests.post(get_foto_list_url, params={**self.params, **self.params_for_wall_post_board})
        response.raise_for_status()
        if response.status_code != 200 or response.json().get('error') is not None:
            VkPost.__error_func(response.json().get('error'))
            raise Exception
        else:
            print(f'Функция {self.send_post_board.__name__} успешно отработала {datetime.datetime.now()}')

def main():
    def start():
        vkposter_main_arenda = VkPost(config.owner_id_main_arenda)
        vkposter_altay_more = VkPost(config.owner_id_altay_more)
        vkposter_altay_arenda_3 = VkPost(config.owner_id_arenda_3)
        while True:
            try:
                vkposter_main_arenda.send_post()
                time.sleep(0.33)
                vkposter_main_arenda.send_post_board()
                time.sleep(0.33)
                vkposter_altay_more.send_post()
                time.sleep(0.33)
                vkposter_altay_arenda_3.send_post()
                time.sleep(config.time_to_sleep)
            except:
                time.sleep(1200)

    start()


if __name__ == '__main__':
    main()
