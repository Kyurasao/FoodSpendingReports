from random import choice

import requests

FOOD_NAME = ['tomato', 'potato', 'apple', 'cucumber', 'orange', 'egg', 'chicken']

LIST_OF_NAMES = [
    ['tomato', 'potato', 'apple'],
    ['cucumber', 'orange'],
    ['egg'],
    ['chicken', '123'],
    ['1', '2', '3']
]

LINK = 'http://127.0.0.1:8000/Example003/'


def food_generator():
    return choice(FOOD_NAME)


def name_generator():
    return choice(LIST_OF_NAMES)


def example003():
    data = {
        "example001": {"name": food_generator()},
        "example002": {"list_of_names": name_generator()}
    }
    r = requests.post(LINK, json=data)
    return r.text


if __name__ == '__main__':
    for _ in range(10):
        result = example003()
        print(result)
