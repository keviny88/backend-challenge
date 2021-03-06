from my_database import MyDatabase
from pathlib import Path

if __name__ == '__main__':
    myDB = MyDatabase()
    schema = Path("data_drop/schema.csv")
    data = Path("data_drop/data.csv")

    # If there is not a schema.csv or data.csv in the data_drop folder, cancel the program.
    if not schema.is_file() or not data.is_file():
        print("Missing schema or data file!")
    else:
        name = raw_input("Enter a table name: ")
        print("")
        myDB.create_table(name, schema)
        myDB.insert_data(name, data)
        myDB.show_table(name)


