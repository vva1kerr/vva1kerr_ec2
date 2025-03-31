import sqlite3

con = sqlite3.connect("data/tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)")

con.commit()

con.close()