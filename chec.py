import os

db_path = "cve_data.db"

if os.path.exists(db_path):
    print("✅ Database exists:", db_path)
else:
    print("❌ Database not found. You need to create it.")
