from tests.unit.unit_base_test import UnitBaseTest
from models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")
        #This is confirming that the store_id for the item created above is set to 1
        self.assertEqual(item.store_id, 1)
        #is is confirming that the the item is associated with a store, but since the store doesn't already exist (because this is just a unit test) it returns None because it can't be found.
        self.assertIsNone(item.store)


    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
