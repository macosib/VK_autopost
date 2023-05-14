import config
import time
import requests
import os
import datetime


def main():
    def start():
        vkposter_main_arenda = VkApi(config.owner_id_main_arenda)
        vkposter_altay_more = VkApi(config.owner_id_altay_more)
        vkposter_altay_arenda_3 = VkApi(config.owner_id_arenda_3)
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
