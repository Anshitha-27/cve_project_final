import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cve_models import db


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


DATABASE_PATH = os.path.join(BASE_DIR, "cve_data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

if __name__ == "__main__":
    print("Starting database initialization...")

    try:
        with app.app_context():
            print("App context created successfully!")


            if os.path.exists(DATABASE_PATH):
                print(f"Database file already exists at: {DATABASE_PATH}")
            else:
                print(f" Database file does not exist yet at: {DATABASE_PATH}")


            db.create_all()
            print("Tables created successfully!")


            open(DATABASE_PATH, "a").close() 
            print("Empty database file manually created!")

            conn = db.engine.raw_connection()
            conn.commit() 
            conn.close()
            print("SQLite database file committed and written!")


            db.session.commit()
            db.session.close()
            print("Database session closed!")

            if os.path.exists(DATABASE_PATH):
                print(f"Database file `cves.db` successfully created at: {DATABASE_PATH}")
            else:
                print("Database file was NOT created! (Possible permission issue)")

    except Exception as e:
        print(f"ERROR: {e}")
