CVE API Documentation

## Get All CVEs (With Filters)
**Endpoint:** `GET /api/cves`  
**Query Params:**  
- `id=CVE-XXXX-YYYY` → Filter by CVE ID  
- `year=YYYY` → Filter by Year  
- `min_score=X&max_score=Y` → Filter by CVE Score  
- `last_modified=N` → Filter by Last Modified Days  

**Example Request:**  
`GET /api/cves?year=2023&min_score=5.0&max_score=9.0`

**Response:**
```json
[
    {
        "id": "CVE-2023-12345",
        "description": "A critical vulnerability in XYZ software.",
        "severity": "7.8",
        "published_date": "2023-04-12",
        "last_modified": "2023-06-01"
    }
]
