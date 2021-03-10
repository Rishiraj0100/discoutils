"""
MIT License

Copyright (c) 2021 Rishiraj0100

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



import random
import requests
import discord


class random_things():
    def randomColor():
        clist = ['blue', 'blurple', 'dark_blue', 'dark_gold', 'dark_green', 'dark_grey', 'dark_magenta', 'dark_orange', 'dark_purple', 'dark_red', 'dark_teal', 'darker_grey', 'gold', 'green', 'greyple', 'light_grey', 'lighter_grey', 'magenta', 'orange', 'purple', 'red', 'teal']
        return eval(f"discord.Color.{random.choice(clist)}()")

    def random_dog():
        api= "https://random.dog/woof.json"
        data = requests.get(api).json()
        image = data['url']
        return image

    def random_cat():
        api ="https://some-random-api.ml/img/cat"
        data = requests.get(api).json()
        img = data['link']
        return img
