from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    """Class representing all tests for the users resource"""
    def test_register_user(self):
        """method tests the successful registration of a user via the api"""
        #initializing a client so we can make api calls
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                response = client.post('/register', json={'username': 'testusername1', 'password': 'testpassword1'})
                #verifying that the status code is the expected 201 based on the user resource
                self.assertEqual(response.status_code, 201)
                #verifying that the expected user was successfully registered.
                self.assertIsNotNone(UserModel.find_by_username('testusername1'))
                #verifying that the correct response message was received.
                self.assertDictEqual({'message': 'User created successfully.'}, json.loads(response.data)) #json.loads is used to convert the json string received with the response into a Dictionary so that it can be compared to the expected resuls

    def test_register_and_login(self):
        #initializing a client so we can make api calls
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                #user is registered
                client.post('/register', json={'username': 'testusername1', 'password': 'testpassword1'})
                #post to auth endpoint with user credentials
                auth_response = client.post('/auth', json={'username': 'testusername1', 'password': 'testpassword1'}, headers={'Content-Typpe': 'application/json'})
                #verifying the response contains the string 'access_token' which is should if the user was authenticated.
                self.assertIn('access_token', json.loads(auth_response.data).keys()) #converting json received in response and converting to a dictionary. Then getting a list of keys for the created dictionary. Then we expect access_token to be in that list.

    def test_register_duplicate_user(self):
        #initializing a client so we can make api calls
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                #user is registered
                client.post('/register', json={'username': 'testusername1', 'password': 'testpassword1'})
                response = client.post('/register', json={'username': 'testusername1', 'password': 'testpassword1'})
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message' : 'A user with that username already exists'}, json.loads(response.data))
