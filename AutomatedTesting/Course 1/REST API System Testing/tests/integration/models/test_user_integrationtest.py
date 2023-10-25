from tests.integration.Integration_base_test import BaseTest
from models.user import UserModel


class UserTest(BaseTest):
    #verifying the store json method when no items are associated
    def test_store_json(self):
        store = StoreModel('Test Store 1')
        expected = {
            'name': 'Test Store 1',
            'items': []
        }
        self.assertDictEqual(store.json(), expected)