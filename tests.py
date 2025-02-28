import unittest
from app import app

class CVETestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_cves(self):
        response = self.client.get("/cves/list")
        self.assertEqual(response.status_code, 200)

    def test_get_cve_details(self):
        response = self.client.get("/cves/CVE-2023-1234")
        self.assertIn(response.status_code, [200, 404])

if __name__ == "__main__":
    unittest.main()
