from models.store import StoreModel
from models.item import ItemModel
from models.user import UserModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    """Class representing all tests for the Item resource"""
    def setUp(self):
        #Calling the basetest setup method because the SetUp method here is overriding it.
        super(ItemTest, self).setUp()
        with self.app() as client:
            #getting an access token that can be used in requests
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth', data=json.dumps({'username': 'test', 'password': '1234'}), headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                #the GET request does not have authorization headers passed with it, so a 401 status code is expected.
                response = client.get('/item/test')
                self.assertEqual(response.status_code, 401)


    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                #passing in the authorization header, but the item 'test' is not present.
                response = client.get('/item/test', headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Item not found'}, json.loads(response.data))

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                ItemModel('test', 35.01, 1).save_to_db()
                response = client.get('/item/test', headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': 'test', 'price': 35.01}, json.loads(response.data))
                
    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                ItemModel('test', 35.01, 1).save_to_db()
                response = client.delete('/item/test', headers={'Authorization': self.access_token})
                self.assertIsNone(ItemModel.find_by_name('test'))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'}, json.loads(response.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                response = client.post('/item/test', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(ItemModel.find_by_name('test'))


    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                client.post('/item/test', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                response = client.post('/item/test', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "An item with name 'test' already exists."}, json.loads(response.data))
        
    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                response = client.put('/item/test', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 200)
                #checking to see that the item was created with the correct price
                self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
                self.assertDictEqual({'name': 'test', 'price': 17.99}, json.loads(response.data))


    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/teststore1')
                client.post('/store/teststore2')
                client.post('/item/test', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                response = client.put('/item/test', json={'price': 12.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test').price, 12.99)
                self.assertDictEqual({'name': 'test', 'price': 12.99}, json.loads(response.data))


    def test_item_list(self):
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                client.post('/store/teststore1')
                client.post('/store/teststore2')
                client.post('/item/test1', json={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                client.post('/item/test2', json={'price': 18.99, 'store_id': 1}, headers={'Authorization': self.access_token})
                client.post('/item/test3', json={'price': 10.99, 'store_id': 2}, headers={'Authorization': self.access_token})
                response = client.get('/items', headers={'Authorization': self.access_token})
                self.assertEqual(response.status_code, 200)
                #verifying that the correct response message was received when listing all stores.
                self.assertDictEqual({'items': [{'name': 'test1', 'price': 17.99}, {'name': 'test2', 'price': 18.99}, {'name': 'test3', 'price': 10.99}]}, json.loads(response.data))