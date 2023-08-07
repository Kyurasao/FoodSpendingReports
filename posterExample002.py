from random import choice

import requests

LIST_OF_NAMES = [
    ['tomato', 'potato', 'apple'],
    ['cucumber', 'orange'],
    ['egg'],
    ['chicken', '123'],
    ['1', '2', '3']
]

LINK = 'http://127.0.0.1:8000/Example002/'


def name_generator():
    return choice(LIST_OF_NAMES)


def example002():
    data = {
        "list_of_names": name_generator()
    }
    r = requests.post(LINK, json=data)
    return r.text


if __name__ == '__main__':
    for _ in range(10):
        result = example002()
        print(result)
