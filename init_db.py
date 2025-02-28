from app import app, db

# Ensure the database tables are created inside the app context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
