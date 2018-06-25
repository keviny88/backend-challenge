import sqlite3
import csv
sqlite_file = 'my_db.sqlite'

class MyDatabase:

    sqlite_file = 'my_db.sqlite'

    def __init__(self):
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()

    def create_table(self, schema, name):
        self.c.execute("DROP TABLE IF EXISTS " + name)
        sql_create_table = "CREATE TABLE IF NOT EXISTS " + name + "("

        with open(schema, "r") as f:
            reader = csv.reader(f, delimiter = "\t")
            next(f)
            for line in (reader):
                try:
                    field_name, width, type = line[0].split(',')
                except ValueError:
                    print("Value for this line does not have three fields")
                    continue

                sql_create_table += " {} {}({}),".format(field_name, type, width)

        sql_create_table= sql_create_table.rstrip(",")
        sql_create_table += ");"
        self.c.execute(sql_create_table)
        self.conn.commit()

    # Creating a a visual representation of the table
    def show_table(self, name):
        # Extract the header names and print them out
        header = ""
        for title in self.get_headers(name):
            header += title + "  | "
        print(header)


    def insert_data(self, data_file):
        pass


    # Gets headers for a table and returns them in a list
    def get_headers(self, name):
        self.c.execute("PRAGMA table_info({})".format(name))
        return [row[1] for row in self.c.fetchall()]



x = MyDatabase()
x.create_table('schema.csv', 'authors')
print(x.get_headers('authors'))
# x.show_table('authors')
x.conn.close()


