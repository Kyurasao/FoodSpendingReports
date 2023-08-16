import sqlite3
import time
from webserver.test_webserver import con


ENTRIES = [
    ('Anton', '13.08.2023 02:36:50'),
    ('Oleg', '13.08.2023 02:43:56'),
    ('Nikita', '13.08.2023 02:44:39'),
    ('Anna', '13.08.2023 03:14:27'),
    ('Olga', '13.08.2023 03:14:36'),
    ('Elena', '13.08.2023 03:14:49'),
    ('Maria', '13.08.2023 03:15:24'),
]

UPDATE_ENTRIES = [
    ('OLEG', 2),
    ('OLGA', 7),
    ('NIKITA', 3),
]

DELETE_ENTRIES = [
    (4,),
]


# def create(name: str):
#     try:
#         # con = sqlite3.connect('request_db.db')
#         cur = con.cursor()
#         print("The database 'request_db.db' is connected to SQLite")
#         date_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
#         cur.execute('INSERT INTO request (name, time) VALUES (?, ?)', (name, date_time))
#         con.commit()
#         print("The entry has been successfully entered into the table 'request'")
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")
#
#
# def create_many(entry_data: list[tuple]):
#     try:
#         # con = sqlite3.connect('request_db.db')
#         cur = con.cursor()
#         print("The database 'request_db.db' is connected to SQLite")
#         cur.executemany('INSERT INTO request (name, time) VALUES (?, ?)', entry_data)
#         con.commit()
#         print("The entry has been successfully entered into the table 'request'")
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")


def read_all(table: str):
    try:
        # con = sqlite3.connect(db)
        cur = con.cursor()

        res = cur.execute(f'SELECT id, name, time FROM {table} ORDER BY time')
        print(f"Read all rows from {table}")
        for row in res.fetchall():
            print(row)

        # зачем нужен fetchall, если можно ввести вот так? Потому что cur.execute - это ссылка на ячейку памяти,
        # а в результате .fetchall() получаем список всех значений в таблице
        # fetchone() выводит первую строку из таблицы

        # for row in cur.execute(f'SELECT id, name, time FROM {table} ORDER BY time'):
        #     print(row)

        cur.close()
        # con.close()

    except sqlite3.Error as error:
        print("Error when working with SQLite! |", error)

    # finally:
    #     if con:
    #         # cur.close()
    #         con.close()
    #         print("Connection to SQLite is closed")


# def read_many(db, table: str, size: int):
#     try:
#         # con = sqlite3.connect(db)
#         cur = con.cursor()
#         res = cur.execute(f'SELECT id, name, time FROM {table} ORDER BY time')
#
#         # откуда начинает выводить fetchmany, что является начальным значенмем?
#         # как продолжить вывод с последнего значения
#         print(f"Read first {size} rows from 'request'")
#         for row in res.fetchmany(size):
#             print(row)
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")
#
#
# def update_name(db, table, name: str, num: int):
#     try:
#         # con = sqlite3.connect(db)
#         cur = con.cursor()
#         cur.execute(f"""UPDATE {table} SET name = ?
#                     WHERE id = ?""", (name, num))
#         con.commit()
#         print(f"The entry has been successfully updated")
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")
#
#
# def update_many_name(db, table, update_data: list[tuple]):
#     try:
#         # con = sqlite3.connect(db)
#         cur = con.cursor()
#         cur.executemany(f"""UPDATE {table} SET name = ?
#                     WHERE id = ?""", update_data)
#         con.commit()
#         print(f"The {cur.rowcount} entry/ies has been successfully updated")
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")
#
#
# def delete(db, table: str, delete_data: list[tuple]):
#     try:
#         # con = sqlite3.connect(db)
#         cur = con.cursor()
#         cur.executemany(f"""DELETE FROM {table}
#                     WHERE id = ?""", delete_data)
#         con.commit()
#         print(f"The {cur.rowcount} entry/ies has been successfully deleted")
#         cur.close()
#         # con.close()
#
#     except sqlite3.Error as error:
#         print("Error when working with SQLite", error)
#
#     finally:
#         if con:
#             # cur.close()
#             con.close()
#             print("Connection to SQLite is closed")
#

def main():
    try:
        # con = sqlite3.connect('request_db.db')
        cur = con.cursor()
        print("The database 'request_db.db' is connected to SQLite")
        res = cur.execute("""
                          SELECT name FROM sqlite_master
                          WHERE name = 'request'
        """).fetchone()
        if not res:
            print("Table 'request' not found!")
            cur.execute("""
                        CREATE TABLE request
                            (id INTEGER PRIMARY KEY,
                             name TEXT,
                             time TEXT)
            """)
            print("Table 'request' created")
        else:
            print("Table 'request' found!")
        cur.close()
        # con.close()

    except sqlite3.Error as error:
        print("Error connecting to SQLite", error)

    # finally:
    #     if con:
    #         cur.close()
    #         con.close()
    #         print("Connection to SQLite is closed")

    # create('Maria')

    # create_many(ENTRIES)

    # read_all('request_db.db', 'request')

    # read_many('request_db.db', 'request', 3)

    # update_name('request_db.db', 'request', 'Alexandr', 4)

    # update_many_name('request_db.db', 'request', UPDATE_ENTRIES)

    # delete('request_db.db', 'request', DELETE_ENTRIES)

    read_all('request')


if __name__ == '__main__':
    main()

"""
как правильно расположить закрытие курсора и соединения 
в main, для каких ошибок сделана обратботка исключений
(только для ошибок в соединении?), может ли произойти 
ошибка при создании объекта курсора
"""
