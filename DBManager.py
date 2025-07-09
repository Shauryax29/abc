import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("record.db")
        self.cursor = self.conn.cursor()
        print("Connected")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR(20) PRIMARY KEY,
            email VARCHAR(10) NOT NULL,
            password VARCHAR(20)
        )
        """)
        self.conn.commit()
        print("Table created")

    def saveUser(self, **u):
        try:
            self.cursor.execute("""
            Insert into users (name, email, password) VALUES (?, ?, ?)
            """, (u['name'], u['email'], u['password']))
            self.conn.commit()
            return 1
        except sqlite3.IntegrityError:
            return 2
        # self.showUser(username=u['username'], password=u['password'])
        # return True

    def showUser(self, **u):
        self.cursor.execute('select count(*) from users where email=? and password= ?', (u['email'],u['password']))
        result = self.cursor.fetchall()
        if result[0][0]==1:
            return True
        else:
            return False
        