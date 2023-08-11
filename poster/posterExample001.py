from random import choice

import requests

FOOD_NAME = ['tomato', 'potato', 'apple', 'cucumber', 'orange', 'egg', 'chicken']

LINK = 'http://127.0.0.1:8000/Example001/'


def food_generator():
    return choice(FOOD_NAME)


def example001():
    data = {
        "name": food_generator()
    }
    r = requests.post(LINK, json=data)
    return r.text


if __name__ == '__main__':
    for _ in range(10):
        result = example001()
        print(result)
