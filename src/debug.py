import sqlite3

conn = sqlite3.connect("fitpal.db")
c = conn.cursor()
c.execute("SELECT * FROM workout_history")
print(c.fetchall())