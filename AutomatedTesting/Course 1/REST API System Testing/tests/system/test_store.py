from models.store import StoreModel
from tests.base_test import BaseTest
import json


class StorerTest(BaseTest):
    """Class representing all tests for the Store resource"""
    def test_create_store(self):
        """method tests the successful creation of a store via the api"""
        #initializing a client so we can make api calls
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                response = client.post('/store/teststore1')
                #verifying that the status code is the expected 201 based on the store resource
                self.assertEqual(response.status_code, 201)
                #verifying that the expected store was successfully created.
                self.assertIsNotNone(StoreModel.find_by_name('teststore1'))

    def test_create_duplicate_store(self):
        """method tests attempted creation of a duplicate store via the api"""
        #initializing a client so we can make api calls
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                #creating a store
                client.post('/store/teststore1')
                #attempting to create the same store and storing to response variable
                response = client.post('/store/teststore1')
                #verifying that the status code is the expected 400 based on the store resource
                self.assertEqual(response.status_code, 400)
                #verifying that the correct response message was received.
                self.assertDictEqual({'message': "A store with name 'teststore1' already exists."}, json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                client.post('/store/teststore1')
                response = client.delete('/store/teststore1')
                #verifying that the correct response message was received when deleting a store.
                self.assertDictEqual({'message': 'Store deleted'}, json.loads(response.data))

    def test_find_store(self):
        with self.app() as client:
            #self.app_context is initialized because the methods tested all saving data to the database
            with self.app_context():
                client.post('/store/teststore1')
                response = client.get('/store/teststore1')
                #verifying that the correct response message was received when deleting a store.
                self.assertDictEqual({'name': 'teststore1', 'items': []}, json.loads(response.data))

    def test_store_not_found(self):
        pass

    def test_store_found_with_items(self):
        pass

    def test_store_list(self):
        pass

    def test_store_list_with_items(self):
        pass