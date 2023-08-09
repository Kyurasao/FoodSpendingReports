import sqlite3
import time


def main():
    # conn = sqlite3.connect('example.db')
    # cursor = conn.cursor()  # зачем эта строка??
    # # time TEXT, time: Union[str, datetime]
    # ... if cursor.execute else cursor.execute('''CREATE TABLE example
    #                (id INTEGER PRIMARY KEY,
    #                 name TEXT,
    #                 time TEXT)''')
    # conn.close()

    # # Проверка наличия базы данных
    # global conn
    # try:
    #     conn = sqlite3.connect('example.db')
    # except sqlite3.Error as e:
    #     if e.args[0] == 'table mytable does not exist':
    #         # Создание базы данных и таблиц
    #         conn = sqlite3.connect('example.db')
    #         c = conn.cursor()
    #         c.execute('''CREATE TABLE example
    #                   (id INTEGER PRIMARY KEY,
    #                    name TEXT,
    #                    time TEXT)''')
    #         conn.commit()  # зачем эта строка??
    #         print('База данных создана')
    #     else:
    #         print(f'Ошибка при создании базы данных: {e}')
    # finally:
    #     # Закрытие соединения
    #     conn.close()

    global con
    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE example
                       (id INTEGER PRIMARY KEY,
                        name TEXT,
                        time TEXT)''')
        rows = cur.fetchall()
        if len(rows) > 0:
            print('Table exists')
        else:
            # cur.execute(f"CREATE TABLE mytable(name text, time text)")
            cur.execute('''CREATE TABLE example
                                   (id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    time TEXT)''')
            con.commit()
            print('Table created')

    except sqlite3.OperationalError:
        print('Database doesn’t exist')
    finally:
        con.close()

    while True:
        value = input("type: 'exit' to exit | 'create' to create a new entry \n")
        if value == 'exit':
            break
        elif value == 'create':
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()  # зачем эта строка??
            date_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
            name = input('Enter the name: ')
            cursor.execute('INSERT INTO example (name, time) VALUES (?, ?)', (name, date_time))
            conn.commit()
            conn.close()


if __name__ == '__main__':
    main()
