"""
This is a program for collecting the amount of food eaten and issuing reports.
Users will be asked for information about their daily diet, and
a report on the amount of food eaten per day will be issued.
"""

import json
import time
from pathlib import Path
from typing import List


def create_meal(meals: list):
    details = {}
    dish = 0
    print(f"Let's enter meal data...")
    date_time_string = input("Enter time of meal | 'now' or date in format [dd.mm.yyyy hh:mm:ss]: \n")
    date_time = time.strftime('%d.%m.%Y %H:%M:%S',
                              time.localtime(time.time())) if date_time_string == 'now' else date_time_string

    while True:
        meal_list = []
        dish += 1
        print("Let's enter the composition of the MEAL...")
        value = input("type: 'finish' to exit | 'add' to add more \n")
        if value == 'finish':
            break
        elif value == 'add':

            while True:
                print("Let's enter the composition of the DISH...")
                value = input(
                    "type: 'finish' to exit | 'add' to add more \n")  # исправить ошибку: неправильный ввод finish или add
                if value == 'finish':
                    break
                elif value == 'add':
                    food = input('Enter the name of the food: \n')
                    amount = input('Enter the amount of the food: \n')
                    meal_list.append({food: amount})
                else:
                    print(f'Unknown value. Once again...')
            details['Dish ' + str(dish)] = meal_list

        else:
            print(f'Unknown value. Once again...')

    # adding details to list of expenses
    meals.append({date_time: details})


def main():
    # read db file
    p = Path('db.json')
    with p.open('r') as file:
        file_data = file.read()
        meals: List = json.loads(file_data) if file_data else []

    while True:
        value = input("type: 'exit' to exit | 'list' to list all meals "
                      "| 'create' to create more | [number of the line] to edit \n")
        if value == 'exit':
            break
        elif value == 'create':
            create_meal(meals=meals)
        elif value == 'list':
            for index, expense in enumerate(meals):
                print(f'[{index + 1}] {expense}')
        elif value.isdigit():
            if 0 < int(value) <= len(meals):
                print(meals[int(value) - 1])
            else:
                print(f'wrong value, we have only [1:{len(meals)}]')
        else:
            print(f'Unknown value. Once again...')
    # saving final data
    with p.open('w+') as file:
        json.dump(meals, file)


if __name__ == '__main__':
    main()
