import sqlite3

conn = sqlite3.connect("cves.db")
cursor = conn.cursor()


cursor.execute("PRAGMA table_info(cve);")
columns = cursor.fetchall()

print("Table Schema:")
for col in columns:
    print(col)

conn.close()
