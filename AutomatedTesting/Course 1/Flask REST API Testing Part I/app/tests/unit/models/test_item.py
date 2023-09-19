from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_item_creation(self):
        monitor = ItemModel('Test Monitor', 399.99)
        self.assertEqual(monitor.name, 'Test Monitor', "The name of the  item after creation does not equal the constructor argument") #The third argument is an optional error message. If not defined, a default error message displays.
        self.assertEqual(monitor.price, 399.99)

    def test_item_json(self):
        monitor = ItemModel('Test Monitor', 399.99)
        expected = {'name': 'Test Monitor', 'price': 399.99}
        self.assertEqual(monitor.json(), expected, f'The JSON export of the item is incorrect. Received {monitor.json()}, Expexted {expected}')

