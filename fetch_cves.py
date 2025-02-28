import requests
import json
from cve_models import db, CVE  # Import the database model
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cves.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cves():
    """Fetches CVE data from NVD API and stores it in the database."""
    print("🚀 Fetching CVEs from NVD API...")
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()
        cve_items = data.get("vulnerabilities", [])

        print(f"{len(cve_items)} CVEs fetched!")

        with app.app_context():
            for item in cve_items:
                cve_id = item["cve"]["id"]
                description = item["cve"]["descriptions"][0]["value"]

                existing_cve = CVE.query.filter_by(cve_id=cve_id).first()
                if not existing_cve:
                    new_cve = CVE(cve_id=cve_id, description=description)
                    db.session.add(new_cve)

            db.session.commit()
            print("CVEs stored in the database!")

    else:
        print(f"Error: API returned status code {response.status_code}")

# Run script
if __name__ == "__main__":
    fetch_cves()
