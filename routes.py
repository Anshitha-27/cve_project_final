from flask import Blueprint, jsonify, request, render_template
from models import CVE
from sqlalchemy import extract
from datetime import datetime, timedelta

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def home():
    return render_template("index.html")  # Load the UI


@app_routes.route("/cves/<cve_id>", methods=["GET"])
def get_cve_details(cve_id):
    cve = CVE.query.filter_by(cve_id=cve_id).first()
    if cve:
        return render_template("cve_detail.html", cve=cve)
    else:
        return "CVE Not Found", 404


@app_routes.route("/cves/list", methods=["GET"])
def get_cves():
    results_per_page = request.args.get("resultsPerPage", type=int, default=10)
    page = request.args.get("page", type=int, default=1)

    query = CVE.query  

   
    cve_id = request.args.get("id")
    if cve_id:
        query = query.filter(CVE.cve_id == cve_id)

    year = request.args.get("year", type=int)
    if year:
        query = query.filter(extract('year', CVE.published_date) == year)

    min_score = request.args.get("min_score", type=float)
    max_score = request.args.get("max_score", type=float)
    if min_score is not None and max_score is not None:
        query = query.filter(CVE.severity >= min_score, CVE.severity <= max_score)
    elif min_score is not None:
        query = query.filter(CVE.severity >= min_score)
    elif max_score is not None:
        query = query.filter(CVE.severity <= max_score)

    last_modified_days = request.args.get("last_modified", type=int)
    if last_modified_days is not None:
        cutoff_date = datetime.utcnow() - timedelta(days=last_modified_days)
        query = query.filter(CVE.last_modified.isnot(None), CVE.last_modified >= cutoff_date)

    if results_per_page:
        paginated_cves = query.paginate(page=page, per_page=results_per_page)
        cves = paginated_cves.items
        total = paginated_cves.total
    else:
        cves = query.all()  # Return all results if no limit is specified
        total = len(cves)

    return jsonify({
        "total": total,
        "cves": [
            {
                "id": cve.cve_id,
                "description": cve.description,
                "severity": cve.severity,
                "published_date": cve.published_date.strftime("%Y-%m-%d"),
                "last_modified": cve.last_modified.strftime("%Y-%m-%d") if cve.last_modified else None
            }
            for cve in cves
        ]
    })
