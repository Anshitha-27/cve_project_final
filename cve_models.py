from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    published_date = db.Column(db.String(20), nullable=False)
    last_modified_date = db.Column(db.String(20), nullable=False)
