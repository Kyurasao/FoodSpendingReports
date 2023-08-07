import string
from datetime import datetime, timedelta
from random import randint, choice

import requests

DISH_NAME = ['Dish_1', 'Dish_2', 'Dish_3', 'Dish_4']

FOOD_NAME = ['tomato', 'potato', 'apple', 'cucumber', 'orange', 'egg', 'chicken']

LINK = 'http://127.0.0.1:8000/Example001/'


def time_generator():
    random_string = ''.join(choice(string.ascii_letters) for _ in range(10))

    now = datetime.now()  # получаем текущую дату и время

    # создаем объект типа timedelta, который представляет разницу
    delta = timedelta(minutes=randint(1, 5))  # выбираем случайное количество минут
    random_time = str(now - delta)
    return random_time if choice([1, 2]) == 1 else random_string


def name_generator():
    return choice(DISH_NAME)


def food_generator():
    return choice(FOOD_NAME)


def amount_generator():
    return str(randint(1, 10))


def example001():
    data = {
        "food": food_generator(),
    }
    r = requests.post(LINK, json=data)
    return r.text


if __name__ == '__main__':
    for _ in range(10):
        result = example001()
        print(result)
