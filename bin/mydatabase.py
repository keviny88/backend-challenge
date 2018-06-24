import sqlite3
sqlite_file = 'my_db.sqlite'

class MyDatabase:
    sqlite_file = 'my_db.sqlite'

    def __init__(self):
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()

    def create_table(self, schema, name):
        self.c.execute("DROP TABLE IF EXISTS " + name)
        




MyDatabase()


