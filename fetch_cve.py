import requests
from extensions import db
from models import CVE
from datetime import datetime
from app import create_app  
app = create_app()  
with app.app_context():  

    BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    def fetch_cve_data(start_index=0, results_per_page=100):
        url = f"{BASE_URL}?startIndex={start_index}&resultsPerPage={results_per_page}"
        response = requests.get(url)
        data = response.json()

        for item in data.get("vulnerabilities", []):
            cve_data = item["cve"]
            cve_id = cve_data["id"]
            description = cve_data["descriptions"][0]["value"]
            severity = cve_data.get("metrics", {}).get("cvssMetricV2", [{}])[0].get("cvssData", {}).get("baseScore", 0)
            print(f"Processing CVE: {cve_id}, Severity: {severity}")

            published_date = parse_date(cve_data["published"])
            last_modified = parse_date(cve_data["lastModified"])

            existing_cve = CVE.query.filter_by(cve_id=cve_id).first()
            if existing_cve:
                
                existing_cve.description = description
                existing_cve.severity = severity
                existing_cve.published_date = published_date
                existing_cve.last_modified = last_modified
            else:
              
                new_cve = CVE(
                    cve_id=cve_id,
                    description=description,
                    severity=severity,
                    published_date=published_date,
                    last_modified=last_modified
                )
                db.session.add(new_cve)

        try:
            db.session.commit()
            print("CVE Data Updated Successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error updating CVE data: {e}")

    def parse_date(date_str):
        """Handles different date formats returned by the API"""
        date_formats = ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%f"]
        for fmt in date_formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        print(f"Warning: Unrecognized date format {date_str}")
        return None  
    fetch_cve_data()  