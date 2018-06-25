import sqlite3
import csv
sqlite_file = 'my_db.sqlite'

class MyDatabase:

    sqlite_file = 'my_db.sqlite'

    def __init__(self):
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()

    def create_table(self, name, schema):
        self.c.execute("DROP TABLE IF EXISTS " + name)
        sql_create_table = "CREATE TABLE IF NOT EXISTS " + name + "("

        with open(schema, "r") as f:
            reader = csv.reader(f, delimiter = "\t")
            next(f)
            for line in reader:
                try:
                    field_name, width, type = line[0].split(',')
                except ValueError:
                    print("Value for this line does not have three fields")
                    continue
                sql_create_table += " {} {}({}),".format(field_name, type, width)

        sql_create_table= sql_create_table.rstrip(",") + ");"
        self.c.execute(sql_create_table)
        self.conn.commit()

    # Since we are inserting data a CSV at a time, we will use batch updates for speed optimization
    def insert_data(self, name, data_file):
        # First we create the SQL batch statement
        headers = self.get_headers(name)
        sql_insert = "INSERT INTO " + name + "("

        for field in headers:
            sql_insert += field + ","
        sql_insert = sql_insert.rstrip(",") + ") VALUES ("

        # We look at the length of headers to know how many '?' to add to the statement
        for i in range(len(headers)):
            sql_insert += "?" + ","
        sql_insert = sql_insert.rstrip(",") + ")"

        # Next we gather the data from the CSV and put it into a list
        # We optimize database update speed, which requires extra space
        data = []
        with open(data_file, "r") as f:
            reader = csv.reader(f, delimiter="\t")
            for line in reader:
                entry = tuple([x for x in line[0].split(",")])

                # If length of tuple is not equal to header list length, then this entry is invalid
                if len(entry) == len(headers):
                    data.append(entry)
                else:
                    print("Entry has wrong number of columns!")

        self.c.executemany(sql_insert, data)

    # Creating a a visual representation of the table
    def show_table(self, name):
        # Extract the header names and print them out
        header_string = ""
        for title in self.get_headers(name):
            header_string += title + "  | "
        print(header_string)

        self.c.execute("SELECT * FROM " + name)
        rows = self.c.fetchall()
        for row in rows:
            row_string = ""
            for col in row:
                row_string += str(col) + "  | "
            print(row_string)

    # Gets headers for a table and returns them in a list
    def get_headers(self, name):
        self.c.execute("PRAGMA table_info({})".format(name))
        return [row[1] for row in self.c.fetchall()]

    def __del__(self):
        self.conn.close()

x = MyDatabase()
x.create_table('authors', 'schema.csv')
x.insert_data('authors', 'data.csv')
x.show_table('authors')
# x.show_table('authors')


