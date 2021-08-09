import random
import requests
import discord


class RandomThings:
    def __init__(self):
        pass

    def Color():
        clist = ['blue', 'blurple', 'dark_blue', 'dark_gold', 'dark_green', 'dark_grey', 'dark_magenta', 'dark_orange', 'dark_purple', 'dark_red', 'dark_teal', 'darker_grey', 'gold', 'green', 'greyple', 'light_grey', 'lighter_grey', 'magenta', 'orange', 'purple', 'red', 'teal']
        return eval(f"discord.Color.{random.choice(clist)}()")

    def Dog():
        api= "https://random.dog/woof.json"
        data = requests.get(api).json()
        image = data['url']
        return image

    def Cat():
        api ="https://some-random-api.ml/img/cat"
        data = requests.get(api).json()
        img = data['link']
        return img
