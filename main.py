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


    def send_post(self):
        get_foto_list_url = self.url + 'wall.post'
        response = requests.post(get_foto_list_url, params={**self.params, **self.params_for_wall_post, })
        response.raise_for_status()
        print(response.status_code)
        print(response.json())
        if response.status_code == 200:
            print(f'Все нормально, super good')
        return response.status_code


    def send_post_board(self):
        get_foto_list_url = self.url + 'board.createComment'
        response = requests.post(get_foto_list_url, params={**self.params, **self.params_for_wall_post_board})
        response.raise_for_status()
        print(response.status_code)
        print(response.json())
        if response.status_code == 200:
            print(f'Все нормально, super good')
        return response.status_code

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
                # vkposter_altay_more.send_post()
                # time.sleep(0.33)
                # vkposter_altay_arenda_3.send_post()
                # time.sleep(config.time_to_sleep)
            except:
                data = f'{datetime.datetime.now()} Error'
                path_ = f'{os.getcwd()}/{config.path}'
                with open(path_, 'a', encoding='utf-8') as f:
                    f.write(data + '\n')
            break
    start()


if __name__ == '__main__':
    main()
    print()