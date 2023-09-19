from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            #item.save_to_db() #uncomment this to induce a failure in the initial check
            #verifying that a 'test' item is NOT already present in the database.
            self.assertIsNone(ItemModel.find_by_name('test'), f'Found an item with name {item.name}, but expected not to.')
            item.save_to_db()
            #verifying that a 'test' item now exists in the database.
            self.assertIsNotNone(ItemModel.find_by_name('test'), f'An item is not present in the database with name {item.name}.')
            item.delete_from_db()
            #verifying that the 'test' item has been deleted from the database.
            self.assertIsNone(ItemModel.find_by_name('test'), f'Found an item with name {item.name}, but expected not to.')


#running this test in vs code it sometimes doesn't actually run the test. Test Results will show tests expected to run 1, but all other values are 0 followed by a message finished running tests. 
#haven't been able to find out why this is happening.
