import config
import time
import requests
import os
import datetime


class VkPost:
    url = 'https://api.vk.com/method/'

    def __init__(self):
        self.owner_id = config.owner_id
        self.params = {
            'access_token': config.token,
            'v': config.version,
            'owner_id': self.owner_id

        }
        self.params_for_wall_post = {
            'message': config.message,
            'attachments': config.photos
        }

    def send_post(self):
        get_foto_list_url = self.url + 'wall.post'
        response = requests.post(get_foto_list_url, params={**self.params, **self.params_for_wall_post})
        response.raise_for_status()
        if response.status_code == 200:
            print(f'Все нормально, super good')
        return response.status_code


def main():

    def start():
        vkposter = VkPost()
        while True:
            try:
                vkposter.send_post()
                time.sleep(config.time_to_sleep)
            except:
                data = f'{datetime.date} --- {datetime.time} Error'
                path_ = f'{os.getcwd()}/{config.path}'
                with open(path_, 'a', encoding='utf-8') as f:
                    f.write(data + '\n')

    start()


if __name__ == '__main__':
    main()
