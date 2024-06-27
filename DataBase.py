import sqlite3

connection = sqlite3.connect('129database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL
)
''')

connection.commit()
connection.close()