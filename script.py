import sqlite3
import time


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
    # con.close()

    while True:
        value = input("type: 'exit' to exit | 'create' to create a new entry \n")
        if value == 'exit':
            break
        elif value == 'create':
            # con = sqlite3.connect('example_db.db')
            # cur = con.cursor()
            date_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
            name = input('Enter the name: ')
            cur.execute('INSERT INTO example_table (name, time) VALUES (?, ?)', (name, date_time))
            con.commit()
    con.close()


if __name__ == '__main__':
    main()
