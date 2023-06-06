import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM users WHERE username="vroman";')
for row in rows:
    print(row)
cursor.close()
conn.close()
