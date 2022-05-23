import sqlite3
from User import *


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.sql = self.db.cursor()
        self.sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            password TEXT,
            name TEXT,
            surname TEXT,
            age TEXT,
            cash INT
        )""")
        self.db.commit()

    def searchUser(self, login):
        self.sql.execute(f"SELECT * FROM users WHERE login = '{login}'")
        row = self.sql.fetchone()
        if row is None:
            return False
        else:
            return True

    def getInfo(self, login):
        self.sql.execute(f"SELECT * FROM users WHERE login = '{login}'")
        row = self.sql.fetchone()
        if row is None:
            return None
        user = User(row[0], row[1], row[2], row[3], row[4], row[5])
        return user

    def show(self):
        self.sql.execute(f"SELECT * FROM users")
        print(self.sql.fetchall())

    def setInfo(self, user):
        self.sql.execute("SELECT login FROM users WHERE login = " + user.login)
        if self.sql.fetchone() is None:
            self.sql.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",
                             (user.login,
                             user.password,
                             user.name,
                             user.surname,
                             user.age,
                             user.cash))
        else:
            self.sql.execute(f"UPDATE users SET "
                             f"login = '{user.login}',"
                             f"password = '{user.password}',"
                             f"name = '{user.name}',"
                             f"surname = '{user.surname}',"
                             f"age = '{user.age}',"
                             f"cash = '{user.cash}'"
                             f"WHERE login = '{user.login}'")
            print('aaaaaaaaaaaa')
        self.db.commit()


    def deleteUser(self, login):
        self.sql.execute(f"DELETE FROM users WHERE login = '{login}'")
        self.db.commit()