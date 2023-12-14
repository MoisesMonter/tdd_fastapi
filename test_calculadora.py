import unittest
from fastapi.testclient import TestClient
from minha_app import app

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        client = TestClient(app)
        response = client.get("/somar/3/5")
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"resultado": 8})
#RED
if __name__ == '__main__':
    unittest.main()