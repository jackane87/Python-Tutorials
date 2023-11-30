from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel

class StoreTest(BaseTest):
    #verifying the store json method when no items are associated
    def test_store_json(self):
        store = StoreModel('Test Store 1')
        expected = {
            'name': 'Test Store 1',
            'items': []
        }
        self.assertDictEqual(store.json(), expected)

    #verifying the store json method when multiple items are associated
    def test_store_json_multiple_items(self):
        with self.app_context():
            store = StoreModel('Test Store 1')
            item1 = ItemModel('test_item1', 19.99, 1)
            item2 = ItemModel('test_item2', 10.99, 1)
            store.save_to_db()
            item1.save_to_db()
            item2.save_to_db()
            expected = {
                'name': 'Test Store 1',
                'items': [{'name': 'test_item1', 'price': 19.99}, {'name': 'test_item2', 'price': 10.99}]
            }
            self.assertDictEqual(store.json(), expected)
    
    #verify that on creation of a store it does not have any items associated with it.
    def test_create_store_items_empty(self):
        store = StoreModel('Test Store 1')
        self.assertListEqual(store.items.all(), [])

    #Verifying saving and deleting an item from the database.
    def test_store_crud(self):
        with self.app_context():
            #stores 1 and 2 created, but not saved to db yet.
            store1 = StoreModel('Test Store 1')
            store2 = StoreModel('Test Store 2')
            #verifying that neither store1 nor store2 can be found in the database yet.
            self.assertIsNone(StoreModel.find_by_name(store1.name),
                              "Found a store with name {}, but expected not to.".format(store1.name))
            self.assertIsNone(StoreModel.find_by_name(store2.name),
                              "Found a store with name {}, but expected not to.".format(store2.name))
            #saving just store 1
            store1.save_to_db()

            #verifying that store1 is now in the database, but store2 is still not present.
            self.assertIsNotNone(StoreModel.find_by_name(store1.name), f'Did not find a store with name {store1.name} when expected to.')
            self.assertIsNone(StoreModel.find_by_name(store2.name),
                              "Found a store with name {}, but expected not to.".format(store2.name))
            
            #deleting store1 from the database.
            store1.delete_from_db()

            #verifying that neither store1 nor store2 are in the database.
            self.assertIsNone(StoreModel.find_by_name(store1.name),
                              "Found a store with name {}, but expected not to.".format(store1.name))
            self.assertIsNone(StoreModel.find_by_name(store2.name),
                              "Found a store with name {}, but expected not to.".format(store2.name))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test Store 1')
            item = ItemModel('test_item', 19.99, 1)
            #must save the store first because the item needs the store in order to be saved.
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')