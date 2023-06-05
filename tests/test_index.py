import unittest
from app import create_app


class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index(self):
        with self.app.test_client() as test_client:
            response = test_client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>RGB controller</h1>', response.data)
