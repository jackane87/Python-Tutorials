from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        #Verifying saving and deleting an item from the database.
        with self.app_context():
            #creating a store in the database. Store needs to exist as a store ID is required for an Item and if a store ID isn't present in the Store table a foreign key constraint error will occur.
            StoreModel('Test Store 1').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test_item', 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(item.store.name, 'test_store')
