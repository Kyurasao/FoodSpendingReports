import sqlite3


def main():
    # создаем соединение с нашей базой данных
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # получаем метаданные для таблицы
    cursor.execute("PRAGMA table_info(users)")

    # выводим названия полей таблицы
    fields = cursor.fetchall()
    for field in fields:
        print(field[1])

    # закрываем соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
