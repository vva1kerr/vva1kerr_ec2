import sqlite3
con = sqlite3.connect("data/tutorial.db")

cur = con.cursor()

cur.execute("SELECT * FROM users")
# cur.execute("SELECT * FROM users WHERE username = 'vva1kerr'")
# cur.execute("SELECT * FROM users WHERE username = 'vva1kerr' AND email = 'account@vva1kerr.com'")
# cur.execute("SELECT * FROM users WHERE username = 'vva1kerr' OR email = 'account@vva1kerr.com'")
# cur.execute("SELECT username FROM users")

print(cur.fetchall())