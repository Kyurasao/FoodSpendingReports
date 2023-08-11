import sqlite3
import time


def create(name: str):
    # while True:
    con = sqlite3.connect('example_db.db')
    cur = con.cursor()
    # value = input("type: 'exit' to exit | 'create' to create a new entry \n")
    # if value == 'exit':
    #     break
    # elif value == 'create':
    date_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    # name = input('Enter the name: ')
    cur.execute('INSERT INTO example_table (name, time) VALUES (?, ?)', (name, date_time))
    con.commit()
    con.close()


def read(db, table: str):
    con = sqlite3.connect(db)
    cur = con.cursor()
    for row in cur.execute(f'SELECT id, name, time FROM {table} ORDER BY time'):
        print(row)
    con.close()


def update():
    ...


def delete():
    ...


def main():
    con = sqlite3.connect('example_db.db')
    cur = con.cursor()
    res = cur.execute("""SELECT name FROM sqlite_master WHERE name = 'example_table'""").fetchone()
    if not res:
        print("Table 'example_table' not found!")
        cur.execute("""CREATE TABLE example_table (id INTEGER PRIMARY KEY, name TEXT, time TEXT)""")
        print("Table 'example_table' created")
    else:
        print("Table 'example_table' found!")
    # con.commit()
    con.close()

    create('N')

    read('example_db.db', 'example_table')

    # while True:
    #     value = input("type: 'exit' to exit | 'create' to create a new entry \n")
    #     if value == 'exit':
    #         break
    #     elif value == 'create':
    #         # con = sqlite3.connect('example_db.db')
    #         # cur = con.cursor()
    #         date_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    #         name = input('Enter the name: ')
    #         cur.execute('INSERT INTO example_table (name, time) VALUES (?, ?)', (name, date_time))
    #         con.commit()
    # con.close()


if __name__ == '__main__':
    main()
