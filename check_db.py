import sqlite3


conn = sqlite3.connect("cves.db")
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📌 Existing Tables in Database:", tables)

conn.close()
