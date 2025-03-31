import os
import sqlite3
from dotenv import load_dotenv
import sys
sys.path.append("src/auth")
from login import hash_password

load_dotenv()

con = sqlite3.connect("data/tutorial.db")

cur = con.cursor()

# Hash the password before storing
hashed_password = hash_password(os.getenv("PASSWORD"))

data = [
    (os.getenv("USERNAME"), os.getenv("EMAIL"), hashed_password),
]

cur.executemany("""
    INSERT INTO users (username, email, password) VALUES(?, ?, ?)
""", data)

con.commit()

con.close()