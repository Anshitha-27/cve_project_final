document.addEventListener("DOMContentLoaded", function () {
    fetch("/cves/list?page=1&per_page=10")  // Fetch CVE data from Flask API
        .then(response => response.json())  // Convert response to JSON
        .then(data => {
            const tableBody = document.getElementById("cve-table-body");
            data.cves.forEach(cve => {
                let row = document.createElement("tr");
                row.innerHTML = `
                    <td><a href="/cves/${cve.cve_id}">${cve.cve_id}</a></td>
                    <td>${cve.description}</td>
                    <td>${cve.published_date}</td>
                    <td>${cve.last_modified}</td>
                    <td>${cve.base_score || "N/A"}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error("Error fetching CVE data:", error));
});
