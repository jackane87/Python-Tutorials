from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest

class StoreTest(UnitBaseTest):
    def test_store_creation(self):
        store = StoreModel("Test Store 1")
        self.assertEqual(store.name, 'Test Store 1', 'The name of the store after creation does not equal the constructor argument.')
 