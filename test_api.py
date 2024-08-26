import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def test_get_users(self):
        response = requests.get(f'{self.BASE_URL}/users')
        
        # Check the status code
        self.assertEqual(response.status_code, 200)
        
        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')
        
        # Check if we get a list of users
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # Check if the first user has the expected keys
        first_user = data[0]
        self.assertIn('id', first_user)
        self.assertIn('name', first_user)
        self.assertIn('username', first_user)
        self.assertIn('email', first_user)

if __name__ == '__main__':
    unittest.main()
