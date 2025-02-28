from extensions import db  # Import db from extensions
from datetime import datetime  # Import datetime for DateTime fields

class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), nullable=True)
    published_date = db.Column(db.DateTime, nullable=False)
    last_modified = db.Column(db.DateTime, nullable=True) 
    def __repr__(self):
        return f"<CVE {self.cve_id}>"
