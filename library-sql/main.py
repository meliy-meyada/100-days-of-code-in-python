import sqlite3


db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# RUN Create method will tell the cursor to execute an action. All actions in SQLite databases are expressed
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# RUN Push data to books-collection.db
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()