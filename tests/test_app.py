import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello(self):
        response = self.app.get("/")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Hello, World!")
    
    def test_health(self):
        response = self.app.get("/health")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "healthy")

if __name__ == "__main__":
    unittest.main()