#importing the BaseTest class which has unittest and the app imported 
from tests.system.base_test import BaseTest
import json

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)
            #json.loads() takes the response data and converts it from a string into a
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})