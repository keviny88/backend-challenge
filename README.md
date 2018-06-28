BACK END CODE CHALLENGE

Installation Prerequisites
--------------------------
Python v3.6.4
- I am using Python for its readability, ease of use, and position as the primary language of the company's backend. For the database, I will be using SQLite, as it is already included in Python and will allow anybody to run this with ease without having to host on a server.

Assumptions
------------
- This application will only take in two files, both of which are already in the "data_drop" folder
- The description makes it seem like we can assume that there will only be one table, with its schema described in the file, "schema.csv". I allowed my program, and many of the class methods, to also allow schemas with different names, to account for scaling in the future and the possibility of having several tables.
- As SQLite is dynamically typed and not staticly typed like MySQL, we assume that the types of the data in the data.csv file will correctly match their corresponding data types as listed in the schema.

System Design
--------------
1. The database program is incorporated into a class, MyDatabase, that establishes the connection to the database as well as provides methods that allow for table creation, deletion, and display, as well as data insertion.
2. I check first if there are schema and data files in the data drop folder before proceeding with the program.
3. To create a table, we scan through each line of the CSV to assemble a SQL statement, with each row encompassing an additional segment added to the overall string that is to be executed at the end.
4. I check that each row in the schema.csv has a field name, width, and type. If any row does not match these specifications, I cancel the creation process.
5. When inserting data, we use a similar SQL statement building process as with creating a table. To optimize speed, I put each row into a list of tuples, which will be batch executed at the end. If any row has more columns than the header for that table, I skip over and do not add that row into the batch, but still allow for the other rows to be inserted.
6. I create a show table function, which queries all of the values for that table from the database and puts it into a display format, so that we may test our application.


Thank you for this opportunity. I hope my application is up to your company's standards and if needed, please do not hesitate to ask me any questions!

