import unittest
from app import app

class CVETestCase(unittest.TestCase):
    def test_get_cves(self):
        tester = app.test_client(self)
        response = tester.get("/cves/list")
        self.assertEqual(response.status_code, 200)

    def test_get_cve_by_id(self):
        tester = app.test_client(self)
        response = tester.get("/cves/CVE-2024-0001")
        self.assertIn(response.status_code, [200, 404])  

if __name__ == "__main__":
    unittest.main()
